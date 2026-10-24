import tkinter as tk
from vistas.ventana_base import crear_menu

def abrir_ventana_admin():
    #Ventana principal
    ventana = tk.Tk()
    ventana.title("Almacén :)")
    ventana.geometry("600x500")
    ventana.configure(background="lightblue")

    # fuente reutilizable para dar jerarquía visual
    fuenteTitulo = ("Segoe UI", 15, "bold")

    # Contenedor para centrar el contenido
    frame = tk.Frame(ventana, background="lightblue")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # titulo
    tk.Label(frame, text="Página Principal", font=fuenteTitulo, background="lightblue").grid(row=0, column=0, pady=15)

    # imagen
    frameImagen = tk.Frame(frame)  # frame para la imagen
    frameImagen.grid(row=1, column=0)

    imagen = tk.PhotoImage(file="../assets/imag.png")
    labelImagen = tk.Label(frameImagen, image=imagen, background="lightgreen", relief="ridge", bd=5)
    labelImagen.grid(row=0, column=0)

    # Botones de menú
    frameMenu = tk.Frame(frame)  # frame para los botones
    frameMenu.grid(row=2, column=0, pady=15)
    frameMenu.configure(background="lightblue")

    crear_menu(frameMenu, fila=0, nivel_usuario="admin")

    # abrir ventana
    ventana.mainloop()
