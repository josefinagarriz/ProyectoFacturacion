import tkinter as tk
import ventana_principal

def ingresar():
    ventana.destroy()
    ventana_principal.abrir_ventana_principal()

#Ventana login
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("600x400")

# fuente reutilizable para dar jerarquía visual
fuenteTitulo = ("Segoe UI", 10, "bold")

#titulo
tk.Label(ventana, text="Ingresar\ncredenciales", font=fuenteTitulo).grid(row=0,column=1)

#usuario
tk.Label(ventana, text="Usuario:").grid(row=1,column=0)
cajaUsuario = tk.Entry(width=18)
cajaUsuario.grid(row=1, column=2)

#contraseña
tk.Label(ventana, text="Contraseña:").grid(row=2,column=0)
cajaContrasenia = tk.Entry(width=18, show="*")
cajaContrasenia.grid(row=2, column=2)

#ingresar
botonIngresar = tk.Button(text="Ingresar", command=ingresar)
botonIngresar.grid(row=3, column=1)

#abrir ventana
ventana.mainloop()