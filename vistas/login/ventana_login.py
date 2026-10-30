import tkinter as tk
from usuarios import ventana_admin, ventana_empleado, ventana_proveedor, ventana_cliente, ventana_gerente
from tkinter import messagebox
from conexion.conexion import *

def abrir_ventana_login():
    global ventana, cajaUsuario, cajaContrasenia

    # Ventana login
    ventana = tk.Tk()
    ventana.title("Login")
    ventana.geometry("600x500")
    ventana.configure(background="lightblue")

    # fuente reutilizable para dar jerarquía visual
    fuenteTitulo = ("Segoe UI", 15, "bold")

    # Contenedor para centrar el login
    frameLogin = tk.Frame(ventana, background="lightgreen", relief="ridge", bd=5)
    frameLogin.place(relx=0.5, rely=0.5, anchor="center")

    # titulo
    tk.Label(frameLogin, text="LOGIN", font=fuenteTitulo, background="lightgreen").grid(row=0, column=0, columnspan=2,pady=15)

    #usuario
    tk.Label(frameLogin, text="Usuario", background="lightgreen").grid(row=1, column=0, padx=10, pady=8, sticky="e")
    cajaUsuario = tk.Entry(frameLogin, width=22)
    cajaUsuario.grid(row=1, column=1, padx=10, pady=8)

    #contraseña
    tk.Label(frameLogin, text="Contraseña", background="lightgreen").grid(row=2, column=0, padx=10, pady=8, sticky="e")
    cajaContrasenia = tk.Entry(frameLogin, width=22, show="*")
    cajaContrasenia.grid(row=2, column=1, padx=10, pady=8)

    # ingresar
    botonIngresar = tk.Button(frameLogin, text="INGRESAR", command=ingresar, background="white")
    botonIngresar.grid(row=3, column=0, columnspan=2, pady=15)

    # abrir ventana
    ventana.mainloop()



def ingresar():
    usuario=cajaUsuario.get()
    contrasenia=cajaContrasenia.get()

    conexion=conectar()
    cursor=conexion.cursor()

    sql="""SELECT u.habilitado, u.usuario, u.contrasenia, r.rol, r.habilitado
           FROM usuarios u
           JOIN roles r ON u.id_rol = r.id
           WHERE u.usuario=%s"""

    cursor.execute(sql, (usuario,))
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    #corrobora si el usuario existe
    if resultado is None:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrecto")
        return

    #el usuario existe, ahora ve si la contraseña es correcta o si está habilitado (no se borró)
    habilitado_usuario=resultado[0]
    usuarioBD = resultado[1]
    contraseniaBD = resultado[2]
    nivel = resultado[3]
    habilitado_rol = resultado[4]

    # Comprobar si el usuario está habilitado
    if habilitado_usuario != 1: #el usuario ya se borró si es 0
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrecto")
        return

    # Comprobar si la contraseña es correcta
    if contrasenia != contraseniaBD: #si no, da error
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrecto")
        return

    if habilitado_rol != 1: #el usuario ya se borró si es 0
        messagebox.showerror("Error", "El rol de este usuario está deshabilitado")
        return

    if nivel == "admin":
        ventana.destroy()
        ventana_admin.abrir_ventana_admin()
    elif nivel == "gerente":
        ventana.destroy()
        ventana_gerente.abrir_ventana_gerente()
    elif nivel == "empleado":
        ventana.destroy()
        ventana_empleado.abrir_ventana_empleado()
    elif nivel == "cliente":
        ventana.destroy()
        ventana_cliente.abrir_ventana_cliente()
    elif nivel == "proveedor":
        ventana.destroy()
        ventana_proveedor.abrir_ventana_proveedor()
    else:
        messagebox.showerror( "Error","El rol asignado no tiene una ventana configurada")

if __name__ == "__main__":
    abrir_ventana_login()