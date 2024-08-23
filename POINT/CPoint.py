from math import sqrt
class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self,x):
        self.x=x
    
    def set_y(self,y):
        self.y=y

    def afficherPoint(self):
        print(f"({self.x},{self.y})")

    def translation(self,do,da):
        self.set_x(self.get_x()+do)
        self.set_y(self.get_y()+da)
        return

    def milieuPoint(self,p):
        p1=Point()
        p1.x=(self.get_x()+p.get_x())/2
        p1.y=(self.get_y()+p.get_y())/2
        return p1
    
    def distance(self,p):
        dx=(abs(self.get_x() - p.get_x()))**2
        dy=(abs(self.get_y() - p.get_y()))**2
        d=sqrt(dx+dy)
        return d
    




