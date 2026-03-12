import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox

def calcular():
    if var1.get() == "" or var2.get() == "" or var3.get() == "":
        messagebox.showerror("ERROR", "FALTAN COLORES POR SELECCIONAR")
        return 
    colores= {
        "Negro": 0, "Café": 1, "Rojo": 2, "Naranja": 3, 
        "Amarillo": 4, "Verde": 5, "Azul": 6, "Violeta": 7, 
        "Gris": 8, "Blanco": 9
    }

    try: 
        c1 = colores[var1.get()]
        c2 = colores[var2.get()]
        c3 = colores[var3.get()]
    
        valor_ohm = (c1 * 10 + c2) * (10 ** c3)
    
        porcentaje = 0.05 if var_tol.get() == 1 else 0.10
    
        v_max = valor_ohm * (1 + porcentaje)
        v_min = valor_ohm * (1 - porcentaje)
    
        lbl_res_ohm.config(text=str(valor_ohm))
        lbl_res_max.config(text=f"{v_max:.1f}")
        lbl_res_min.config(text=f"{v_min:.1f}")
    
    except ValueError:
        messagebox.showerror("Error", "Selecciona los 3 colores")

ventana = tk.Tk()
ventana.title("Practica Resistencias")
ventana.geometry("550x750")
ventana.configure(bg="#5EC5EE") 

tk.Label(ventana, text="Calcular Valor de resistencias", bg="#00FF55", 
         font=("Arial", 12, "bold"), bd=0).pack()

img_pil = Image.open("Resistencias.jpg")  
img_pil_resized = img_pil.resize((200,250), Image.Resampling.LANCZOS)   
tk_image = ImageTk.PhotoImage(img_pil_resized)
    
label_imagen = tk.Label(ventana, image=tk_image, bg="#87CEEB", pady=10)
label_imagen.image = tk_image
label_imagen.pack(pady=15)

opciones = ["Negro", "Café", "Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Violeta", "Gris", "Blanco"]

var1 = tk.StringVar(ventana); var1.set("")
var2 = tk.StringVar(ventana); var2.set("")
var3 = tk.StringVar(ventana); var3.set("")

frame_color1 = tk.Frame(ventana, bg="#87CEEB")
frame_color1.pack(pady=5)
tk.Label(frame_color1, text="seleccionar color 1", bg="#87CEEB", width=15).pack(side="left")
tk.OptionMenu(frame_color1, var1, *opciones).pack(side="left")

f2 = tk.Frame(ventana, bg="#87CEEB")
f2.pack(pady=5)
tk.Label(f2, text="seleccionar color 2", bg="#87CEEB", width=15).pack(side="left")
tk.OptionMenu(f2, var2, *opciones).pack(side="left")

f3 = tk.Frame(ventana, bg="#87CEEB")
f3.pack(pady=5)
tk.Label(f3, text="seleccionar color 3", bg="#87CEEB", width=15).pack(side="left")
tk.OptionMenu(f3, var3, *opciones).pack(side="left")

tk.Label(ventana, text="Tolerancia", bg="#87CEEB", font=("Arial", 10, "bold")).pack(pady=10)
var_tol = tk.IntVar(value=1) 

tk.Radiobutton(ventana, text="oro", variable=var_tol, value=1, bg="#87CEEB").pack()
tk.Radiobutton(ventana, text="plata", variable=var_tol, value=2, bg="#87CEEB").pack()

tk.Button(ventana, text="calcular", command=calcular, bg="#00FF55", width=15).pack(pady=20)

tk.Label(ventana, text="valor ohm:", bg="#87CEEB").pack()
lbl_res_ohm = tk.Label(ventana, text="0", bg="#87CEEB", font=("Arial", 10, "bold"))
lbl_res_ohm.pack()

tk.Label(ventana, text="valor maximo:", bg="#87CEEB").pack()
lbl_res_max = tk.Label(ventana, text="0", bg="#87CEEB", font=("Arial", 10, "bold"))
lbl_res_max.pack()

tk.Label(ventana, text="valor minimo:", bg="#87CEEB").pack()
lbl_res_min = tk.Label(ventana, text="0", bg="#87CEEB", font=("Arial", 10, "bold"))
lbl_res_min.pack()

ventana.mainloop()