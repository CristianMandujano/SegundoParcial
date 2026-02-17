import os

os.system("cls")
print("Operaciones: \n1.- Suma\n2.- Resta\n3.- Multiplicacion\n4.- Division\n5.- Salir")


def suma():
       os.system("cls")
       a= int(input("Ingrese el primer numero: "))
       b= int(input("Ingrese el segundo numero: "))
       c=a+b
       return c
       print ("El resultado de la suma es: ", suma())
       input()

def resta(): 
    os.system("cls")
    num1= int(input("Ingrese el primer numero: "))
    num2= int(input("Ingrese el segundo numero: "))
    resta= num1 - num2
    print ("El resultado de la resta es: ", resta) 
    input()

def multiplicacion():
   os.system("cls")
   num1= int(input("Ingrese el primer numero: "))
   num2= int(input("Ingrese el segundo numero: "))
   multiplicacion= num1 * num2
   print ("El resultado de la multiplicacion es: ", multiplicacion)
   input()

def division():
    os.system("cls")
    num1= int(input("Ingrese el primer numero: "))
    num2= int(input("Ingrese el segundo numero: "))
    division= num1 / num2
    print ("El resultado de la division es: ", division)
    input()

def menu():
    op=0
    while op!=5:
        os.system("cls")
        print(" 1.- +\n 2.- -\n 3.- *\n 4.- / \n 5.- Salir\n")
        op=int(input('OPCION '))
        if op==1:
            suma()
        if op==2:
            resta()
        if op==3:
            multiplicacion()
        if op==4:
            division()
              

