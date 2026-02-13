Alumnos={
    "nombre":"",
    "edad":0,
    "materia":"",
    "calificacion":""
}
ico201=[]
num=int(input("¿Cuantos alumnos quieres registrar"))
for i in range(num):
    nombre=input("Nombre del alumno:")
    edad=int(input("Edad del alumno:"))
    materia=input("Materia del alumno:")
    calificacion=int(input("Calificacion del alumno:"))


    alumno1["nombre"]= nombre
    alumno1["edad"]= edad 
    alumno1["Materia"]= materia 
    alumno1["Calificacion"]= calificacion


    ico201.append(alumno1.copy())
    print("Lista de alumnos ingresados:")
    for alumno in ico201:
        print(alumno)
        