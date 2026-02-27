import tkinter as tk

#Creamos la ventana principal
ventana= tk.Tk()
#Le damos un titulo a la ventana
ventana.title("Mi primera aplicación")
#Le damos un tamaño a la ventana 
ventana.geometry("400x300")

#Creamos una etiqueta 
etiqueta = tk.Label(ventana, text="Hola Mundo", font=("Arial", 16,"bold" ))

etiqueta.pack(pady=20)
#Mostramos la etiqueta en la ventana
ventana.mainloop()
