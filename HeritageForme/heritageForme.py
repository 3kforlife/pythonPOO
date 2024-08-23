class Forme(object):
    def __init__(self,l=0,L=0):
        self.l=l
        self.L=L

class Rectangle(Forme):
    def __init__(self, l=0, L=0):
        super().__init__(l, L)

    def aire(self):
        return self.l*self.L


r=Rectangle(2,3)
print(f"l'aire du rectangle est: {r.aire()}")
