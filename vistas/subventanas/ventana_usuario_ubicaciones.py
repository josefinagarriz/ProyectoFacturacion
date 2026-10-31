import tkinter as tk
from tkinter import ttk, messagebox
from conexion.conexion import *

class VentanaUsuarioUbicaciones(tk.Toplevel):
    def __init__(self, parent, id_usuario):
        super().__init__(parent)

        self.id_usuario = id_usuario

        self.title("Ubicaciones")
        self.geometry("650x350")
        self.transient(parent)

        frame = tk.Frame(self, padx=15, pady=15)
        frame.pack(fill="both", expand=True)

        tk.Label(frame,text="Ubicaciones del usuario",font=("Segoe UI", 13, "bold")).pack(pady=(0, 10))

        columnas = (
            "País",
            "Provincia",
            "Ciudad",
            "Dirección",
            "Código postal"
        )

        self.tabla = ttk.Treeview(frame,columns=columnas,show="headings",height=8)

        anchos = {
            "País": 100,
            "Provincia": 110,
            "Ciudad": 100,
            "Dirección": 160,
            "Código postal": 100
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
            SELECT
                p.pais,
                pr.provincia,
                ci.ciudad,
                uu.direccion,
                uu.codigo_postal
            FROM usuarios_ubicaciones uu
            LEFT JOIN paises p
                ON p.id = uu.id_pais
            LEFT JOIN provincias pr
                ON pr.id = uu.id_provincia
            LEFT JOIN ciudades ci
                ON ci.id = uu.id_ciudad
            WHERE uu.id_usuario = %s
              AND uu.habilitado = 1
        """

        try:
            cursor.execute(sql, (self.id_usuario,))
            registros = cursor.fetchall()

            for registro in registros:
                self.tabla.insert("","end", values=registro)

        except Exception as e:
            messagebox.showerror("Error",f"No se pudieron cargar las ubicaciones:\n{e}",parent=self )

        finally:
            cursor.close()
            conex.close()
