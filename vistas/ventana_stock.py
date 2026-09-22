import tkinter as tk
from tkinter import ttk
from ventana_base import crear_menu
from conexion.conexion import *

class VentanaStock(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Stock")
        self.geometry("650x500")

        # Botones de menú
        crear_menu(self, ventana_actual="Stock", nivel_usuario=nivel_usuario)

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")

        # Campos de formulario stock
        tk.Label(self, text="-Información sobre stock:", font=fuenteTitulo).grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=(12, 4))

        tk.Label(self, text="Descripción").grid(row=3, column=0, sticky="w", padx=(15, 2), pady=3)
        self.cajaDesc = tk.Entry(self, width=18)
        self.cajaDesc.grid(row=3, column=1, sticky="w", pady=3)

        tk.Label(self, text="Tipo").grid(row=3, column=2, sticky="w", padx=(10, 2), pady=3)
        self.cajaTipo = tk.Entry(self, width=18)
        self.cajaTipo.grid(row=3, column=3, sticky="w", pady=3)

        tk.Label(self, text="Precio").grid(row=4, column=0, sticky="w", padx=(15, 2), pady=3)
        self.cajaPrecio = tk.Entry(self, width=18)
        self.cajaPrecio.grid(row=4, column=1, sticky="w", pady=3)

        tk.Label(self, text="Cantidad").grid(row=4, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaCant = tk.Entry(self, width=18)
        self.cajaCant.grid(row=4, column=3, sticky="w", pady=3)

        # Botones de stock
        if nivel_usuario in ("admin", "gerente"):
            botonInsertar = tk.Button(self, text="Insertar", command=self.insertar)
            botonInsertar.grid(row=5, column=0, padx=15, pady=3, sticky="w")

            botonModificar = tk.Button(self, text="Modificar", command=self.modificar)
            botonModificar.grid(row=5, column=1, padx=15, pady=3, sticky="w")

            botonEliminar = tk.Button(self, text="Eliminar", command=self.eliminar)
            botonEliminar.grid(row=5, column=2, padx=15, pady=3, sticky="w")

        # separador
        ttk.Separator(self, orient="horizontal").grid(row=6, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        # tabla de stock
        tk.Label(self, text="-Tabla de stock:", font=fuenteTitulo).grid(row=7, column=0, columnspan=4, sticky="w", padx=10, pady=(0, 4))
        columnas = ("Id", "Descripción", "Tipo", "Precio", "Cantidad")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)
        self.tabla.grid(row=8, column=0, columnspan=7, padx=10, sticky="ew")

        # Para que al seleccionar una fila, su info aparezca en las cajas
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar_tabla()  # para que al abrir la ventana, aparezca lo que ya está en la tabla

    # funcion para guardar stock en tabla con boton insertar
    def insertar(self):
        conex = conectar()
        cursor = conex.cursor()
        sql = """INSERT INTO stock(descripcion, tipo, precio, cantidad)
                 VALUES (%s, %s, %s, %s)"""

        valores = (
            self.cajaDesc.get(),
            self.cajaTipo.get(),
            float(self.cajaPrecio.get()),
            int(self.cajaCant.get())
        )

        cursor.execute(sql, valores)
        conex.commit()

        cursor.close()
        conex.close()

        # insertar nueva fila en tabla
        self.cargar_tabla()

        # limpiar las cajas después de insertar
        self.limpiar_cajas()

    def cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        conex = conectar()
        cursor = conex.cursor()
        cursor.execute("""SELECT id, descripcion, tipo, precio, cantidad
                          FROM stock""")
        registros = cursor.fetchall()
        for registro in registros:
            self.tabla.insert("", "end", values=registro)
        cursor.close()
        conex.close()

    #funcion para seleccionar fila en tabla
    def seleccionar(self, event):
        seleccion=self.tabla.selection()
        if not seleccion:
            return

        fila=seleccion[0]
        valores=self.tabla.item(fila,"values")

        self.limpiar_cajas()

        self.cajaDesc.insert(0,valores[1])
        self.cajaTipo.insert(0,valores[2])
        self.cajaPrecio.insert(0,valores[3])
        self.cajaCant.insert(0,valores[4])

    #funcion para modificar fila en tabla
    def modificar(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            return

        fila = seleccion[0]

        valores = self.tabla.item(fila, "values")
        id = valores[0]
        conex = conectar()
        cursor = conex.cursor()

        sql = """UPDATE stock SET descripcion = %s, tipo = %s,  precio = %s, cantidad = %s 
                 WHERE id = %s """

        datos = (
            self.cajaDesc.get(),
            self.cajaTipo.get(),
            self.cajaPrecio.get(),
            self.cajaCant.get(),
            id
        )

        cursor.execute(sql, datos)

        conex.commit()
        cursor.close()
        conex.close()
        self.cargar_tabla()

        # limpiar las cajas después de modificar
        self.limpiar_cajas()

    #funcion para eliminar fila en tabla
    def eliminar(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            return

        fila = seleccion[0]
        valores = self.tabla.item(fila, "values")
        id = valores[0]
        conex = conectar()
        cursor = conex.cursor()
        sql = """DELETE FROM stock
                 WHERE id = %s """

        cursor.execute(sql, (id,))
        conex.commit()
        cursor.close()
        conex.close()
        self.cargar_tabla()

        # limpiar las cajas después de eliminar
        self.limpiar_cajas()

    #funcion para limpiar cajas
    def limpiar_cajas(self):
        self.cajaDesc.delete(0, tk.END)
        self.cajaTipo.delete(0, tk.END)
        self.cajaPrecio.delete(0, tk.END)
        self.cajaCant.delete(0, tk.END)