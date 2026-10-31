import tkinter as tk
from tkinter import ttk, messagebox
from conexion.conexion import *

class VentanaUsuarioRedes(tk.Toplevel):
    def __init__(self, parent, id_usuario):
        super().__init__(parent)

        self.id_usuario = id_usuario

        self.title("Redes")
        self.geometry("650x350")
        self.transient(parent)

        frame = tk.Frame(self, padx=15, pady=15)
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Redes del usuario",font=("Segoe UI", 13, "bold")).pack(pady=(0, 10))

        columnas = (
            "Redes",
            "Tipo"
        )

        self.tabla = ttk.Treeview(frame,columns=columnas,show="headings",height=8)

        anchos = {
            "Redes": 200,
            "Tipo":100
        }

        for columna in columnas:
            self.tabla.heading(columna, text=columna)
            self.tabla.column(columna,width=anchos[columna], anchor="center")

        self.tabla.pack(fill="both", expand=True)

        self.cargar_tabla()

    def cargar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        conex = conectar()
        cursor = conex.cursor()

        sql = """
            SELECT ur.handle, tr.red_social
            FROM usuarios_redes ur
            INNER JOIN tipos_rs tr
                ON ur.id_tipo_rs = tr.id
            WHERE ur.id_usuario = %s
            AND ur.habilitado = 1
            AND tr.habilitado = 1;
        """

        try:
            cursor.execute(sql, (self.id_usuario,))
            registros = cursor.fetchall()

            for registro in registros:
                self.tabla.insert("","end", values=registro)

        except Exception as e:
            messagebox.showerror("Error",f"No se pudieron cargar las Redes:\n{e}",parent=self )

        finally:
            cursor.close()
            conex.close()
