'''
Docstring for funciones
Las funciones en Python son bloques de código reutilizables que realizan una tarea específica.
Sirven para organizar, reutilizar y hacer más claro el código.
¿Para qué sirven?
* Evitan repetir código.
* Permiten dividir un problema grande en partes pequeñas.
* Hacen el programa más fácil de mantener.
* Mejoran la legibilidad.
En Python se definen con la palabra clave def:
Copiar código
def nombre_funcion(parametros):
    # bloque de código
    return valor
'''

def nombre():#Funcion que no recibe ni regresa nada
    print("Hola mundo")
nombre()

def suma():
    
    a=6
    b=7
    c= a+b


    a=3
    b=7
    c=a+b
    return c #Siempre va al final
print(suma())

def multiplica(a,b):
    return