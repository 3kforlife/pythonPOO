from CPoint import *
print("les coordonnées du premier point")
p1=float(input("x = "))
p2=float(input("y = "))
p=Point(p1,p2)
p.afficherPoint()

print("coordonnées permettant le deplacement du point")
d1=float(input("dx = "))
d2=float(input("dy = "))
p.translation(d1,d2)
p.afficherPoint()

print("les coordonnées du deuxieme point")
x1=float(input("x = "))
x2=float(input("y = "))
x=Point(x1,x2)
x.afficherPoint()

print(f"la distance entre p et x est {p.distance(x)}")
print("le milieu entre p et x est",end=" ")
c=p.milieuPoint(x)
c.afficherPoint()


