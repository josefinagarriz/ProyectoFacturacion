import tkinter as tk
from tkinter import ttk
from datetime import datetime
from ventana_base import crear_menu
from conexion.conexion import *
from tkinter import messagebox

class VentanaFacturacion(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Facturación")
        self.geometry("750x800")
        #variable global para subtotal
        self.subtotal=0
        #variables globales para después agregar en factura
        self.idEmpleado = None
        self.idCliente = None
        self.fecha = datetime.now()

        # Botones de menú
        crear_menu(self, ventana_actual="Facturación", nivel_usuario=nivel_usuario)

        # fuentes reutilizables para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")
        fuenteTotal = ("Segoe UI", 12, "bold")

        # Campos de facturación
        tk.Label(self, text="Datos de facturación", font=fuenteTitulo).grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=(12, 4))

        tk.Label(self, text="Id Empleado").grid(row=3, column=0, sticky="w", padx=(15, 2), pady=3)
        self.cajaEmpleado = tk.Entry(self, width=18)
        self.cajaEmpleado.grid(row=3, column=1, sticky="w", pady=3)

        tk.Label(self, text="Id Cliente").grid(row=3, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaCliente = tk.Entry(self, width=18)
        self.cajaCliente.grid(row=3, column=3, sticky="w", pady=3)

        botonAceptar = tk.Button(self, text="Aceptar", command=self.aceptar)
        botonAceptar.grid(row=4, column=0, padx=15, pady=3)

        ttk.Separator(self, orient="horizontal").grid(row=5, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        #info sobre los productos en factura
        tk.Label(self, text="Producto a comprar", font=fuenteTitulo).grid(row=6, column=0, columnspan=4, sticky="w", padx=10, pady=(0, 4))

        tk.Label(self, text="Id Stock").grid(row=7, column=0, sticky="w", padx=(10, 2), pady=3)
        self.cajaStock = tk.Entry(self, width=18)
        self.cajaStock.grid(row=7, column=1, sticky="w", pady=3)

        tk.Label(self, text="Cantidad").grid(row=7, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaCant = tk.Entry(self, width=18)
        self.cajaCant.grid(row=7, column=3, sticky="w", pady=3)

        #tk.Label(self, text="Valor Unidad").grid(row=8, column=0, sticky="w", padx=(10, 2), pady=3)
        #self.cajaValor = tk.Entry(self, width=18)
        #self.cajaValor.grid(row=8, column=1, sticky="w", pady=3)

        tk.Label(self, text="Descuento %").grid(row=7, column=4, sticky="w", padx=(15, 2), pady=3)
        self.cajaDesc = tk.Entry(self, width=18)
        self.cajaDesc.grid(row=7, column=5, sticky="w", pady=3)

        #Botones de facturación
        botonInsertar = tk.Button(self, text="Insertar producto", command=self.insertar)
        botonInsertar.grid(row=8, column=0, columnspan=2, padx=5, pady=3, sticky="w")

        botonModificar = tk.Button(self, text="Modificar producto", command=self.modificar)
        botonModificar.grid(row=8, column=2, padx=5, pady=3, sticky="w")

        botonEliminar = tk.Button(self, text="Eliminar producto", command=self.eliminar)
        botonEliminar.grid(row=8, column=4, padx=5, pady=3, sticky="w")

        ttk.Separator(self, orient="horizontal").grid(row=9, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        #info de factura
        tk.Label(self, text="Resumen de factura", font=fuenteTitulo).grid(row=10, column=0, columnspan=4, sticky="w", padx=10, pady=(0, 4))

        tk.Label(self, text="Factura:").grid(row=11, column=0, sticky="w", padx=(10, 2), pady=3)
        self.labelFactura = tk.Label(self, text=self.obtenerProximoIdFactura())
        self.labelFactura.grid(row=11, column=1, sticky="w", pady=3)

        tk.Label(self, text="Empleado:").grid(row=11, column=2, sticky="w", padx=(15, 2), pady=3)
        self.labelEmpleado = tk.Label(self, text="-")
        self.labelEmpleado.grid(row=11, column=3, sticky="w", pady=3)

        tk.Label(self, text="Cliente:").grid(row=12, column=0, sticky="w", padx=(10, 2), pady=3)
        self.labelCliente = tk.Label(self, text="-")
        self.labelCliente.grid(row=12, column=1, sticky="w", pady=3)

        tk.Label(self, text="Fecha:").grid(row=12, column=2, sticky="w", padx=(15, 2), pady=3)
        self.labelFecha = tk.Label(self,text=f"{self.fecha:%d/%m/%Y %H:%M}")
        self.labelFecha.grid(row=12, column=3, columnspan=2, sticky="w", pady=3)

        ttk.Separator(self, orient="horizontal").grid(row=13, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        # tabla de facturación
        tk.Label(self, text="Tabla de facturación", font=fuenteTitulo).grid(row=14, column=0, columnspan=4, sticky="w", padx=10, pady=(0, 4))

        columnas = ("Id Stock", "Descripción", "Cantidad", "Valor Unidad $", "Descuento %", "Total $")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)
        self.tabla.grid(row=15, column=0, columnspan=7, padx=10, sticky="ew")

        #Para que al seleccionar una fila, su info aparezca en las cajas
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        ttk.Separator(self, orient="horizontal").grid(row=16, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        #etiquetas de subtotal y total final
        tk.Label(self, text="Subtotal:").grid(row=17, column=0, sticky="w", padx=(10, 2), pady=(2, 12))
        self.labelSub = tk.Label(self, text="$0", font=fuenteTotal)
        self.labelSub.grid(row=17, column=1, sticky="w", pady=(2, 12))

        tk.Label(self, text="Descuento %").grid(row=17, column=2, sticky="w", padx=(15, 2), pady=(2, 12))
        self.cajaSubDesc = tk.Entry(self, width=18)
        self.cajaSubDesc.grid(row=17, column=3, sticky="w", pady=(2, 12))

        botonDesc = tk.Button(self, text="Aplicar y guardar factura", command=self.guardarFactura)
        botonDesc.grid(row=18, column=0, padx=10, pady=(2, 12), sticky="w")

        tk.Label(self, text="Total Final:").grid(row=19, column=0, sticky="e", padx=(10, 2), pady=(2, 12))
        self.labelTotalFin = tk.Label(self, text="$0", font=fuenteTotal, fg="#1a7f37")
        self.labelTotalFin.grid(row=19, column=1, sticky="w", pady=(2, 12))

    #funcion para guardar info de factura con boton aceptar
    def aceptar(self):
        empleado = self.cajaEmpleado.get()
        cliente = self.cajaCliente.get()

        conex = conectar()
        cursor = conex.cursor()

        cursor.execute("SELECT id FROM empleados WHERE id = %s",(empleado,))
        existeEmpleado = cursor.fetchone()

        cursor.execute("SELECT id FROM clientes WHERE id = %s",(cliente,))
        existeCliente = cursor.fetchone()

        cursor.close()
        conex.close()

        if existeEmpleado is None:
            messagebox.showerror(
                "Error",
                "No existe un empleado con ese ID."
            )
            return

        if existeCliente is None:
            messagebox.showerror(
                "Error",
                "No existe un cliente con ese ID."
            )
            return

        self.idEmpleado = empleado
        self.idCliente = cliente

        # insertar info de factura
        self.labelEmpleado.config(text=f"{empleado}")
        self.labelCliente.config(text=f"{cliente}")

    #funcion para guardar facturacion de productos en tabla con boton insertar
    def insertar(self):
        stock = self.cajaStock.get()
        cant = int(self.cajaCant.get())
        descuento = float(self.cajaDesc.get())

        # Buscar producto en MySQL
        conex = conectar()
        cursor = conex.cursor()

        sql = """SELECT descripcion, precio, cantidad
              FROM stock
              WHERE id = %s """

        cursor.execute(sql, (stock,))
        producto = cursor.fetchone()

        cursor.close()
        conex.close()

        # Verificar que exista
        if producto is None:
            messagebox.showerror(
                "Error",
                "No existe un producto con ese Id Stock."
            )
            return

        descripcion = producto[0]
        valor = float(producto[1])
        stockDisponible = int(producto[2])

        if cant > stockDisponible:
            messagebox.showerror("Stock insuficiente",f"Solo hay {stockDisponible} unidades disponibles."
            )
            return

        # Calcular total del producto
        total = (cant * valor) * ((100 - descuento) / 100)

        # Insertar en la tabla visual
        self.tabla.insert(
            "",
            "end",
            values=(stock,descripcion,cant, f"{valor:.2f}",f"{descuento:.2f}",f"{total:.2f}" ))

        # Actualizar subtotal
        self.subtotal += total
        self.labelSub.config(text=f"${self.subtotal:.2f}")

        self.limpiar_cajas()

    #Función para aplicar descuento a subtotal
    def guardarFactura(self):
        # Comprobar que empleado y cliente fueron aceptados
        if self.idEmpleado is None or self.idCliente is None:
            messagebox.showerror(
                "Error",
                "Primero validar empleado y cliente."
            )
            return

        # Comprobar que haya productos
        if not self.tabla.get_children():
            messagebox.showerror(
                "Error",
                "La factura no tiene productos."
            )
            return

        subDesc= float(self.cajaSubDesc.get())
        totalFin= self.subtotal * ((100-subDesc)/100)

        conex = conectar()
        cursor = conex.cursor()

        try:

            #guardar factura
            sqlFactura = """
                         INSERT INTO facturas (id_empleado, id_cliente, fecha, subtotal, descuento, total)
                         VALUES (%s, %s, %s, %s, %s, %s) """

            datosFactura = (
                self.idEmpleado,
                self.idCliente,
                self.fecha,
                self.subtotal,
                subDesc,
                totalFin
            )

            cursor.execute(sqlFactura, datosFactura)

            # ID REAL generado por MySQL
            idFactura = cursor.lastrowid

            #guardar detalles
            for fila in self.tabla.get_children():

                valores = self.tabla.item(fila, "values")

                idStock = valores[0]
                cantidad = int(valores[2])
                valorUnitario = float(valores[3])
                descuento = float(valores[4])
                total = float(valores[5])

                # comprobar stock actual
                cursor.execute(
                    """SELECT cantidad FROM stock
                    WHERE id = %s""",(idStock,))

                resultadoStock = cursor.fetchone()

                if resultadoStock is None:
                    raise Exception(
                        f"El producto {idStock} ya no existe."
                    )

                cantidadDisponible = int(resultadoStock[0])

                if cantidad > cantidadDisponible:
                    raise Exception(
                        f"Stock insuficiente para el producto {idStock}. "
                        f"Disponible: {cantidadDisponible}")

                # guardar detalle
                sqlDetalle = """INSERT INTO detalle_factura(id_factura, id_stock, cantidad,valor_unitario, descuento, total)
                             VALUES (%s, %s, %s, %s, %s, %s) """

                datosDetalle = (idFactura, idStock, cantidad, valorUnitario, descuento, total)

                cursor.execute(sqlDetalle, datosDetalle)

                # descontar stock
                cursor.execute(
                    """UPDATE stock SET cantidad = cantidad - %s
                    WHERE id = %s """,(cantidad, idStock))

            # Si absolutamente todo salió bien:
            conex.commit()

            self.labelFactura.config(text=idFactura)
            self.labelTotalFin.config(text=f"${totalFin:.2f}")

            messagebox.showinfo(
                "Factura guardada",f"Factura {idFactura} guardada correctamente.")

            self.limpiar_factura()

        except Exception as error:

            # Deshacer factura, detalles y cambios de stock
            conex.rollback()
            messagebox.showerror(
                "Error",
                f"No se pudo guardar la factura:\n{error}")

        finally:
            cursor.close()
            conex.close()

    #funcion para seleccionar fila en tabla y que cambien los valores de las cajas
    def seleccionar(self, event):
        seleccion=self.tabla.selection()
        if not seleccion:
            return

        fila=seleccion[0]
        valores=self.tabla.item(fila,"values")

        self.limpiar_cajas()

        self.cajaStock.insert(0,valores[0])
        self.cajaCant.insert(0,valores[2])
        self.cajaDesc.insert(0,valores[4])

    #funcion para modificar fila en tabla
    def modificar(self):
        seleccion=self.tabla.selection()

        if not seleccion:
            return

        fila=seleccion[0]

        # volver a calcular subtotal (restar lo que estaba antes)
        self.restarSubtotal(fila)

        #insertar en la tabla nuevas modificaciones
        stock = self.cajaStock.get()
        cant = int(self.cajaCant.get())
        descuento = float(self.cajaDesc.get())

        # Buscar nuevamente producto y precio
        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
            """SELECT descripcion, precio FROM stock
            WHERE id = %s""",(stock,))

        producto = cursor.fetchone()

        cursor.close()
        conex.close()

        if producto is None:
            messagebox.showerror(
                "Error",
                "No existe un producto con ese Id Stock."
            )
            return

        descripcion = producto[0]
        valor = float(producto[1])

        total = (cant * valor) * ((100 - descuento) / 100)

        self.tabla.item(fila,values=(stock, descripcion, cant, f"{valor:.2f}", f"{descuento:.2f}", f"{total:.2f}"))

        self.sumarSubtotal(fila)
        self.limpiar_cajas()

    #funcion para eliminar fila en tabla
    def eliminar(self):
        seleccion=self.tabla.selection()

        if not seleccion:
            return

        fila = seleccion[0]

        # volver a calcular subtotal (restar lo que estaba antes)
        self.restarSubtotal(fila)

        for fila in seleccion:
            self.tabla.delete(fila)

        # limpiar las cajas después de eliminar
        self.limpiar_cajas()


    #funcion para restar en el subtotal
    def restarSubtotal(self, fila):
        valores = self.tabla.item(fila, "values")
        self.subtotal -= float(valores[5])
        self.labelSub.config(text=f"{self.subtotal:.2f}")

    # funcion para sumar en el subtotal
    def sumarSubtotal(self, fila):
        valores = self.tabla.item(fila, "values")
        self.subtotal += float(valores[5])
        self.labelSub.config(text=f"{self.subtotal:.2f}")

    #funcion para limpiar las cajas de producto (no toca factura/empleado/cliente)
    def limpiar_cajas(self):
        self.cajaStock.delete(0, tk.END)
        self.cajaCant.delete(0, tk.END)
        self.cajaDesc.delete(0, tk.END)

    def obtenerProximoIdFactura(self):
        conex = conectar()
        cursor = conex.cursor()

        cursor.execute(
            "SELECT COALESCE(MAX(id), 0) + 1 FROM facturas"
        )

        proximoId = cursor.fetchone()[0]

        cursor.close()
        conex.close()

        return proximoId

    def limpiar_factura(self):
        # Limpiar cajas de empleado y cliente
        self.cajaEmpleado.delete(0, tk.END)
        self.cajaCliente.delete(0, tk.END)

        # Limpiar cajas del producto
        self.limpiar_cajas()

        # Limpiar descuento general
        self.cajaSubDesc.delete(0, tk.END)

        # Limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Reiniciar subtotal
        self.subtotal = 0
        self.labelSub.config(text="$0.00")

        # Reiniciar total final
        self.labelTotalFin.config(text="$0.00")

        # Reiniciar datos de empleado y cliente
        self.idEmpleado = None
        self.idCliente = None

        self.labelEmpleado.config(text="-")
        self.labelCliente.config(text="-")

        # Nueva fecha para la próxima factura
        self.fecha = datetime.now()
        self.labelFecha.config(
            text=f"{self.fecha:%d/%m/%Y %H:%M}"
        )

        # Mostrar próximo número de factura
        self.labelFactura.config(
            text=self.obtenerProximoIdFactura()
        )