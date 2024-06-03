import pymysql
import requete
import csv

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

def start(address, login, mdp, port, chemin_csv='./csv') -> None:
    """
        Cette fonction va se connecter à la base de données
        est créer la base de données
    """

    bd = pymysql.connect(host=address, port=port, user=login, password=mdp)
    curs = bd.cursor()
    chemin_csv = chemin_csv

    taille=len(requete.creation)
    try:
        curs.execute(requete.creation[0])
    except pymysql.err.ProgrammingError:
        pass
    curs.execute("USE sae_23")

    for i in range(1,taille):
        try:
            curs.execute(requete.creation[i])
        except pymysql.err.ProgrammingError:
            continue
    bd.commit()

    with open(f"{chemin_csv}/batimentsalle.csv", 'r+') as file:
        read = csv.reader(file, delimiter=';')
        cpt=-1
        for elem in read:
            cpt+=1
            if cpt==0:
                continue
            else:
                val="NULL,'"+str(elem[0])+"','"+str(elem[1])+"','"+str(elem[2])+"','"+str(elem[3])+"'"
                curs.execute(requete.request_ajout.format("batiment",requete.valeur["batiment"],val))
                
                curs.execute(f"SELECT id_batiment FROM batiment WHERE adresse = '{elem[1]}'")
                id = curs.fetchall()
                # print(id[0][0])
                if len(elem) == 5:
                    salle=elem[4].split(',')
                    for sal in salle:
                        val="NULL,'"+str(id[0][0])+"','"+str(sal)+"'"
                        curs.execute(requete.request_ajout.format("salle",requete.valeur["salle"],val))
        bd.commit()
    
    with open(f"{chemin_csv}/compositeur.csv", 'r+') as file:
        read = csv.reader(file, delimiter=';')
        cpt=-1
        for elem in read:
            cpt+=1
            if cpt==0:
                continue
            else:
                datenai="NULL" if elem[1].strip() =="NULL" else f"'{elem[1].strip()}'"
                datemor="NULL" if elem[2].strip() =="NULL" else f"'{elem[2].strip()}'"
                nbmor="NULL" if elem[3].strip() =="NULL" else f"'{elem[3].strip()}'"
                val=f"NULL,'{elem[0]}',{datenai},{datemor},{nbmor}"
                # print(requete.request_ajout.format("compositeur",requete.valeur["compositeur"],val))
                curs.execute(requete.request_ajout.format("compositeur",requete.valeur["compositeur"],val))
        bd.commit()

    with open(f"{chemin_csv}/morceau.csv", 'r+') as file:
        read = csv.reader(file, delimiter=';')
        cpt=-1
        for elem in read:
            cpt+=1
            if cpt==0:
                continue
            else:
                # print(requete.select_with_where.format("id_compositeur","compositeur","nom_compositeur",elem[0]))
                curs.execute(requete.select_with_where.format("id_compositeur","compositeur","nom_compositeur",f"'{elem[0]}'"))
                id_comp=curs.fetchall()
                datecomp="NULL" if elem[2] =="NULL" else f"'{elem[2]}'"
                lieucomp="NULL" if elem[5] =="NULL" else f"'{elem[5]}'"
                val=f"NULL,'{id_comp[0][0]}','{elem[1]}',{datecomp},'{elem[3]}','{elem[4]}',{lieucomp}"
                # print(requete.request_ajout.format("morceau",requete.valeur["morceau"],val))
                curs.execute(requete.request_ajout.format("morceau",requete.valeur["morceau"],val))
        bd.commit()
    
    with open(f"{chemin_csv}/concert.csv", 'r+') as file:
        read = csv.reader(file, delimiter=';')
        cpt=-1
        for elem in read:
            cpt+=1
            if cpt==0:
                continue
            else:
                curs.execute(requete.select_with_where.format("id_salle","salle","nom_salle",f"'{elem[0]}'"))
                # print(requete.select_with_where.format("id_salle","salle","nom_salle",f"'{elem[0]}'"))
                id_salle=curs.fetchall()
                chef="NULL" if elem[5] =="NULL" else f"'{elem[5]}'"
                soliste="NULL" if elem[6] =="NULL" else f"'{elem[6]}'"
                prix="NULL" if elem[7] =="NULL" else f"'{elem[7]}'"
                val=f"NULL,'{id_salle[0][0]}','{elem[1]}','{elem[2]}','{elem[3]}','{elem[4]}',{chef},{soliste},{prix},'{elem[8]}','{elem[9]}','{elem[10]}'"
                # print(requete.request_ajout.format("concert",requete.valeur["concert"],val))
                curs.execute(requete.request_ajout.format("concert",requete.valeur["concert"],val))
        bd.commit()

    with open(f"{chemin_csv}/jouer.csv", 'r+') as file:
        read = csv.reader(file, delimiter=';')
        cpt=-1
        for elem in read:
            cpt+=1
            if cpt==0:
                continue
            else:
                curs.execute(requete.select_with_where.format("id_concert","concert","nom_concert",f"'{elem[0]}'"))
                id_concert=curs.fetchall()[0][0]
                curs.execute(requete.select_with_where.format("id_morceau","morceau","nom_morceau",f"'{elem[1]}'"))
                id_morceau=curs.fetchall()[0][0]
                val=f"'{id_concert}','{id_morceau}'"
                # print(requete.request_ajout.format("jouer",requete.valeur["jouer"],val))
                curs.execute(requete.request_ajout.format("jouer",requete.valeur["jouer"],val))
        bd.commit()


if __name__ == "__main__":
    address, port, user, mdp, database, chem = lireconf()
    port = int(port)
    print("Création de la base:")
    sql = start(address, user, mdp, port, chem)
    print("fin")