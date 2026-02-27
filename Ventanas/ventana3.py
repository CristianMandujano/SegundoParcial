import tkinter as tk

#Creamos la ventana principal
def saludo():
    label_resultado.config(text="Hola alumnos de python")

ventana= tk.Tk()
#Le damos un titulo a la ventana
ventana.title("Ejemplo con botones")
#Le damos un tamaño a la ventana 
ventana.geometry("400x300")

#Creamos el boton
boton=tk.Button(ventana, text="Saludar", command=saludo)
boton.pack(pady=20)


#Creamos una etiqueta 
label_resultado= tk.Label(ventana, text="Presiona el boton", font=("Arial", 16,"bold" ))

label_resultado.pack(pady=20)
#Mostramos la etiqueta en la ventana
ventana.mainloop()
