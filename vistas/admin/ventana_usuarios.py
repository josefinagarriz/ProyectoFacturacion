import tkinter as tk
from tkinter import ttk
from ventana_base import crear_menu
from conexion.conexion import *
from admin.ventana_datos_usuario import VentanaDatosUsuario


class VentanaUsuarios(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Usuarios")
        self.geometry("1050x550")

        # Botones de menú
        crear_menu(self, ventana_actual="Usuarios", nivel_usuario=nivel_usuario)

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")

        # Campos del formulario usuario
        tk.Label(self, text="-Inserte información sobre usuario:", font=fuenteTitulo).grid(row=2, column=0,
                                                                                           columnspan=4, sticky="w",
                                                                                           padx=10, pady=(12, 4))

        tk.Label(self, text="Nombre de perfil").grid(row=3, column=0, sticky="w", padx=(10, 2), pady=3)
        self.cajaNombre = tk.Entry(self, width=18)
        self.cajaNombre.grid(row=3, column=1, sticky="w", pady=3)

        tk.Label(self, text="Contraseña").grid(row=3, column=2, sticky="w", padx=(15, 2), pady=3)
        self.cajaContra = tk.Entry(self, width=18)
        self.cajaContra.grid(row=3, column=3, sticky="w", pady=3)

        tk.Label(self, text="Nivel").grid(row=3, column=4, sticky="w", padx=(15, 2), pady=3)
        # self.cajaNivel = tk.Entry(self, width=18)
        self.cajaNivel = ttk.Combobox(self, values=("admin", "gerente", "empleado"), state="readonly", width=18)
        self.cajaNivel.grid(row=3, column=5, sticky="w", pady=3)

        # Botones de usuario
        botonInsertar = tk.Button(self, text="Insertar", command=self.insertar)
        botonInsertar.grid(row=6, column=0, padx=15, pady=3, sticky="w")

        botonModificar = tk.Button(self, text="Modificar", command=self.modificar)
        botonModificar.grid(row=6, column=1, padx=15, pady=3, sticky="w")

        botonEliminar = tk.Button(self, text="Eliminar", command=self.eliminar)
        botonEliminar.grid(row=6, column=2, padx=15, pady=3, sticky="w")

        # separador
        ttk.Separator(self, orient="horizontal").grid(row=7, column=0, columnspan=7, sticky="ew", padx=10, pady=8)

        # tabla de usuarios
        tk.Label(self, text="-Tabla de Usuarios:", font=fuenteTitulo).grid(row=8, column=0, columnspan=4, sticky="w",
                                                                           padx=10, pady=(0, 4))

        columnas = ("Id usuario", "Nombre", "Contraseña", "Nivel")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100)
        self.tabla.grid(row=9, column=0, columnspan=7, padx=10, sticky="ew")

        # Para que al seleccionar una fila, su info aparezca en las cajas
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar_tabla()  # para que al abrir la ventana, aparezca lo que ya está en la tabla

    # funcion para guardar usuarios en tabla con boton insertar
    def insertar(self):
        nivel = self.cajaNivel.get()

        if not self.cajaNombre.get() or not self.cajaContra.get() or not nivel:
            return

        if nivel == "admin":
            conex = conectar()
            cursor = conex.cursor()
            sql = """INSERT INTO usuarios(usuario, password, nivel_usuario)
                     VALUES (%s, %s, %s)"""
            valores = (
                self.cajaNombre.get(),
                self.cajaContra.get(),
                nivel)
            cursor.execute(sql, valores)
            conex.commit()
            cursor.close()
            conex.close()

            self.cargar_tabla()
            self.limpiar_cajas()

        elif nivel == "empleado":
            VentanaDatosUsuario(self,self.cajaNombre.get(),self.cajaContra.get(),nivel)

        elif nivel == "gerente":
            VentanaDatosUsuario(self,self.cajaNombre.get(),self.cajaContra.get(),nivel)


    def cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        conex = conectar()
        cursor = conex.cursor()
        cursor.execute("""SELECT id, usuario, password, nivel_usuario
                          FROM usuarios""")
        registros = cursor.fetchall()
        for registro in registros:
            self.tabla.insert("", "end", values=registro)
        cursor.close()
        conex.close()

    # funcion para seleccionar fila en tabla
    def seleccionar(self, event):
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        fila = seleccion[0]
        valores = self.tabla.item(fila, "values")

        self.limpiar_cajas()

        self.cajaNombre.insert(0, valores[1])
        self.cajaContra.insert(0, valores[2])
        self.cajaNivel.insert(0, valores[3])

    # funcion para modificar fila en tabla
    def modificar(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            return

        fila = seleccion[0]

        valores = self.tabla.item(fila, "values")
        id = valores[0]
        conex = conectar()
        cursor = conex.cursor()

        sql = """UPDATE usuarios \
                 SET usuario       = %s, \
                     password      = %s
                 WHERE id = %s """

        datos = (
            self.cajaNombre.get(),
            self.cajaContra.get(),
            id
        )

        cursor.execute(sql, datos)

        conex.commit()
        cursor.close()
        conex.close()
        self.cargar_tabla()

        # limpiar las cajas después de modificar
        self.limpiar_cajas()

    # funcion para eliminar fila en tabla
    def eliminar(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            return

        fila = seleccion[0]
        valores = self.tabla.item(fila, "values")
        id_usuario = valores[0]

        conex = conectar()
        cursor = conex.cursor()

        try:
            #primero obtenemos el nivel del usuario
            sql_nivel = """SELECT nivel_usuario
                           FROM usuarios
                           WHERE id = %s"""

            cursor.execute(sql_nivel, (id_usuario,))
            resultado = cursor.fetchone()

            if resultado:
                nivel = resultado[0]

                #Si es empleado, eliminar sus datos
                if nivel == "empleado":
                    sql_empleado = """DELETE FROM empleados
                                      WHERE id_usuario = %s"""
                    cursor.execute(sql_empleado, (id_usuario,))

                #Si es gerente, eliminar sus datos
                elif nivel == "gerente":
                    sql_gerente = """DELETE FROM gerentes
                                     WHERE id_usuario = %s"""
                    cursor.execute(sql_gerente, (id_usuario,))

            #Finalmente eliminar el usuario
            sql_usuario = """DELETE FROM usuarios
                             WHERE id = %s"""

            cursor.execute(sql_usuario, (id_usuario,))
            conex.commit()

            self.cargar_tabla()
            self.limpiar_cajas()

        except Exception as e:
            conex.rollback()
            print("Error:", e)

        finally:
            cursor.close()
            conex.close()

    #funcion para limpiar cajas
    def limpiar_cajas(self):
        self.cajaNombre.delete(0, tk.END)
        self.cajaContra.delete(0, tk.END)
        self.cajaNivel.delete(0, tk.END)
