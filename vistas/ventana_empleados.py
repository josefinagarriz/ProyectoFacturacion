import tkinter as tk
from tkinter import ttk
from ventana_base import crear_menu
from conexion.conexion import *

class VentanaEmpleados(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Empleados")
        self.geometry("1050x550")

        #Botones de menú
        crear_menu(self, ventana_actual="Empleados", nivel_usuario=nivel_usuario)

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")

        #Campos del formulario empleados
        tk.Label(self, text="-Inserte información sobre empleado:", font=fuenteTitulo).grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=(12, 4))

        tk.Label(self, text="Nombre").grid(row=3, column=0, sticky="w", padx=(10, 2), pady=3)
        self.cajaNombre = tk.Entry(self, width=18)
        self.cajaNombre.grid(row=3, column=1, sticky="w", pady=3)

        tk.Label(self, text="Apellido").grid(row=3, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaApellido = tk.Entry(self, width=18)
        self.cajaApellido.grid(row=3, column=3, sticky="w", pady=3)

        tk.Label(self, text="DNI").grid(row=3, column=4, sticky="w", padx=(15, 2), pady=3)
        self.cajaDNI = tk.Entry(self, width=18)
        self.cajaDNI.grid(row=3, column=5, sticky="w", pady=3)

        tk.Label(self, text="Teléfono").grid(row=4, column=0, sticky="w", padx=(10, 2), pady=3)
        self.cajaTelef = tk.Entry(self, width=18)
        self.cajaTelef.grid(row=4, column=1, sticky="w", pady=3)

        tk.Label(self, text="Email").grid(row=4, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaEmail = tk.Entry(self, width=18)
        self.cajaEmail.grid(row=4, column=3, sticky="w", pady=3)

        tk.Label(self, text="Dirección").grid(row=4, column=4, sticky="w", padx=(15, 2), pady=3)
        self.cajaDire = tk.Entry(self, width=18)
        self.cajaDire.grid(row=4, column=5, sticky="w", pady=3)

        tk.Label(self, text="Edad").grid(row=5, column=0, sticky="w", padx=(10, 2), pady=3)
        self.cajaEdad = tk.Entry(self, width=18)
        self.cajaEdad.grid(row=5, column=1, sticky="w", pady=3)

        tk.Label(self, text="Departamento").grid(row=5, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaDep = tk.Entry(self, width=18)
        self.cajaDep.grid(row=5, column=3, sticky="w", pady=3)

        tk.Label(self, text="Sueldo $").grid(row=5, column=4, sticky="w", padx=(15, 2), pady=3)
        self.cajaSueldo = tk.Entry(self, width=18)
        self.cajaSueldo.grid(row=5, column=5, sticky="w", pady=3)

        #Botones de empleados
        botonInsertar = tk.Button(self, text="Insertar", command=self.insertar)
        botonInsertar.grid(row=6, column=0, padx=15, pady=3, sticky="w")

        botonModificar = tk.Button(self, text="Modificar", command=self.modificar)
        botonModificar.grid(row=6, column=1, padx=15, pady=3, sticky="w")

        botonEliminar = tk.Button(self, text="Eliminar", command=self.eliminar)
        botonEliminar.grid(row=6, column=2, padx=15, pady=3, sticky="w")

        #separador
        ttk.Separator(self, orient="horizontal").grid(row=7, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        #tabla de empleados
        tk.Label(self, text="-Tabla de empleados:", font=fuenteTitulo).grid(row=8, column=0, columnspan=4, sticky="w", padx=10, pady=(0, 4))

        columnas=("Id", "Nombre", "Apellido", "DNI", "Teléfono", "Email", "Dirección", "Edad", "Departamento", "Sueldo")
        self.tabla= ttk.Treeview(self, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)
        self.tabla.grid(row=9, column=0, columnspan=7, padx=10, sticky="ew")

        # Para que al seleccionar una fila, su info aparezca en las cajas
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar_tabla() #para que al abrir la ventana, aparezca lo que ya está en la tabla

    #funcion para guardar empleados en tabla con boton insertar
    def insertar(self):
        conex = conectar()
        cursor = conex.cursor()
        sql = """INSERT INTO empleados(nombre, apellido, dni, telefono, email, direccion, edad, departamento, sueldo)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        valores=(
            self.cajaNombre.get(),
            self.cajaApellido.get(),
            self.cajaDNI.get(),
            self.cajaTelef.get(),
            self.cajaEmail.get(),
            self.cajaDire.get(),
            int(self.cajaEdad.get()),
            self.cajaDep.get(),
            float(self.cajaSueldo.get())
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
        cursor.execute("""SELECT id,nombre,apellido,dni,telefono,email,direccion,edad,departamento,sueldo
                          FROM empleados""")
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

        self.cajaNombre.insert(0,valores[1])
        self.cajaApellido.insert(0,valores[2])
        self.cajaDNI.insert(0,valores[3])
        self.cajaTelef.insert(0,valores[4])
        self.cajaEmail.insert(0,valores[5])
        self.cajaDire.insert(0,valores[6])
        self.cajaEdad.insert(0,valores[7])
        self.cajaDep.insert(0,valores[8])
        self.cajaSueldo.insert(0, valores[9])

    #funcion para modificar fila en tabla
    def modificar(self):
        seleccion=self.tabla.selection()

        if not seleccion:
            return

        fila=seleccion[0]

        valores = self.tabla.item(fila, "values")
        id= valores[0]
        conex = conectar()
        cursor = conex.cursor()

        sql = """UPDATE empleados SET nombre = %s, apellido = %s, dni = %s, telefono = %s, email = %s, direccion = %s, edad = %s, departamento = %s, sueldo = %s
                 WHERE id = %s """

        datos=(
        self.cajaNombre.get(),
        self.cajaApellido.get(),
        self.cajaDNI.get(),
        self.cajaTelef.get(),
        self.cajaEmail.get(),
        self.cajaDire.get(),
        self.cajaEdad.get(),
        self.cajaDep.get(),
        self.cajaSueldo.get(),
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
        seleccion=self.tabla.selection()

        if not seleccion:
            return

        fila = seleccion[0]
        valores = self.tabla.item(fila, "values")
        id = valores[0]
        conex = conectar()
        cursor = conex.cursor()
        sql = """DELETE FROM empleados
                 WHERE id = %s """

        cursor.execute(sql, (id,))
        conex.commit()
        cursor.close()
        conex.close()
        self.cargar_tabla()

        # limpiar las cajas después de eliminar
        self.limpiar_cajas()

    # funcion para limpiar cajas
    def limpiar_cajas(self):
        self.cajaNombre.delete(0, tk.END)
        self.cajaApellido.delete(0, tk.END)
        self.cajaDNI.delete(0, tk.END)
        self.cajaTelef.delete(0, tk.END)
        self.cajaEmail.delete(0, tk.END)
        self.cajaDire.delete(0, tk.END)
        self.cajaEdad.delete(0, tk.END)
        self.cajaDep.delete(0, tk.END)
        self.cajaSueldo.delete(0, tk.END)
