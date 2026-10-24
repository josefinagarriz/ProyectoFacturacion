import tkinter as tk
import ventana_admin
import ventana_gerente
import ventana_empleado
import ventana_cliente
import ventana_proveedor
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
    elif nivel == "cliente":
        ventana_cliente.abrir_ventana_cliente()
    elif nivel == "proveedor":
        ventana_proveedor.abrir_ventana_proveedor()

#Ventana login
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("600x500")
ventana.configure(background="lightblue")

# fuente reutilizable para dar jerarquía visual
fuenteTitulo = ("Segoe UI", 15, "bold")

# Contenedor para centrar el login
frameLogin = tk.Frame(ventana, background="lightgreen", relief="ridge", bd=5)
frameLogin.place(relx=0.5, rely=0.5, anchor="center")

#titulo
tk.Label(frameLogin, text="LOGIN", font=fuenteTitulo, background="lightgreen").grid(row=0, column=0, columnspan=2, pady=15)

#usuario
tk.Label(frameLogin, text="Usuario", background="lightgreen").grid(row=1, column=0, padx=10, pady=8, sticky="e")
cajaUsuario = tk.Entry(frameLogin, width=22)
cajaUsuario.grid(row=1, column=1, padx=10, pady=8)

#contraseña
tk.Label(frameLogin, text="Contraseña", background="lightgreen").grid(row=2, column=0, padx=10, pady=8, sticky="e")
cajaContrasenia = tk.Entry(frameLogin, width=22, show="*")
cajaContrasenia.grid(row=2, column=1, padx=10, pady=8)

#ingresar
botonIngresar = tk.Button(frameLogin, text="INGRESAR", command=ingresar, background="white")
botonIngresar.grid(row=3, column=0, columnspan=2, pady=15)

#abrir ventana
ventana.mainloop()