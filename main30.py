def saisir():
    n = int(input("n : "))
    if 1<= n <=40:
        return n
    print("The value of n must be between 2 and 40!")

def date():
    date = dict()
    while True:
        day = int(input("day :"))
        if 1<= day <=31:
            date["day"] = day
        else:
            print("the jour must be in 1 and 31!")
            continue
        month = int(input("month : "))
        if 1<=month<=12:
            date["month"] = month
        else:
            print("the mois must be in 1 and 12!")
            continue
        year = int(input("year : "))
        if 999< year <9999:
            date["year"] = year
        else :
            print("The annee must contain 4 digits!")
            continue
        break
    return date
    
def ajouter(n):
        listes = []
        for i in range(n):
            e = dict()
            while True:
                e["NInscription"] = i + 1
                NP = input("Nom & Prenom : ")
                if "  " not in NP and NP.count(" ") == 1:
                    e["N et P"] = NP
                else:
                    print("Entre 1 espace between Nom et Prenom!")
                    continue
                e["date"] = date()
                moy = float(input("Moyenne : "))
                try:
                    if 0.0<= moy <=20.00:
                        e["Moyenne"] = moy
                    else:
                        print("The Moyenne must be between 0.0 and 20.0!")
                        continue
                except ValueError:
                    print("Please enter a valid number for Moyenne!")
                    continue
                
                print("Registration Success!")
                print(" "*50)
                listes.append(e)
                break
        return listes
 
def tri(listes):
    for i in range (len(listes)):
        for j in range (i+1,len(listes)):
            if listes[i]["Moyenne"] < listes[j]["Moyenne"]:
                (listes[i] , listes[j]) = (listes[j],listes[i])
    return listes

def remplir(listes):
    f = open("liste.txt" , "a")
    for list in listes:
        f.write(str(list) +"\n")
    f.close()

def afficher():
    f = open("liste.txt" , "r")
    reads = f.read()
    print(reads)
    f.close()

def maxx(listes):
    print("Students with Moyenne >= 10:")
    for i in range(len(listes)):
        if listes[i]["Moyenne"] >= 10:
            print(listes[i])
    return listes

def minx(listes):
    print("Students with Moyenne <= 10:")
    for i in range (len(listes)):
        if  listes[i]["Moyenne"] <= 10:
            print(listes[i])
    return listes

n=saisir()
listes = ajouter(n)
listes_triees = tri(listes)
remplir(listes)
afficher()
maxx(listes_triees)
minx(listes_triees)