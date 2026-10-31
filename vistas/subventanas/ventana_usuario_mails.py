import tkinter as tk
from tkinter import ttk, messagebox
from conexion.conexion import *

class VentanaUsuarioMails(tk.Toplevel):
    def __init__(self, parent, id_usuario):
        super().__init__(parent)

        self.id_usuario = id_usuario

        self.title("Mails")
        self.geometry("650x350")
        self.transient(parent)

        frame = tk.Frame(self, padx=15, pady=15)
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Mails del usuario",font=("Segoe UI", 13, "bold")).pack(pady=(0, 10))

        columnas = (
            "Mails",
        )

        self.tabla = ttk.Treeview(frame,columns=columnas,show="headings",height=8)

        anchos = {
            "Mails": 200
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
            SELECT mail
            FROM usuarios_mails
            WHERE id_usuario = %s
            AND habilitado = 1;
        """

        try:
            cursor.execute(sql, (self.id_usuario,))
            registros = cursor.fetchall()

            for registro in registros:
                self.tabla.insert("","end", values=registro)

        except Exception as e:
            messagebox.showerror("Error",f"No se pudieron cargar los mails:\n{e}",parent=self )

        finally:
            cursor.close()
            conex.close()
