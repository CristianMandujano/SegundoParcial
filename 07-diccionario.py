'''
Docstring for 07-diccionario

¿Que es un diccionario?
un diccionarion es una estructura de datos que almacena informacion en pares clave-valor

no se accede por posicion si no por clave 

ejemplo:
'''
alumno={
      "nombre": "Ana",
      "edad": 21,
      "carrera": "Ingenieria"
}
print(type(alumno))
print(alumno)

print("print(alumno['nombre']) = ", alumno["nombre"])
print("print(alumno.get('edad')) = ", alumno.get("edad"))

#Agregar o modificar valores
alumno["promedio"]=9.2
print(alumno)
alumno["edad"] = 22
print(alumno)

#Eliminar un par clave-valor
del alumno["carrera"]
print(alumno)

#Recorrer un diccionario
for clave in alumno:
    print(clave)
    print(clave, ":", alumno[clave])

#Funciones mu utiles para diccionarios
print("Cantidad de pares clave-valor: ",len(alumno))
print("Claves del diccionario: ",alumno.keys())
print("Valores del diccionario: ",alumno.values())
print("Pares clave valor: ", alumno.items())

alumno1 = {
       "nombre": "",
       "edad": 0,
       "carrera": "Ingenieria"
}
ICO201=[alumno1,alumno1,alumno1]











