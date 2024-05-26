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

class SymphonicaSonata:
    def __init__(self) -> None:
        self.lookup = TemplateLookup(directories=["template"], input_encoding='utf-8', module_directory="mod")
    
    @cherrypy.expose
    def index(self) -> None:
        template = self.lookup.get_template('index.html')
        return template.render(concert=sql.info_index())
    
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
        ...
        
    @cherrypy.expose
    def affParDate(self):
        ...
        
    @cherrypy.expose
    def affParCompositeur(self):
        liste_comp = sql.return_all_comp()
        tmpl = self.lookup.get_template("affParCompositeur.html")
        return tmpl.render(compositeurs=liste_comp)
    
    @cherrypy.expose
    def insertPage(self):
        ...
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche(self, composer=None):
        concerts = sql.get_concerts_by_composer(composer)
        tmpl = self.lookup.get_template("Recherche.html")
        ph=f"Concerts en lien avec : {composer}"
        return tmpl.render(ph = ph, composer=composer, concerts=concerts)
    
    @cherrypy.expose
    def adminPage(self):
        ...
    
    @cherrypy.expose
    def concertDetails(self, id_):
        concert = sql.get_concert_details(id_)
        morceau = sql.get_concert_prg(id_)
        tmpl = self.lookup.get_template("concertDetails.html")
        return tmpl.render(concert_=concert[0], morc=morceau)

if __name__ == "__main__":
    address, port, user, mdp, database, chem = lireconf()
    port = int(port)
    print(address, port, user, mdp, database, chem)
    print("connexion")
    sql = bdd.bdd(address, user, mdp, port, chem)
    print("connexion établie\n")
    sql.info_index()
    cherrypy.quickstart(SymphonicaSonata(), config="config.txt")
