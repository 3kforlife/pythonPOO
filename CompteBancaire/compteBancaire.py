class CompteBancaire(object):
    def __init__(self,numeroCompte,nom,solde=0):
        self.numeroCompte=numeroCompte
        self.nom=nom
        self.solde=solde

    def versement(self,somme):
        self.solde+=somme
    
    def retrait(self,somme):
        if(self.solde<somme):
            print("solde insuffisant.Impossible d'effectuer l'opération")
        else:
            self.solde-=somme
    
    def agios(self):
        self.solde*=95/100

    def affichage(self):
        print(f"Numero de compte: {self.numeroCompte}\nNom du propriétaire: {self.nom}\nSolde: {self.solde} Francs CFA")
