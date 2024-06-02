import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
import bdd

def lireconf():
    with open("./config.conf", 'r') as conf:
        file = conf.readlines()
        data = False
        listeinfo = []
        for line in file:
            if line[0:3] == "###":
                continue
            elif line.strip() == "[bdd conf]":
                data = True
            elif data == True:
                listeinfo.append(line.strip().split(':')[1].strip())
        return listeinfo[0], listeinfo[1], listeinfo[2], listeinfo[3], listeinfo[4], listeinfo[5]

def change_date_form(date):
    """Change la date de format JJ/MM/AAAA à AAAA-MM-JJ"""
    date = date.split('-')
    return f"{date[2]}-{date[1]}-{date[0]}"

def dict_to_list(dico):
    liste = []
    for key in dico:
        liste.append(dico[key])
    return liste

class SymphonicaSonata:
    idrese=None
    def __init__(self) -> None:
        self.lookup = TemplateLookup(directories=["template"], input_encoding='utf-8', module_directory="mod")
    
    @cherrypy.expose
    def index(self) -> None:
        template = self.lookup.get_template('index.html')
        print(sql.info_index())
        return template.render(concerts=sql.info_index())
    
    @cherrypy.expose
    def template(self):
        template = self.lookup.get_template('template.html')
        return template.render()
    
    @cherrypy.expose
    def affParMorceau(self):
        list_morc = sql.return_all_morc()
        tmpl = self.lookup.get_template("affParMorceau.html")
        return tmpl.render(morceaux=list_morc)
    
    @cherrypy.expose
    def affParGenre(self):
        """Affiche les concerts par genre musical
        """
        list_genre = sql.return_all_genre()
        tmpl = self.lookup.get_template("affParGenre.html")
        return tmpl.render(genres=list_genre)
        
    @cherrypy.expose
    def affParDate(self):
        """Affiche les concerts par date
        """
        tmpl = self.lookup.get_template("affParDate.html")
        return tmpl.render()
        
    @cherrypy.expose
    def affParCompositeur(self):
        """
        Affiche les concerts par compositeur"""
        liste_comp = sql.return_all_comp()
        tmpl = self.lookup.get_template("affParCompositeur.html")
        return tmpl.render(compositeurs=liste_comp)
    
    @cherrypy.expose
    def insertPage(self):
        tables = ["batiment", "salle", "concert", "compositeur", "morceau", "jouer"]
        tmpl = self.lookup.get_template("seltableinsert.html")
        return tmpl.render(tables=tables)
    
    @cherrypy.expose
    def delpage(self):
        tables = ["batiment", "salle", "concert", "compositeur", "morceau"]
        tmpl = self.lookup.get_template("seltable.html")
        return tmpl.render(tables=tables)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def deleteTable(self, table=None):
        headers, content = sql.get_table_content(table)
        tmpl = self.lookup.get_template("deleteTable.html")
        return tmpl.render(table=table, headers=headers, table_content=content)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def deleteEntry(self, table=None, id=None):
        sql.delete_entry(table, id)
        raise cherrypy.HTTPRedirect(f"/index")
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche_par_compositeur(self, composer=None):
        """
        Recherche les concerts par compositeur
        """
        concerts = sql.get_concerts_by_composer(composer)
        tmpl = self.lookup.get_template("Recherche.html")
        ph=f"Concerts du compositeur : {composer}"
        return tmpl.render(ph = ph, concerts=concerts)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche_par_morceau(self, morceau=None):
        """
        Recherche les concerts par morceau
        """
        concerts = sql.get_concerts_by_morceau(morceau)
        tmpl = self.lookup.get_template("Recherche.html")
        ph=f"Concerts contenant le morceau : {morceau}"
        return tmpl.render(ph = ph, concerts=concerts)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche_par_genre(self, genre=None):
        """
        Recherche les concerts par genre
        """
        concerts = sql.get_concerts_by_genre(genre)
        tmpl = self.lookup.get_template("Recherche.html")
        ph=f"Concerts du genre : {genre}"
        return tmpl.render(ph = ph, concerts=concerts)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche_par_date(self, concertDate=None):
        """
        Recherche les concerts par date
        """
        concerts = sql.get_concerts_by_date(concertDate)
        tmpl = self.lookup.get_template("Recherche.html")
        ph=f"Concerts après le {concertDate}"
        return tmpl.render(ph = ph, concerts=concerts)
    
    @cherrypy.expose
    def updatePage(self):
        tmp1 = self.lookup.get_template("selTableMaj.html")
        return tmp1.render(tables=["batiment", "salle", "concert", "compositeur", "morceau"])
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def selectUpdate(self, table=None):
        entries = sql.get_table_content(table)
        tmpl = self.lookup.get_template("selectUpdate.html")
        return tmpl.render(table=table, entries=entries)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def updateTable(self, table=None):
        headers, content = sql.get_table_content(table)
        tmpl = self.lookup.get_template("updateTable.html")
        return tmpl.render(table=table, headers=headers, table_content=content)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def submitUpdate(self, entry_id, **data):
        sql.update_entry(entry_id, data)
        raise cherrypy.HTTPRedirect('/selectUpdate')
    
    @cherrypy.expose
    def concertDetails(self, id_):
        """
        
        """
        concert = sql.get_concert_details(id_)
        print(concert[0])
        morceau = sql.get_concert_prg(id_)
        tmpl = self.lookup.get_template("concertDetails.html")
        return tmpl.render(concert_=concert[0], morc=morceau)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def reserver(self, concert_id):
        self.idrese = concert_id
        tmpl = self.lookup.get_template("reserver.html")
        return tmpl.render()
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def submitForm(self, nom, prenom):
        n,p,nc=sql.reserver(self.idrese, nom, prenom)
        tmpl = self.lookup.get_template("confirmation.html")
        return tmpl.render(nom=n, prenom=p,concert=nc)
    
    @cherrypy.expose
    def rese(self):
        tmpl = self.lookup.get_template("showrese.html")
        return tmpl.render(rese = sql.showrese())
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def insertIntoTable(self, table=None):
        headers, _ = sql.get_table_content(table)
        formatted_headers = []

        for header in headers:
            is_primary_key = f"id_{table}" in header
            is_foreign_key = "id_" in header
            options = []

            if is_foreign_key:
                foreign_table = header[3:]
                options = sql.get_foreign_key_options(foreign_table)
            
            formatted_headers.append({
                "name": header,
                "is_primary_key": is_primary_key,
                "is_foreign_key": is_foreign_key,
                "options": options
            })

        tmpl = self.lookup.get_template("insertIntoTable.html")
        return tmpl.render(table=table, headers=formatted_headers)
    
    
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def insertEntry(self, table=None, **data):
        donnee=dict_to_list(data)
        sql.add_valeur(table, donnee)
        raise cherrypy.HTTPRedirect(f"/index")

if __name__ == "__main__":
    address, port, user, mdp, database, chem = lireconf()
    port = int(port)
    print(address, port, user, mdp, database, chem)
    print("connexion")
    sql = bdd.bdd(address, user, mdp, port, chem)
    print("connexion établie\n")
    sql.info_index()
    cherrypy.quickstart(SymphonicaSonata(), config="config.txt")

# Pour lancer le serveur, il suffit de lancer ce fichier.
