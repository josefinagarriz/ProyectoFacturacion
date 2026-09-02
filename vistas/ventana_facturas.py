import tkinter as tk
from tkinter import ttk
from ventana_base import crear_menu
from conexion.conexion import *

class VentanaFacturas(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Facturas")
        self.geometry("800x600")

        # Botones de menú
        crear_menu(self, ventana_actual="Facturas")

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")

        # tabla de facturas
        tk.Label(self, text="-Tabla de facturas:", font=fuenteTitulo).grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=(0, 4))

        columnas = ("Id", "Fecha","Empleado", "Cliente", "Subtotal", "Descuento", "Total")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)
        self.tabla.grid(row=3, column=0, columnspan=7, padx=10, sticky="ew")

        self.tabla.bind("<<TreeviewSelect>>",self.seleccionar_factura)

        self.cargar_facturas()

        # separador
        ttk.Separator(self, orient="horizontal").grid(row=4, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        # tabla de detalles
        tk.Label(self, text="-Tabla de detalles:", font=fuenteTitulo).grid(row=5, column=0, columnspan=4, sticky="w",padx=10, pady=(0, 4))

        columnasDetalles = ("Id Detalle","Id Stock","Cantidad","Valor Unitario","Descuento","Total")
        self.tablaDetalle = ttk.Treeview(self, columns=columnasDetalles, show="headings", height=10)
        for col in columnasDetalles:
            self.tablaDetalle.heading(col, text=col)
            self.tablaDetalle.column(col, width=100)
        self.tablaDetalle.grid(row=6, column=0, columnspan=7, padx=10, sticky="ew")

    def cargar_facturas(self):

        conex = conectar()
        cursor = conex.cursor()

        sql = """SELECT id, fecha, id_empleado, id_cliente, subtotal, descuento, total
              FROM facturas
              ORDER BY id  """

        cursor.execute(sql)
        registros = cursor.fetchall()

        cursor.close()
        conex.close()

        for registro in registros:
            self.tabla.insert("","end",values=registro)

    def seleccionar_factura(self, event):
        seleccion = self.tabla.selection()

        if not seleccion:
            return

        fila = seleccion[0]

        valores = self.tabla.item(
            fila,
            "values"
        )

        idFactura = valores[0]

        self.cargar_detalles(idFactura)

    def cargar_detalles(self, idFactura):

        # Primero limpiar la tabla de detalles
        for fila in self.tablaDetalle.get_children():
            self.tablaDetalle.delete(fila)

        conex = conectar()
        cursor = conex.cursor()

        sql = """
              SELECT id, id_stock, cantidad, valor_unitario,  descuento, total
              FROM detalle_factura 
              WHERE id_factura = %s """

        cursor.execute(sql, (idFactura,))
        registros = cursor.fetchall()

        cursor.close()
        conex.close()

        for registro in registros:
            self.tablaDetalle.insert(
                "",
                "end",
                values=(
                    registro[0],
                    registro[1],
                    registro[2],
                    f"{registro[3]:.2f}",
                    f"{registro[4]:.2f}",
                    f"{registro[5]:.2f}"
                )
            )