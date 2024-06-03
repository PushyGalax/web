##########################################################
###                     IMPORTATION                    ###
##########################################################

import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
import bdd

##########################################################
###                     FONCTIONS                      ###
##########################################################

def lireconf():
    """
    Lit le fichier de configuration et retourne les informations de connexion à la base de données.

    Fonctionnement :
    - Ouvre et lit le fichier `config.conf`.
    - Recherche la section `[bdd conf]` et récupère les informations suivantes :
      adresse, port, utilisateur, mot de passe, base de données et chemin.
    - Retourne ces informations sous forme de tuple.
    """
    with open("./config.conf", 'r') as conf:
        file = conf.readlines()
        data = False
        listeinfo = []
        for line in file:
            if line[0:3] == "###":
                continue
            elif line.strip() == "[bdd conf]":
                data = True
            elif data:
                listeinfo.append(line.strip().split(':')[1].strip())
        return listeinfo[0], listeinfo[1], listeinfo[2], listeinfo[3], listeinfo[4], listeinfo[5]

def change_date_form(date):
    """
    Change le format d'une date de JJ/MM/AAAA à AAAA-MM-JJ.

    Paramètre :
    - date : chaîne de caractères représentant une date au format JJ/MM/AAAA

    Retour :
    - Chaîne de caractères représentant la date au format AAAA-MM-JJ
    """
    date = date.split('-')
    return f"{date[2]}-{date[1]}-{date[0]}"

def dict_to_list(dico):
    """
    Convertit un dictionnaire en liste de ses valeurs.

    Paramètre :
    - dico : dictionnaire à convertir

    Retour :
    - Liste des valeurs du dictionnaire
    """
    return list(dico.values())

##########################################################
###                     CLASSES                        ###
##########################################################

class SymphonicaSonata:
    """
    Classe principale pour l'application web Symphonica Sonata.

    Attributs :
    - lookup : objet TemplateLookup pour gérer les templates Mako
    - idrese : identifiant du concert pour la réservation
    """
    idrese = None

    def __init__(self) -> None:
        self.lookup = TemplateLookup(directories=["template"], input_encoding='utf-8', module_directory="mod")
    
    @cherrypy.expose
    def index(self) -> None:
        """
        Page d'accueil affichant les concerts à venir.

        Fonctionnement :
        - Récupère les informations des prochains concerts depuis la base de données.
        - Affiche les concerts à l'aide du template `index.html`.
        """
        template = self.lookup.get_template('index.html')
        return template.render(concerts=sql.info_index())
    
    @cherrypy.expose
    def template(self):
        """
        Page de test pour les templates.

        Retour :
        - Rendu du template `template.html`.
        """
        template = self.lookup.get_template('template.html')
        return template.render()
    
    @cherrypy.expose
    def affParMorceau(self):
        """
        Affiche les concerts par morceau.

        Fonctionnement :
        - Récupère la liste de tous les morceaux depuis la base de données.
        - Affiche les morceaux à l'aide du template `affParMorceau.html`.
        """
        list_morc = sql.return_all_morc()
        tmpl = self.lookup.get_template("affParMorceau.html")
        return tmpl.render(morceaux=list_morc)
    
    @cherrypy.expose
    def affParGenre(self):
        """
        Affiche les concerts par genre musical.

        Fonctionnement :
        - Récupère la liste de tous les genres musicaux prédéfinis.
        - Affiche les genres à l'aide du template `affParGenre.html`.
        """
        list_genre = sql.return_all_genre()
        tmpl = self.lookup.get_template("affParGenre.html")
        return tmpl.render(genres=list_genre)
    
    @cherrypy.expose
    def affParDate(self):
        """
        Affiche les concerts par date.

        Retour :
        - Rendu du template `affParDate.html`.
        """
        tmpl = self.lookup.get_template("affParDate.html")
        return tmpl.render()
    
    @cherrypy.expose
    def affParCompositeur(self):
        """
        Affiche les concerts par compositeur.

        Fonctionnement :
        - Récupère la liste de tous les compositeurs depuis la base de données.
        - Affiche les compositeurs à l'aide du template `affParCompositeur.html`.
        """
        liste_comp = sql.return_all_comp()
        tmpl = self.lookup.get_template("affParCompositeur.html")
        return tmpl.render(compositeurs=liste_comp)
    
    @cherrypy.expose
    def insertPage(self):
        """
        Page d'insertion de nouvelles entrées dans les tables.

        Retour :
        - Rendu du template `seltableInsert.html` avec la liste des tables.
        """
        tables = ["batiment", "salle", "concert", "compositeur", "morceau", "jouer"]
        tmpl = self.lookup.get_template("seltableInsert.html")
        return tmpl.render(tables=tables)
    
    @cherrypy.expose
    def delpage(self):
        """
        Page de suppression d'entrées dans les tables.

        Retour :
        - Rendu du template `seltable.html` avec la liste des tables.
        """
        tables = ["batiment", "salle", "concert", "compositeur", "morceau"]
        tmpl = self.lookup.get_template("seltable.html")
        return tmpl.render(tables=tables)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def deleteTable(self, table=None):
        """
        Page de sélection des entrées à supprimer dans une table.

        Paramètre :
        - table : nom de la table

        Fonctionnement :
        - Récupère le contenu et les en-têtes de la table depuis la base de données.
        - Affiche les entrées à l'aide du template `deleteTable.html`.
        """
        headers, content = sql.get_table_content(table)
        tmpl = self.lookup.get_template("deleteTable.html")
        return tmpl.render(table=table, headers=headers, table_content=content)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def deleteEntry(self, table=None, id=None):
        """
        Supprime une entrée spécifique dans une table.

        Paramètres :
        - table : nom de la table
        - id : identifiant de l'entrée à supprimer

        Fonctionnement :
        - Supprime l'entrée de la table dans la base de données.
        - Redirige vers la page d'accueil.
        """
        sql.delete_entry(table, id)
        raise cherrypy.HTTPRedirect(f"/index")
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche_par_compositeur(self, composer=None):
        """
        Recherche les concerts par compositeur.

        Paramètre :
        - composer : nom du compositeur

        Fonctionnement :
        - Récupère les concerts associés au compositeur depuis la base de données.
        - Affiche les résultats à l'aide du template `Recherche.html`.
        """
        concerts = sql.get_concerts_by_composer(composer)
        tmpl = self.lookup.get_template("Recherche.html")
        ph = f"Concerts du compositeur : {composer}"
        return tmpl.render(ph=ph, concerts=concerts)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche_par_morceau(self, morceau=None):
        """
        Recherche les concerts par morceau.

        Paramètre :
        - morceau : nom du morceau

        Fonctionnement :
        - Récupère les concerts contenant le morceau depuis la base de données.
        - Affiche les résultats à l'aide du template `Recherche.html`.
        """
        concerts = sql.get_concerts_by_morceau(morceau)
        tmpl = self.lookup.get_template("Recherche.html")
        ph = f"Concerts contenant le morceau : {morceau}"
        return tmpl.render(ph=ph, concerts=concerts)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche_par_genre(self, genre=None):
        """
        Recherche les concerts par genre.

        Paramètre :
        - genre : genre musical

        Fonctionnement :
        - Récupère les concerts associés au genre depuis la base de données.
        - Affiche les résultats à l'aide du template `Recherche.html`.
        """
        concerts = sql.get_concerts_by_genre(genre)
        tmpl = self.lookup.get_template("Recherche.html")
        ph = f"Concerts du genre : {genre}"
        return tmpl.render(ph=ph, concerts=concerts)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def Recherche_par_date(self, concertDate=None):
        """
        Recherche les concerts par date.

        Paramètre :
        - concertDate : date du concert

        Fonctionnement :
        - Récupère les concerts ayant lieu après la date spécifiée depuis la base de données.
        - Affiche les résultats à l'aide du template `Recherche.html`.
        """
        concerts = sql.get_concerts_by_date(concertDate)
        tmpl = self.lookup.get_template("Recherche.html")
        ph = f"Concerts après le {concertDate}"
        return tmpl.render(ph=ph, concerts=concerts)
    
    @cherrypy.expose
    def updatePage(self):
        """
        Page de sélection des tables pour mise à jour.

        Retour :
        - Rendu du template `selTableMaj.html` avec la liste des tables.
        """
        tmp1 = self.lookup.get_template("selTableMaj.html")
        return tmp1.render(tables=["batiment", "salle", "concert", "compositeur", "morceau"])

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def updateTable(self, table=None):
        """
        Page de mise à jour des entrées d'une table spécifique.

        Paramètre :
        - table : nom de la table

        Fonctionnement :
        - Récupère le contenu et les en-têtes de la table depuis la base de données.
        - Affiche les entrées à l'aide du template `updateTable.html`.
        """
        headers, content = sql.get_table_content(table)
        tmpl = self.lookup.get_template("updateTable.html")
        return tmpl.render(table=table, headers=headers, table_content=content)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def updateForm(self, table, entry_id):
        """
        Formulaire de mise à jour d'une entrée spécifique.

        Paramètres :
        - table : nom de la table
        - entry_id : identifiant de l'entrée à mettre à jour

        Fonctionnement :
        - Récupère les détails de l'entrée depuis la base de données.
        - Affiche le formulaire de mise à jour à l'aide du template `updateform.html`.
        """
        entry = sql.get_entry_by_id(table, entry_id)
        template = self.lookup.get_template('updateform.html')
        return template.render(table=table, entry=entry, id_=f"id_{table}")
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def submitUpdate(self, table, entry_id, **data):
        """
        Soumet la mise à jour d'une entrée spécifique.

        Paramètres :
        - table : nom de la table
        - entry_id : identifiant de l'entrée à mettre à jour
        - data : dictionnaire contenant les nouvelles valeurs des colonnes

        Fonctionnement :
        - Met à jour l'entrée dans la base de données.
        - Redirige vers la page d'accueil.
        """
        sql.update_entry(table, entry_id, data)
        raise cherrypy.HTTPRedirect(f'/index')
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def submitUpdate(self, entry_id, **data):
        """
        Soumet la mise à jour d'une entrée spécifique.

        Paramètres :
        - entry_id : identifiant de l'entrée à mettre à jour
        - data : dictionnaire contenant les nouvelles valeurs des colonnes

        Fonctionnement :
        - Met à jour l'entrée dans la base de données.
        - Redirige vers la page de sélection pour mise à jour.
        """
        sql.update_entry(entry_id, data)
        raise cherrypy.HTTPRedirect('/selectUpdate')
    
    @cherrypy.expose
    def concertDetails(self, id_):
        """
        Affiche les détails d'un concert spécifique.

        Paramètre :
        - id_ : identifiant du concert

        Fonctionnement :
        - Récupère les détails du concert et le programme depuis la base de données.
        - Affiche les détails à l'aide du template `concertDetails.html`.
        """
        concert = sql.get_concert_details(id_)
        morceau = sql.get_concert_prg(id_)
        tmpl = self.lookup.get_template("concertDetails.html")
        return tmpl.render(concert_=concert[0], morc=morceau)
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def reserver(self, concert_id):
        """
        Page de réservation pour un concert spécifique.

        Paramètre :
        - concert_id : identifiant du concert

        Fonctionnement :
        - Stocke l'identifiant du concert pour la réservation.
        - Affiche le formulaire de réservation à l'aide du template `reserver.html`.
        """
        self.idrese = concert_id
        tmpl = self.lookup.get_template("reserver.html")
        return tmpl.render()
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def submitForm(self, nom, prenom):
        """
        Soumet la réservation pour un concert.

        Paramètres :
        - nom : nom de la personne réservant
        - prenom : prénom de la personne réservant

        Fonctionnement :
        - Ajoute la réservation dans la base de données.
        - Affiche la confirmation de réservation à l'aide du template `confirmation.html`.
        """
        n, p, nc = sql.reserver(self.idrese, nom, prenom)
        tmpl = self.lookup.get_template("confirmation.html")
        return tmpl.render(nom=n, prenom=p, concert=nc)
    
    @cherrypy.expose
    def rese(self):
        """
        Affiche toutes les réservations.

        Fonctionnement :
        - Récupère toutes les réservations depuis la base de données.
        - Affiche les réservations à l'aide du template `showrese.html`.
        """
        tmpl = self.lookup.get_template("showrese.html")
        return tmpl.render(rese=sql.showrese())
    
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def insertIntoTable(self, table=None):
        """
        Page de formulaire d'insertion pour une table spécifique.

        Paramètre :
        - table : nom de la table

        Fonctionnement :
        - Récupère les en-têtes de la table depuis la base de données.
        - Détermine les clés primaires et étrangères.
        - Affiche le formulaire d'insertion à l'aide du template `insertIntoTable.html`.
        """
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
        """
        Insère une nouvelle entrée dans une table spécifique.

        Paramètre :
        - table : nom de la table
        - data : dictionnaire contenant les valeurs des colonnes

        Fonctionnement :
        - Convertit les données en liste.
        - Ajoute l'entrée dans la base de données.
        - Redirige vers la page d'accueil.
        """
        donnee = dict_to_list(data)
        sql.add_valeur(table, donnee)
        raise cherrypy.HTTPRedirect(f"/index")

##########################################################
###                     MAIN                           ###
##########################################################

if __name__ == "__main__":
    address, port, user, mdp, database, chem = lireconf()
    port = int(port)
    sql = bdd.bdd(address, user, mdp, port, chem)
    cherrypy.quickstart(SymphonicaSonata(), config="config.txt")

# Pour lancer le serveur, il suffit de lancer ce fichier.
