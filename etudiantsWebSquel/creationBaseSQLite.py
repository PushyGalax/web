import sqlite3,os
reqCreat = """
CREATE TABLE IF NOT EXISTS etudiant (
    numEtudiant integer primary key autoincrement,
    prenom NOT NULL,
    nom  NOT NULL,
    dateNaissance TEXT NOT NULL default '2000-01-01') ;
"""
reqInsert = ["INSERT INTO `etudiant` VALUES (NULL, 'christian','DUCCINI','1900-01-01');",\
"INSERT INTO etudiant VALUES (NULL, 'toto','MARCEL','1981-04-27');",\
"INSERT INTO `etudiant` VALUES (NULL, 'paul','ISSON','1982-09-09');",\
"INSERT INTO `etudiant` VALUES (NULL, 'mic','ROSOFT','1980-05-05');",\
"INSERT INTO `etudiant` VALUES (NULL, 'mat','HEMATIC','1979-12-10');",\
"INSERT INTO `etudiant` VALUES (NULL, 'vincent','MILANES','1980-03-13');",\
"INSERT INTO `etudiant` VALUES (NULL, 'paula','RITE','1981-09-15');",\
"INSERT INTO `etudiant` VALUES (NULL, 'nin','DEJARDIN','1981-05-04');",\
"INSERT INTO `etudiant` VALUES (NULL, 'jonathan','LETRAIN','1981-06-23');",\
"INSERT INTO `etudiant` VALUES (NULL, 'lauriane','DUCCINI','2002-08-10');"]

print("Pour info, dans le répertoire courant : \n",os.listdir("."))
choix = input("Nom du fichier contenant la base à créer, '' pour valeur par défaut : ")
if choix == '' :
    fich = "etudiants.sqlite"
else :
    fich = choix.strip()
db= sqlite3.connect(fich)
cursor=db.cursor()
cursor.execute(reqCreat)
for req in reqInsert :
    cursor.execute(req)
cursor.close()
db.commit()
db.close()
q=input("Une touche pour finir")
