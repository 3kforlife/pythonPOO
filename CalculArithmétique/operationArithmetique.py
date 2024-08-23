from calculArithmetique import *
cal=Calcul()
while True:
    print("VEUILLEZ CHOISIR UNE OPTION\n-------------------------")
    print("1-Factorielle d'un entier\n2-Cumul d'un entier\n3-test de primalité d'un entier\n4-test de primalité de deux entiers\n5-table de multiplication\n6-liste des diviseurs d'un entier\n7-liste des diviseurs premiers d'un entier\n8-Quitter")
    choix=int(input("votre choix! "))
    match(choix):
        case 1:
            n=int(input("entrer un entier! "))
            print(f"factorielle de {n}: {cal.factorielle(n)}")
            print("\n")
        case 2:
            n=int(input("entrer un entier! "))
            print(f"cumul de {n}: {cal.cumul(n)}")
            print("\n")

        case 3:
            n=int(input("entrer un entier! "))
            t=cal.testPrimalite(n)
            if(t==True):
                print("c'est un nombre premier")
            else:
                print("ce n'est pas un nombre premier")
            print("\n")

        case 4:
            n=int(input("Premier entier! "))
            m=int(input("Deuxième entier! "))
            cal.testPrimalites(n,m)
            print("\n")
        case 5:
            n=int(input("entrer un entier! "))
            cal.tableMultiplication(n)
            print("\n")

        case 6:
            n=int(input("entrer un entier! "))
            print(f"la liste de diviseurs de cet entier est: {cal.diviseurs(n)}")
            print("\n")

        case 7:
            n=int(input("entrer un entier! "))
            print(f"la liste de diviseurs premiers de cet entier est: {cal.diviseursPremiers(n)}")
            print("\n")

        case 8:
            break
        case _:
            print("votre choix n'existe pas dans les options")
            print("\n")





