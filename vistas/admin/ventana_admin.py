import tkinter as tk
from vistas.ventana_base import crear_menu

def abrir_ventana_admin():
    #Ventana principal
    ventana = tk.Tk()
    ventana.title("Almacén :)")
    ventana.geometry("600x400")

    # Hacer que la columna principal ocupe todo el ancho (esté centrada)
    ventana.columnconfigure(0, weight=1)

    # fuente reutilizable para dar jerarquía visual
    fuenteTitulo = ("Segoe UI", 10, "bold")

    #titulo
    tk.Label(ventana, text="Página Principal Admin", font=fuenteTitulo).grid(row=0,column=0, pady=10)

    #imagen
    frameImagen = tk.Frame(ventana) #frame para la imagen
    frameImagen.grid(row=1, column=0)

    imagen = tk.PhotoImage(file="../assets/imag.png")
    labelImagen = tk.Label(frameImagen, image=imagen)
    labelImagen.grid(row=0, column=0)

    #Botones de menú
    frameMenu = tk.Frame(ventana) #frame para los botones
    frameMenu.grid(row=2, column=0, pady=15)

    crear_menu(frameMenu, fila=0)

    #abrir ventana
    ventana.mainloop()