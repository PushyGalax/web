##########################################################
###                     README                         ###
##########################################################

Bienvenue dans l'application Symphonica Sonata !

Cette application permet de gérer et d'afficher des concerts de musique classique. Suivez les étapes ci-dessous pour configurer et lancer l'application.


##########################################################
###                 PRÉREQUIS                          ###
##########################################################

- Python 3.x
- Un serveur LAMP, WAMP ou MAMP configuré
- Les modules Python suivants :
  - cherrypy
  - mako
  - pymysql


##########################################################
###                 CONFIGURATION                      ###
##########################################################

1. Configuration du serveur de base de données

   Ouvrez le fichier `config.conf` et mettez à jour les paramètres de connexion à votre serveur de base de données LAMP, WAMP ou MAMP. Le format du fichier `config.conf` est précisé dedans


2. Configuration de l'hébergement

    Ouvrez le fichier `config.txt` et mettez à jour les paramètres de votre hébergement. Par défaut, les paramètres sont configurés pour localhost sur le port 8080


##########################################################
###            CRÉATION DE LA BASE DE DONNÉES          ###
##########################################################

Avant de lancer l'application web, vous devez créer la base de données. Pour ce faire, suivez les étapes ci-dessous :

1. Assurez-vous que votre serveur de base de données est en cours d'exécution.
2. Lancez le fichier `createbase.py` pour créer la base de données et les tables nécessaires avec les données



##########################################################
###              LANCEMENT DE L'APPLICATION            ###
##########################################################

Après avoir créé la base de données, vous pouvez lancer l'application web. Suivez les étapes ci-dessous :

1. Assurez-vous que votre serveur de base de données est en cours d'exécution.
2. Lancez le fichier `interfaceweb.py` pour démarrer le site web 



L'archive est de cette forme :

├── bdd.py                                              Fichier communiquant avec la BDD
├── config.conf                                         Configuration bdd
├── config.txt                                          Configuration site
├── createbase.py                                       Creation base
├── interfaceweb.py                                     Interface web
├── readme.txt                                          Readme
├── requete.py                                          Requete sql
├── csv                                                 Csv donnée de la base
│   ├── batimentsalle.csv
│   ├── compositeur.csv
│   ├── concert.csv
│   ├── jouer.csv
│   └── morceau.csv
└── template                                            Template html
    ├── assets                                          Image
    │   ├── bannière_symphonica.webp
    │   └── scan.png
    ├── css                                             Style
    │   ├── bootstrap.min.css
    │   ├── bootstrap.min.css.map
    │   └── style.css    
    ├── js                                              Javascript
    │   ├── bootstrap.min.js
    │   ├── bootstrap.min.js.map
    │   └── jquery-3.5.0.min.js    
    ├── affParCompositeur.html                          Selection par compositeurs
    ├── affParDate.html                                 Selection par date
    ├── affParGenre.html                                Selection par genre
    ├── affParMorceau.html                              Selection par morceau
    ├── concertDetails.html                             Detail carte concert
    ├── confirmation.html                               Confirmation et billet d'entrée
    ├── deleteTable.html                                Selection table à supprimer
    ├── index.html                                      Accueil du site
    ├── insertIntoTable.html                            Insertion de données
    ├── Recherche.html                                  Affichage des concerts par critère
    ├── reserver.html                                   Reservation de concert
    ├── seltable.html                                   Selection de table
    ├── seltableInsert.html                             Selection de table pour insertion
    ├── selTableMaj.html                                Selection de table pour mise à jour
    ├── showrese.html                                   Affichage des reservations
    ├── showTableData.html                              Affichage des données de la table pour la mise à jour
    ├── template.html                                   Nav bar est template de toutes les pages
    ├── updateform.html                                 Formulaire de mise à jour
    └── updateTable.html                                Mise à jour de la données
    