class Etudiant(object):
    
    
    def __init__(self,nom):
        self.nom=nom
         
    def calc_moyenne(self):
        n=int(input("le nombre de notes! "))
        som=0
        for i in range(n):
            a=float(input(f"NOTE n¤{i+1}: "))
            som=som+a
        m=som/n
        return m
    
    def affichage(self):
        print(f"NOM: {self.nom}\nMOYENNE: {self.calc_moyenne()}")

a=Etudiant("kokodoko")
a.calc_moyenne()
print("---------------------------------")
a.affichage()