#####################################################
###                   IMPORTS                    ####
#####################################################
import pymysql
import requete
import csv
import datetime

#####################################################
###                   CLASSE                     ####
#####################################################

class bdd:
    def __init__(self, address, login, mdp, port, chemin_csv='./csv') -> None:
        """
        Initialise la connexion à la base de données.

        Paramètres :
        - address : adresse du serveur de la base de données
        - login : nom d'utilisateur pour la base de données
        - mdp : mot de passe pour la base de données
        - port : port de connexion au serveur de la base de données
        - chemin_csv : chemin vers le dossier contenant les fichiers CSV pour l'importation des données
        """
        self.bd = pymysql.connect(host=address, port=port, user=login, password=mdp)
        self.curs = self.bd.cursor()
        self.chemin_csv = chemin_csv
        self.curs.execute("USE sae_23")
    
    def info_index(self):
        """
        Récupère les informations sur les trois prochains concerts triés par date.

        Fonctionnement :
        - Exécute une requête pour obtenir le nom du concert, la date du concert et le nom de la salle.
        - Filtre les concerts à venir et en sélectionne jusqu'à trois.
        - Retourne une liste de tuples contenant les informations des concerts triés par date.
        """
        self.curs.execute(requete.select_join.format("nom_concert, date_concert, nom_salle", "concert", "salle", "concert.id_salle", "salle.id_salle", "1", "1") + " ORDER BY date_concert")
        valeur = self.curs.fetchall()
        dat = datetime.datetime.now().date()
        conc = []
        cpt = 0
        for elem in valeur:
            if cpt == 3:
                break
            if elem[1] > dat:
                conc.append(elem)
                cpt += 1
        conc = sorted(conc, key=lambda x: x[1])
        return conc

    def return_all_comp(self):
        """
        Récupère tous les noms de compositeurs.

        Fonctionnement :
        - Exécute une requête pour obtenir tous les noms de compositeurs.
        - Retourne une liste contenant les noms des compositeurs.
        """
        self.curs.execute(requete.select_key.format("nom_compositeur", "compositeur"))
        lis = []
        for elem in self.curs.fetchall():
            lis.append(elem[0])
        return lis
    
    def return_all_morc(self):
        """
        Récupère tous les noms de morceaux.

        Fonctionnement :
        - Exécute une requête pour obtenir tous les noms de morceaux.
        - Retourne une liste contenant les noms des morceaux.
        """
        self.curs.execute(requete.select_key.format("nom_morceau", "morceau"))
        lis = []
        for elem in self.curs.fetchall():
            lis.append(elem[0])
        return lis
    
    def return_all_genre(self):
        """
        Retourne une liste de genres musicaux prédéfinis.

        Fonctionnement :
        - Retourne une liste de genres musicaux sous forme de chaînes de caractères.
        """
        lis = ['symphonique', 'vent', 'corde', 'duo', 'trio', 'quatuor', 'soliste', 'rock', 'électro', 'traditionnelle', 'spéciale']
        return lis

    def get_concerts_by_composer(self, comp):
        """
        Récupère les concerts par compositeur.

        Paramètre :
        - comp : nom du compositeur

        Fonctionnement :
        - Exécute une requête pour obtenir les concerts associés à un compositeur donné.
        - Retourne une liste de tuples contenant les informations des concerts.
        """
        self.curs.execute(requete.select_triple_join.format("nom_concert, date_concert, id_salle, concert.id_concert, genre_concert", "concert", "jouer", "concert.id_concert", "jouer.id_concert", "morceau", "morceau.id_morceau", "jouer.id_morceau", "compositeur", "morceau.id_compositeur", "compositeur.id_compositeur", "nom_compositeur", f"'{comp}'"))
        lis = []
        for elem in self.curs.fetchall():
            self.curs.execute(requete.select_join.format("adresse, ville, code_postale", "batiment", "salle", "salle.id_batiment", "batiment.id_batiment", "id_salle", f"'{elem[2]}'"))
            info = self.curs.fetchall()
            lis.append((elem[0], elem[1], str(info[0]), elem[3], elem[4]))
        return lis
    
    def get_concerts_by_morceau(self, morc):
        """
        Récupère les concerts par morceau.

        Paramètre :
        - morc : nom du morceau

        Fonctionnement :
        - Exécute une requête pour obtenir les concerts associés à un morceau donné.
        - Retourne une liste de tuples contenant les informations des concerts.
        """
        self.curs.execute(requete.select_double_join.format("nom_concert, date_concert, id_salle, concert.id_concert, genre_concert", "concert", "jouer", "concert.id_concert", "jouer.id_concert", "morceau", "morceau.id_morceau", "jouer.id_morceau", "nom_morceau", f"'{morc}'"))
        lis = []
        for elem in self.curs.fetchall():
            self.curs.execute(requete.select_join.format("adresse, ville, code_postale", "batiment", "salle", "salle.id_batiment", "batiment.id_batiment", "id_salle", f"'{elem[2]}'"))
            info = self.curs.fetchall()
            lis.append((elem[0], elem[1], str(info[0]), elem[3], elem[4]))
        return lis
    
    def get_concerts_by_genre(self, genre):
        """
        Récupère les concerts par genre musical.

        Paramètre :
        - genre : genre musical

        Fonctionnement :
        - Exécute une requête pour obtenir les concerts associés à un genre musical donné.
        - Retourne une liste de tuples contenant les informations des concerts.
        """
        self.curs.execute(requete.select_with_where.format("nom_concert, date_concert, id_salle, concert.id_concert, genre_concert", "concert", "genre_concert", f"'{genre}'"))
        lis = []
        for elem in self.curs.fetchall():
            self.curs.execute(requete.select_join.format("adresse, ville, code_postale", "batiment", "salle", "salle.id_batiment", "batiment.id_batiment", "id_salle", f"'{elem[2]}'"))
            info = self.curs.fetchall()
            lis.append((elem[0], elem[1], str(info[0]), elem[3], elem[4]))
        return lis
    
    def get_concerts_by_date(self, date):
        """
        Récupère les concerts par date.

        Paramètre :
        - date : date du concert

        Fonctionnement :
        - Exécute une requête pour obtenir les concerts ayant lieu à une date donnée.
        - Retourne une liste de tuples contenant les informations des concerts.
        """
        self.curs.execute(requete.select_with_where_supp.format("nom_concert, date_concert, id_salle, concert.id_concert, genre_concert", "concert", "date_concert", f"'{date}'"))
        lis = []
        for elem in self.curs.fetchall():
            self.curs.execute(requete.select_join.format("adresse, ville, code_postale", "batiment", "salle", "salle.id_batiment", "batiment.id_batiment", "id_salle", f"'{elem[2]}'"))
            info = self.curs.fetchall()
            lis.append((elem[0], elem[1], str(info[0]), elem[3], elem[4]))
        return lis
    
    def delete_entry(self, table, id_):
        """
        Supprime une entrée dans une table spécifique.

        Paramètres :
        - table : nom de la table
        - id_ : identifiant de l'entrée à supprimer
        """
        self.curs.execute(requete.deletedata.format(table, f"id_{table}", f"'{id_}'"))
        self.bd.commit()
    
    def get_table_content(self, table):
        """
        Récupère le contenu complet d'une table spécifique.

        Paramètre :
        - table : nom de la table

        Fonctionnement :
        - Exécute une requête pour obtenir toutes les entrées de la table spécifiée.
        - Récupère et retourne les en-têtes de colonnes et le contenu de la table.
        """
        query = f"SELECT * FROM {table}"
        self.curs.execute(query)
        content = self.curs.fetchall()
        
        self.curs.execute(f"SHOW COLUMNS FROM {table}")
        headers = [column[0] for column in self.curs.fetchall()]

        return headers, content
    
    def get_entry_by_id(self, table, entry_id):
        """
        Récupère une entrée spécifique par son identifiant.

        Paramètres :
        - table : nom de la table
        - entry_id : identifiant de l'entrée

        Fonctionnement :
        - Exécute une requête pour obtenir une entrée spécifique de la table.
        - Retourne un dictionnaire contenant les colonnes et leurs valeurs.
        """
        self.curs.execute(f"SELECT * FROM {table} WHERE id_{table} = {entry_id}")
        result = self.curs.fetchone()
        return dict(zip([desc[0] for desc in self.curs.description], result))
    
    def update_entry(self, table, entry_id, data):
        """
        Met à jour une entrée spécifique dans une table.

        Paramètres :
        - table : nom de la table
        - entry_id : identifiant de l'entrée à mettre à jour
        - data : dictionnaire contenant les colonnes et leurs nouvelles valeurs

        Fonctionnement :
        - Construit et exécute une requête de mise à jour (UPDATE) pour la table et l'entrée spécifiées.
        """
        columns = ', '.join(f"{key} = %s" for key in data)
        values = list(data.values())
        values.append(entry_id)
        query = f"UPDATE {table} SET {columns} WHERE id = %s"
        self.curs.execute(query, values)
        self.conn.commit()
    
    def get_foreign_key_options(self, foreign_table):
        """
        Récupère les options de clés étrangères pour une table spécifique.

        Paramètre :
        - foreign_table : nom de la table étrangère

        Fonctionnement :
        - Exécute une requête pour obtenir les identifiants et noms des entrées de la table étrangère.
        - Retourne une liste de dictionnaires contenant les valeurs des clés étrangères et leurs affichages.
        """
        query = f"SELECT id_{foreign_table}, nom_{foreign_table} FROM {foreign_table}"
        self.curs.execute(query)
        return [{"value": row[0], "display": row[1]} for row in self.curs.fetchall()]
    
    def get_concert_details(self, id_):
        """
        Récupère les détails d'un concert spécifique.

        Paramètre :
        - id_ : identifiant du concert

        Fonctionnement :
        - Exécute une requête pour obtenir les détails d'un concert par son identifiant.
        - Retourne une liste de tuples contenant les informations détaillées du concert.
        """
        self.curs.execute(requete.select_with_where.format("date_concert, formation, chef_d_orchestre, soliste, prix_place, genre_concert, durée_concert, id_salle, nom_concert, nb_place_restante, id_concert", "concert", "id_concert", f"'{id_}'"))
        lis = []
        for elem in self.curs.fetchall():
            self.curs.execute(requete.select_join.format("adresse, ville, code_postale", "batiment", "salle", "salle.id_batiment", "batiment.id_batiment", "id_salle", f"'{elem[7]}'"))
            info = self.curs.fetchall()
            lis.append((elem[0], str(info[0]), elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[8], elem[9], elem[10]))
        return lis
    
    def reserver(self, id_, nom, prenom):
        """
        Réserve une place pour un concert.

        Paramètres :
        - id_ : identifiant du concert
        - nom : nom de la personne réservant
        - prenom : prénom de la personne réservant

        Fonctionnement :
        - Insère une nouvelle réservation dans la table des réservations.
        - Met à jour le nombre de places restantes pour le concert.
        - Retourne les informations de réservation.
        """
        self.curs.execute(requete.request_ajout.format("reservation", requete.valeur["reservation"], f"NULL, '{id_}', '{nom}', '{prenom}'"))
        self.curs.execute(requete.select_with_where.format("nb_place_restante", "concert", "id_concert", f"'{id_}'"))
        nb_place = self.curs.fetchall()[0][0]
        self.curs.execute(requete.update.format("concert", "nb_place_restante", f"'{nb_place-1}'", "id_concert", f"'{id_}'"))
        self.bd.commit()
        self.curs.execute(requete.select_with_where.format("nom_concert", "concert", "id_concert", f"'{id_}'"))
        return nom, prenom, self.curs.fetchall()[0][0]
    
    def showrese(self):
        """
        Affiche toutes les réservations triées par nom de concert.

        Fonctionnement :
        - Exécute une requête pour obtenir toutes les réservations triées par nom de concert.
        - Retourne une liste de tuples contenant les informations des réservations.
        """
        self.curs.execute(requete.select_join.format("nom_reservation, prenom_reservation, nom_concert", "reservation", "concert", "reservation.id_concert", "concert.id_concert", "1", "1") + " ORDER BY nom_concert")
        lis = []
        for elem in self.curs.fetchall():
            lis.append((elem[0], elem[1], elem[2]))
        return lis
    
    def get_concert_prg(self, id_):
        """
        Récupère le programme d'un concert spécifique.

        Paramètre :
        - id_ : identifiant du concert

        Fonctionnement :
        - Exécute une requête pour obtenir les morceaux joués lors d'un concert.
        - Retourne une liste de morceaux.
        """
        self.curs.execute(requete.select_double_join.format("nom_morceau", "morceau", "jouer", "morceau.id_morceau", "jouer.id_morceau", "concert", "concert.id_concert", "jouer.id_concert", "concert.id_concert", f"'{id_}'"))
        lis = []
        for elem in self.curs.fetchall():
            lis.append(elem[0])
        return lis

    def update(self, table, cle, valeur, id):
        """
        Met à jour une valeur spécifique dans une table donnée.

        Fonctionnement :
        - Exécute une requête UPDATE pour modifier la valeur d'une colonne spécifiée (`cle`)
        dans une table spécifique (`table`) pour une entrée spécifiée par son identifiant (`id`).
        """
        self.curs.execute(requete.update.format(table, cle, f"'{valeur}'" if valeur != "NULL" else "NULL", f"id_{table}", f"'{id}'"))
        self.bd.commit()
    
    def add_valeur(self, table, *args):
        """
        Ajoute une nouvelle entrée (ligne) dans une table spécifiée avec les valeurs fournies.

        Fonctionnement :
        - Génère et exécute une requête INSERT INTO pour ajouter une nouvelle entrée dans une table (`table`)
        avec les valeurs spécifiées (`args`).
        """
        lis = args[0]
        if table not in ["jouer", "reservation"]:
            val = "NULL,"
            for elem in range(len(lis)):
                if lis[elem][-1] == "µ":
                    val += f"{lis[elem][:-1]},"
                else:
                    val += f"'{lis[elem]}',"
        else:
            val = ""
            for elem in range(len(lis)):
                if lis[elem][-1] == "µ":
                    val += f"{lis[elem][:-1]},"
                else:
                    val += f"'{lis[elem]}',"
        
        self.curs.execute(requete.request_ajout.format(table, requete.valeur[table], val[:-1]))
        self.bd.commit()
