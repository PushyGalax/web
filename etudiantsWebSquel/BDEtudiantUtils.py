from mkRequest import _requetes, mkInsertRequest, mkDeleteRequest, mkDeleteByNumRequest, mkGetByNumRequest, mkGetByNomRequest

_dbConfig = {
        'driver' : "MySQL",
        'db' : 'etudiants',
        'host' : "localhost",
        'user' : "root",
        'passwd' : "",
        'port' : 3306     # port MySQL standard (par défaut)
    }

def majParamsConnexion() -> None:
    # actuellement, ne gère que sqlite et MYSQL
    # récup des paramètres dans le fichier de conf
    # paramètres MYSQL, valeurs par défaut
    # attention, le port sera alors stocké comme une chaîne !
    try :
        with open("config.txt") as f :
            for ligne in f :
                if ligne[0] == '#' or ligne[0] == '[' or len(ligne)<3 :
                    continue
                champs = ligne.split(':')
                _dbConfig[champs[0].strip()] = champs[1].strip().strip('"')
        print(_dbConfig)
    except FileNotFoundError as e :
        print("'config.txt' absent, utilisation des valeurs par défaut")
        
def dbConnect():
    # récup des paramètres dans le fichier de conf
    match _dbConfig['driver'].upper() :
        case "MYSQL" :
            import pymysql
            db = pymysql.connect(host = _dbConfig['host'], user=_dbConfig['user'], passwd=_dbConfig['passwd'], port=int(_dbConfig['port']), db = _dbConfig['db'])
        case "SQLITE" :
            import os,sqlite3
            nomFich = _dbConfig['db']+".sqlite"
            db = sqlite3.connect(nomFich)
        case _ :
            raise ValueError
    cursor=db.cursor()
    return (db,db.cursor())

##  La collection est stockee dans une base de donnée, dont le format est fixé :
##  Pas de tentative de rendre le code générique, pour éviter de donner un corrigé trop complexe.
## 
##  Néanmoins le maximum a été encapsulé dans des parties spécifiques pour faciliter
##  les modifications éventuelles.
##
##  La connection est effectuée à chaque fois...:-(
def createBaseMYSQL() -> None :
    import pymysql
    db = pymysql.connect(host = _dbConfig['host'], user=_dbConfig['user'], passwd=_dbConfig['passwd'], port=int(_dbConfig['port']))
    cursor = db.cursor()
    cursor.execute(_requetes["drop"])
    cursor.execute(_requetes["createBase"])
    cursor.execute(_requetes["use"])
    cursor.execute(_requetes["createTable"])
    cursor.execute(_requetes["insertEtudiants"])

def createBaseSQLITE(nomFich: str) -> None :
    import os,sqlite3
    if os.path.isfile(nomFich) :
        os.remove(nomFich)
    db = sqlite3.connect(nomFich)
    cursor=db.cursor()
    cursor.execute("""CREATE TABLE etudiant ( numEtudiant integer primary key autoincrement, prenom NOT NULL, nom  NOT NULL, dateNaissance NOT NULL default '2000-01-01') ;""")
    cursor.execute(_requetes["insertEtudiants"])
    db.commit()
    db.close()

def initBase() -> None :
    """ Vérifie que la base existe, sinon propose de la créer en mode CLI.
            Jette une exception si paramètres de connexion incorrects """
    majParamsConnexion()     
    match _dbConfig['driver'].upper() :
        case "MYSQL" :
            try :
                import pymysql
                db = pymysql.connect(host=_dbConfig['host'], user=_dbConfig['user'], passwd=_dbConfig['passwd'], port=int(_dbConfig['port']), db =_dbConfig['db'] )
                cursor = db.cursor()
                cursor.execute(_requetes["getAll"])
            except pymysql.err.OperationalError as e:
                print(e)
                if '1044' in str(e) :
                    print (f"Vérifiez les paramètres de connexion à la base {_dbConfig['db']}")
                    raise e
                elif '1049' in str(e) :
                    choix = input("base inexistante, voulez-vouz créer une base 'etudiants' standard? (o/n) :")
                    if choix.upper() in ['O','OUI','Y' 'YES'] :
                         createBaseMySQL()
                    else :
                        raise e
        case "SQLITE" :
            import os,sqlite3
            nomFich = _dbConfig['db']+".sqlite"
            if not os.path.isfile(nomFich) :
                choix = input(f"la base {nomFich} n'existe pas, voulez-vous la créer (O pour oui) ?  : ")
                if choix.upper() in ['O','OUI','Y' 'YES'] :
                    createBaseSQLITE(nomFich)
            else :
                try :
                    db = sqlite3.connect(nomFich)
                    cursor = db.cursor()
                    cursor.execute(_requetes["getAll"])
                except sqlite3.OperationalError as e :
                    choix = input(f"le fichier {nomFich} existe, mais ne contient pas de base, voulez-vous le supprimer (O pour oui) ?  : ")
                    if choix.upper() in ['O','OUI','Y' 'YES'] :
                        createBaseSQLITE(nomFich)
                    else :
                        raise e                  
        case _ :
            print (f"SGBDR {_dbConfig['driver'].upper()} non géré")
            raise ValueError                
    
# la fonction suivante permettent de convertir une date du format ISO (format stocké dans la base SQLite par ex)
#    au format python "date"
def isoStr2Date(date : str ) -> object :
    """ fonction de conversion d'une date-chaîne du format ISO (yyyy-mm-jj) pour avoir un objet "Date"             
    """
    import datetime
    d = date.split('-')
    return datetime.date(int(d[0]), int(d[1]), int(d[2]))

# la fonction suivante permettent de normaliser un tuple obtenir à partir d'un date de donnée pour s'assurer
# que la date est bien au format "date" python
def normalizeEtudiant(t : tuple) -> tuple :
    import datetime
    if isinstance(t[3],datetime.date) :
        if _dbConfig['driver'].upper() != "MYSQL" :
            raise ValueError
        tNorm = t
    else :
        if _dbConfig['driver'].upper() != "SQLITE" :
            raise ValueError
        tNorm = (t[0],t[1],t[2],isoStr2Date(t[3]))
    return tNorm

# les 2 fonctions suivantes permettent de convertir des dates du format ISO (format stocké dans la base)
#    au format "habituel" (jj/mm/aaaa) pour affichage, ou pour écriture dans les fichiers texte
def isoDate2String(date : str ) -> str :
    """ fonction de conversion d'une date-chaîne au format ISO (yyyy-mm-jj)
            au format "habituel" (jj/mm/aaaa) 
    """
    d = date.split('-')
    s= d[2]+"/"+ d[1]+"/"+d[0]
    return s
    
def date2ISO(date : str ) -> str :
    """ fonction de conversion d'une date-chaîne au format "habituel" (jj/mm/aaaa)
            au format  ISO (yyyy-mm-jj)
    """
    d = date.split('/')
    s = d[2]+"-"+ d[1]+"-"+d[0]
    return s

# La routine suivante encapsule une bonne partie des accès à la base de donnée.
# Pour les requêtes de type "select", elle rend la liste des résultats (liste de tuples) obtenus
#   par un "fetchall", sinon, elle rend le résultat de la requête !
def execute(req : str) :    # type de valeur rendu variable :-(
    _dbEtudiant, _cursorEtudiant = dbConnect()
    res = _cursorEtudiant.execute(req)
    if "select" in req :
        res = _cursorEtudiant.fetchall()
    else :
        _dbEtudiant.commit()
    return res

# La routine suivante n'est utilisée que pour débug (menu "exécuter requête SQL"!)
def executeReq(req : str) -> tuple :
    _dbEtudiant, _cursorEtudiant = dbConnect()
    cr = _cursorEtudiant.execute(req)
    res = _cursorEtudiant.fetchall()
    _dbEtudiant.commit()
    return cr,res

def getEtudiants() -> list :
    """ getEtudiants() -> liste de tuples "Etudiant"
    Rend le contenu de la base sous forme d'une liste de tuples.
    Attention, la "dateNaissance" (4°élément) est un objet "datetime.date" python!!! """
    req = _requetes["getAll"]
    etudiants = []
    for t in execute(req) :
        etudiants.append(normalizeEtudiant(t))
    return etudiants

def getEtudiantsStr()-> list :
    """ getEtudiantsStr() -> liste de chaînes
    Rend le contenu de la base sous forme d'une liste de chaînes """
    etudiantsStr = []
    for etud in getEtudiants() :
        etudiantsStr.append(etudToString(etud))
    return etudiantsStr

# les fonctions suivantes opèrent sur les "etudiants"
# en attendant la prog "objet" objet "Etudiant" (et/ou un ORM),
#   un "étudiant" est considéré commu un "tuple" issu directement de la table "etudiant",
#   la date est au format "date" Python !
def etudToString(etud : tuple) -> str :
    """ Rend le tuple sous forme d'une chaîne de caractères """
    anniv = etud[3].strftime("%d/%m/%Y")
    return f"n°{etud[0]} : {etud[1]} {etud[2]} né(e) le {anniv}"

def etudToCSV(etud: tuple) -> str :
    """ Rend le tuple sous forme d'une chaîne de caractères, format csv"""
    anniv = etud[3].strftime("%d/%m/%Y")
    return f"{etud[0]};{etud[1]};{etud[2]};{anniv};"

# les fonctions suivantes opèrent sur la collection (idem, pas d'"objet")
def dbToString() -> str :
    """ Rend le contenu de la base sous forme d'une chaîne de caractères """
    s= ''
    for etud in getEtudiants():
        s = s + etudToString(etud) + "\n"
    return s

def dbToFile() -> str:
    """ Rend le contenu de la base sous forme d'une chaîne de caractères au format "csv"
    """
    s = ''
    for etud in getEtudiants() :
        s = s + etudToCSV(etud) + '\n'
    return s

def reset() -> None :
    """ Remise à zéro de la table """
    req = _requetes["reset"]
    execute(req)

def getParAge() -> list :
    """ Rend le contenu de la base sous forme d'une liste de tuples, rangés par ordre d'âge """
    req = _requetes["getAllParAge"]
    etuds = []
    for t in execute(req) :
        etuds.append(normalizeEtudiant(t))
    return etuds
        
def getPlusJeune() -> tuple :
    """ Rend une ou une des étudiant le ou la plus jeune """
    req = _requetes["getAllParAge"]
    return normalizeEtudiant(execute(req)[0])

def insertEtudiant(prenom : str, nom : str, dateNaissance : str) -> None :
    """ Insertion d'un étudiant dans la collection"""
    req = mkInsertRequest(prenom.capitalize(),nom.upper(),dateNaissance)
    execute(req)

def deleteEtudiant(prenom : str, nom : str) -> None :  
    """ Suppression d'un étudiant dans la collection
    On en supprime potentiellement plusieurs si le couple(prenom,nom) n'est pas unique!"""
    p = prenom.capitalize()
    n = nom.upper()
    reqVerif = mkGetByNomRequest(p, n)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkDeleteRequest(p, n)
    execute(req)

def deleteEtudiantByNum(num : int) -> None :
    """ Suppression d'un étudiant dans la collection"""
    reqVerif = mkGetByNumRequest(num)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkDeleteByNumRequest(num)
    execute(req)

def loadFromCSVFile(path : str) -> None:
    """ Permet de charger une liste d'"etudiant"s à partir d'un fichier texte "CSV" """
    import csv
    with open(path, newline='\n',encoding='utf-8') as csvFile :
        lignesEtud = csv.reader(csvFile,delimiter=';')
        for champs in lignesEtud :
            if len(champs) < 3 :
                print ("ligne incorrecte : <{}>, ignorée".format(champs))
                continue
            prenom = champs[0].capitalize()
            nom = champs[1].upper()
            date = date2ISO(champs[2])
            insertEtudiant(prenom,nom,date)

def saveToTextFile(path="etudiants.txt"):
    """ Permet d'exporter la table "etudiant" de la base dans un fichier texte "bien formatté" """
    with open(path,"w") as f :
        f.write(dbToFile())
        
if __name__ == '__main__':
    import os
    print(f"Fichiers dans le répertoire courant : {os.listdir()}")
    initBase()
    print (f"config utilisée : {_dbConfig['driver']}")
    print ("====== ")
    print (dbToString())
    input("Une touche pour finir")
        
