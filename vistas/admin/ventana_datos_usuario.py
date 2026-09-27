import tkinter as tk
from tkinter import messagebox
from conexion.conexion import *

class VentanaDatosUsuario(tk.Toplevel):
    def __init__(self, parent, usuario, password, nivel_usuario):
        super().__init__(parent)
        self.title("Datos Usuario")
        self.geometry("1050x550")

        self.parent = parent

        self.usuario=usuario
        self.password = password
        self.nivel=nivel_usuario

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI", 10, "bold")

        #Campos del formulario empleados
        tk.Label(self, text="-Inserte información sobre nuevo usuario:", font=fuenteTitulo).grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=(12, 4))

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

    #funcion para guardar usuarios en tabla con boton insertar
    def insertar(self):
        conex = conectar()
        cursor = conex.cursor()

        try:

            #crear el usuario
            sql_usuario = """INSERT INTO usuarios(usuario, password, nivel_usuario)
                                 VALUES (%s, %s, %s)"""

            valores_usuario = (self.usuario,self.password,self.nivel)

            cursor.execute(sql_usuario, valores_usuario)

            #Obtener el id que MySQL acaba de generar
            id_usuario = cursor.lastrowid

            if self.nivel == "empleado":
                sql_empleado = """INSERT INTO empleados(nombre, apellido, dni, telefono, email, direccion, edad, departamento, sueldo, id_usuario)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                valores_empleado=(
                    self.cajaNombre.get(),
                    self.cajaApellido.get(),
                    self.cajaDNI.get(),
                    self.cajaTelef.get(),
                    self.cajaEmail.get(),
                    self.cajaDire.get(),
                    int(self.cajaEdad.get()),
                    self.cajaDep.get(),
                    float(self.cajaSueldo.get()),
                    id_usuario
                )

                cursor.execute(sql_empleado, valores_empleado)

            elif self.nivel == "gerente":
                sql_gerente = """INSERT INTO gerentes(nombre, apellido, dni, telefono, email, direccion, edad, departamento, sueldo, id_usuario)
                                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                valores_gerente = (
                    self.cajaNombre.get(),
                    self.cajaApellido.get(),
                    self.cajaDNI.get(),
                    self.cajaTelef.get(),
                    self.cajaEmail.get(),
                    self.cajaDire.get(),
                    int(self.cajaEdad.get()),
                    self.cajaDep.get(),
                    float(self.cajaSueldo.get()),
                    id_usuario
                )

                cursor.execute(sql_gerente, valores_gerente)

            conex.commit()

            self.parent.cargar_tabla()
            self.parent.limpiar_cajas()

            cursor.close()
            conex.close()

            self.destroy()

        except Exception as e:
            conex.rollback()
            cursor.close()
            conex.close()

            print("Error:", e)
