import tkinter as tk
from tkinter import ttk
from ventana_base import crear_menu
from conexion.conexion import *

class VentanaComprar(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Comprar")
        self.geometry("1050x550")

        #Botones de menú
        crear_menu(self, ventana_actual="Comprar", nivel_usuario=nivel_usuario)

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")

        #Campos