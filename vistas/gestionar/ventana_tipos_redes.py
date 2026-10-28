import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conexion.conexion import *

class VentanaTiposRedes(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Tipos redes")
        self.geometry("1050x550")

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")

        #Campos