import math, os

class OperasBas:
    n1=0
    n2=0
    res=0
    def sumar(self,a,b):
        self.res.n1+self.n2
        return self.res
    def resta(self,a,b):
        self.res.n1-self.n2
        return self.res
    def multiplicacion(self,a,b):
        self.res.n1*self.n2
        return self.res
    def division(self,a,b):
        self.res.n1/self.n2
        return self.res
    def pedirNumeros( self):
        self.n1=int(input("n1: "))
        self.n2=int(input("n2: "))

    def imprimir(self):
        print("El resultado es: ", self.res)

#Creando objetos
def main():
   obj=OperasBas()


   op=0

   while op!=5:
        os.system('cls')
        print("1.- +\n 2.- -\n 3.- \n 4.- /\n 5.- salir\n")
        op=int(input('OPCION:'))
        if op==1:
           obj.pedirNumeros()
           obj.sumar()
           obj.imprimir()
           input()
        if op ==2:
           obj.pedirNumeros()
           obj.resta()
           obj.imprimir()
           input()
        if op ==3:
           obj.pedirNumeros()
           obj.multiplicacion()
           obj.imprimir()
           input()
        if op ==4:
           obj.pedirNumeros()
           obj.division()
           obj.imprimir()
           input()

if __name__=="__main__":
    main()


