import tkinter as tk
from tkinter import ttk
from ventana_base import crear_menu
from conexion.conexion import *
from tkinter import messagebox
from datetime import datetime

class VentanaEntradas(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Entradas")
        self.geometry("750x800")

        # Botones de menú
        crear_menu(self, ventana_actual="Entradas", nivel_usuario=nivel_usuario)

        # fuentes reutilizables para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")
        fuenteTotal = ("Segoe UI", 12, "bold")

        # Campos de entradas
        tk.Label(self, text="Datos de entrada", font=fuenteTitulo).grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=(12, 4))

        tk.Label(self, text="Id Proveedor").grid(row=3, column=0, sticky="w", padx=(15, 2), pady=3)
        self.cajaProveedor = tk.Entry(self, width=18)
        self.cajaProveedor.grid(row=3, column=1, sticky="w", pady=3)

        tk.Label(self, text="Id Stock").grid(row=3, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaStock = tk.Entry(self, width=18)
        self.cajaStock.grid(row=3, column=3, sticky="w", pady=3)

        tk.Label(self, text="Cantidad").grid(row=4, column=0, sticky="w", padx=(15, 2), pady=3)
        self.cajaCant = tk.Entry(self, width=18)
        self.cajaCant.grid(row=4, column=1, sticky="w", pady=3)

        tk.Label(self, text="Descuento %").grid(row=4, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaDesc = tk.Entry(self, width=18)
        self.cajaDesc.grid(row=4, column=3, sticky="w", pady=3)

        #Botones de facturación
        botonInsertar = tk.Button(self, text="Insertar entrada", command=self.insertar)
        botonInsertar.grid(row=6, column=0, columnspan=2, padx=5, pady=3, sticky="w")

        ttk.Separator(self, orient="horizontal").grid(row=7, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        #tabla de entradas
        tk.Label(self, text="Tabla de entradas", font=fuenteTitulo).grid(row=8, column=0, columnspan=4, sticky="w", padx=10, pady=(0, 4))

        columnas = ("Id","Id Proveedor", "Id Stock", "Cantidad", "Valor Unidad $", "Descuento %", "Total $", "fecha")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)
        self.tabla.grid(row=9, column=0, columnspan=7, padx=10, sticky="ew")

        #Para que al seleccionar una fila, su info aparezca en las cajas
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar_tabla()

    # funcion para guardar entradas en tabla con boton insertar
    def insertar (self):
        proveedor= int(self.cajaProveedor.get())
        stock= int(self.cajaStock.get())
        cant= int(self.cajaCant.get())
        desc= float(self.cajaDesc.get())

        conex = conectar()
        cursor = conex.cursor()

        #corroborar que existen los id
        cursor.execute("SELECT id FROM proveedores WHERE id = %s", (proveedor,))
        existeProveedor = cursor.fetchone()

        cursor.execute("SELECT id FROM stock WHERE id = %s", (stock,))
        existeStock = cursor.fetchone()

        if existeProveedor is None:
            messagebox.showerror(
                "Error",
                "No existe un proveedor con ese ID."
            )
            return

        if existeStock is None:
            messagebox.showerror(
                "Error",
                "No existe un stock con ese ID."
            )
            return

        #buscar producto
        sqlProducto = """SELECT precio
                        FROM stock
                        WHERE id = %s """

        cursor.execute(sqlProducto, (stock,))
        producto = cursor.fetchone()

        valor= float(producto[0])
        total= (cant*valor) * ((100 - desc) / 100)
        fecha= datetime.now()

        #insertar entrada en base de datos
        sql = """INSERT INTO entradas(id_proveedor, id_stock, cantidad, precio_unitario, descuento, total, fecha)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        valores = (
            proveedor,
            stock,
            cant,
            valor,
            desc,
            total,
            fecha
        )

        cursor.execute(sql, valores)

        sql_stock = """UPDATE stock
                       SET cantidad = cantidad + %s
                       WHERE id = %s"""

        cursor.execute(sql_stock, (cant, stock))

        conex.commit()

        cursor.close()
        conex.close()

        # insertar nueva fila en tabla
        self.cargar_tabla()

        # limpiar las cajas después de insertar
        self.limpiar_cajas()


    #funcion para seleccionar fila en tabla y que cambien los valores de las cajas
    def seleccionar(self, event):
        seleccion=self.tabla.selection()
        if not seleccion:
            return

        fila=seleccion[0]
        valores=self.tabla.item(fila,"values")

        self.limpiar_cajas()

        self.cajaProveedor.insert(0, valores[1])
        self.cajaStock.insert(0,valores[2])
        self.cajaCant.insert(0,valores[3])
        self.cajaDesc.insert(0,valores[5])


    #funcion para limpiar las cajas de producto (no toca factura/empleado/cliente)
    def limpiar_cajas(self):
        self.cajaProveedor.delete(0,tk.END)
        self.cajaStock.delete(0, tk.END)
        self.cajaCant.delete(0, tk.END)
        self.cajaDesc.delete(0, tk.END)

    def cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        conex = conectar()
        cursor = conex.cursor()
        cursor.execute("""SELECT id, id_proveedor, id_stock, cantidad, precio_unitario, descuento, total, fecha
                          FROM entradas""")
        registros = cursor.fetchall()
        for registro in registros:
            self.tabla.insert("", "end", values=registro)
        cursor.close()
        conex.close()