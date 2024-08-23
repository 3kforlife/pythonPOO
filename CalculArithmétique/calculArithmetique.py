class Calcul(object):
    def __init__(self):
        pass


    #Factorielle
    def factorielle(self,n):
        f=1
        for i in range(1,n+1):
            f*=i
        return f
    
    #cumul
    def cumul(self,n):
        s=0
        for i in range(1,n+1):
            s+=i
        return s
    
    #test de primalité d'un nombre
    def testPrimalite(self,n):
        p=0
        for i in range(1,n+1):
            if(n%i==0):
                p+=1
        if(p==2):
            return True
        else:
            return False
        
    #test de primalité de deux nombres
    def testPrimalites(self,n,m):
        divCommun=0
        for i in range(1,n+1):
            if(n%i==0 and m%i==0):
                divCommun+=1
        if(divCommun==1):
            print("Ces deux entiers sont premiers")
        else:
            print("Ces deux entiers ne sont pas premiers")

    #table de multiplication
    def tableMultiplication(self,n):
        for i in range(1,13):
            print(f"{n} * {i} = {n*i}")

    #listes des diviseurs d'un entier
    def diviseurs(self,n):
        listDiv=[]
        for i in range(1,n+1):
            if(n%i==0):
                listDiv.append(i)
        return listDiv
    
    #listes des diviseurs premiers d'un entier
    def diviseursPremiers(self,n):
        listDivPr=[]
        for i in range(1,n+1):
            if(n%i==0 and self.testPrimalite(i)):
                listDivPr.append(i)
        return listDivPr
