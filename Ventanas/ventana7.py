import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Cerrar con configuracion")
root.geometry("500x400")
def cerrar():
    respuesta= messagebox.askyesno("salir", "¿Deseas cerrar la aplicación?")
    if respuesta:
        root.destroy()


#Cargar imagen
imagen=Image.open("imagen.jpeg")
fondo=ImageTk.PhotoImage(imagen)
#label como fondo
label_fondo=tk.Label(root, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

frame_acciones=tk.LabelFrame(root, text="Acciones", bg="#2672BA", fg="white", padx=10, pady=10 )
frame_acciones.place(x=200, y=250, width=200, height=100)
tk.Button(frame_acciones, text="salir", command=cerrar).pack(pady=20)


root.mainloop()
