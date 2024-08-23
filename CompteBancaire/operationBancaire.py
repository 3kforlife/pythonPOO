from compteBancaire import *

a=input("votre numero de compte! ")
b=input("votre nom! ")
c=int(input("votre solde! "))
cpte=CompteBancaire(a,b,c)
while True:
    print("VEUILLEZ CHOISIR UNE OPTION\n-----------------------")
    print("1-DEPOT\n2-RETRAIT\n3-AFFICHAGE DU COMPTE\n4-QUITTER")
    choix=int(input("votre choix! "))
    match(choix):
        case 1:
            arg=int(input("entrer le montant à déposer! "))
            cpte.versement(arg)
            print("\n")
        case 2:
            arg=int(input("entrer le montant à retirer! "))
            cpte.retrait(arg)
            print("\n")

        case 3:
            cpte.affichage()
            print("\n")

        case 4:
            break
        case _:
            print("Soyez sérieux")
            print("\n")



        

            