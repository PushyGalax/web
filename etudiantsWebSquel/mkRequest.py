# les fonctions suivantes permettent de créer des requêtes "SQL" avec des valeurs variables

_requetes = {
    "drop" : "DROP DATABASE IF EXISTS etudiants",
    "createBase" : "CREATE DATABASE IF NOT EXISTS etudiants DEFAULT CHARACTER SET utf8",
    "use" : "USE etudiants",
    "createTable" : "CREATE TABLE etudiant ( numEtudiant INTEGER PRIMARY KEY AUTO_INCREMENT,\
        prenom VARCHAR(30) NOT NULL,\
        nom VARCHAR(30) NOT NULL,\
        dateNaissance DATE NOT NULL default '2023-01-01') ; ",
    "insertEtudiants" : "INSERT INTO etudiant (prenom,nom,dateNaissance) VALUES ('christian','DUCCINI','1900-01-01'),\
        ('toto','MARCEL','1981-04-27'),('paul','ISSON','1982-09-09'),('mic','ROSOFT','1980-05-05'),\
        ('mat','HEMATIC','1979-12-10'),('vincent','MILANES','1980-03-13'),('paula','RITE','1981-09-15'),\
        ('nin','DEJARDIN','1981-05-04'),('jonathan','LETRAIN','1981-06-23'),('lauriane','DUCCINI','2002-08-10');",
    "reset" : "truncate table etudiant;",
    "getAll" : "select * from etudiant order by nom, prenom;",
    "getAllParAge" : "select * from etudiant order by dateNaissance desc;",
    "getById" : "select * from etudiant where numEtudiant = {};",
    "getByNom" : "select * from etudiant where nom = '{}' and prenom = '{}';",
    "insert" : "insert into etudiant (prenom,nom,dateNaissance) values ('{}','{}','{}');",
    "delete" : "delete from etudiant where nom = '{}' and prenom = '{}';" ,
    "deleteByNum" : "delete from etudiant where numEtudiant = {};" }

def mkInsertRequest(prenom, nom, anniversaire) :
    s= _requetes["insert"].format(prenom.capitalize(),nom.upper(),anniversaire)
    return s
    
def mkDeleteRequest(prenom,nom) :
    s= _requetes["delete"].format(nom.upper(),prenom.capitalize())
    return s

def mkDeleteByNumRequest(num) :
    s= _requetes["deleteByNum"].format(num)
    return s

def mkGetByNumRequest(num) :
    s= _requetes["getById"].format(num)
    return s

def mkGetByNomRequest(prenom,nom) :
    s= _requetes["getByNom"].format(nom.upper(),prenom.capitalize())
    return s
        
