import math
import os

class OperasBas:

    def __init__(self):
        self.res = 0

    def Cuadrado(self):
        lado = float(input("Lado: "))
        self.res = lado * lado
        return self.res

    def Rectangulo(self):
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        self.res = base * altura
        return self.res

    def Triangulo(self):
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        self.res = (base * altura) / 2
        return self.res

    def Circulo(self):
        radio = float(input("Radio: "))
        self.res = math.pi * (radio ** 2)
        return self.res

    def Trapecio(self):
        baseMayor = float(input("Base mayor: "))
        baseMenor = float(input("Base menor: "))
        altura = float(input("Altura: "))
        self.res = ((baseMayor + baseMenor) * altura) / 2
        return self.res

    def imprimir(self):
        print("El área de la figura es: ", self.res)


def main():
    obj = OperasBas()
    op = 0

    while op != 6:
        os.system('cls') 
        print("Seleccione el área que desea calcular: ")
        print("1.- Cuadrado")
        print("2.- Rectangulo")
        print("3.- Triangulo")
        print("4.- Circulo")
        print("5.- Trapecio")
        print("6.- Salir")

        op = int(input('OPCION: '))

        if op == 1:
            obj.Cuadrado()
            obj.imprimir()
            input()

        elif op == 2:
            obj.Rectangulo()
            obj.imprimir()
            input()

        elif op == 3:
            obj.Triangulo()
            obj.imprimir()
            input()

        elif op == 4:
            obj.Circulo()
            obj.imprimir()
            input()

        elif op == 5:
            obj.Trapecio()
            obj.imprimir()
            input()


if __name__ == "__main__":
    main()