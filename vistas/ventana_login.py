import tkinter as tk
from admin import ventana_admin
from gerente import ventana_gerente
from empleado import ventana_empleado
from tkinter import messagebox
from conexion.conexion import *

def ingresar():
    usuario=cajaUsuario.get()
    contrasenia=cajaContrasenia.get()

    conexion=conectar()
    cursor=conexion.cursor()

    sql="""SELECT usuario, password, nivel_usuario
           FROM usuarios
           WHERE usuario=%s"""

    cursor.execute(sql, (usuario,))
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    #corrobora si el usuario existe
    if resultado is None:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrecto")
        return

    #el usuario existe, ahora ve si la contraseña es correcta
    usuarioBD = resultado[0]
    contraseniaBD = resultado[1]
    nivel = resultado[2]

    if contrasenia != contraseniaBD: #si no, da error
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrecto")
        return

    ventana.destroy()
    if nivel == "admin":
        ventana_admin.abrir_ventana_admin()
    elif nivel == "gerente":
        ventana_gerente.abrir_ventana_gerente()
    elif nivel == "empleado":
        ventana_empleado.abrir_ventana_empleado()


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