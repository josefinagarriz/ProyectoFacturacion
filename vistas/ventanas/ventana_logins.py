import tkinter as tk
from base.ventana_base import crear_menu


class VentanaLogins(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Logins")
        self.geometry("1050x550")

        #Botones de menú
        crear_menu(self, ventana_actual="Logins", nivel_usuario=nivel_usuario)

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")

        #Campos