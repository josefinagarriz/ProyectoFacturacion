import tkinter as tk
from tkinter import ttk, messagebox
from base.ventana_base import crear_menu
from conexion.conexion import *
from subventanas.ventana_usuario_mails import VentanaUsuarioMails
from subventanas.ventana_usuario_redes import VentanaUsuarioRedes
from subventanas.ventana_usuario_telefonos import VentanaUsuarioTelefonos
from subventanas.ventana_usuario_ubicaciones import VentanaUsuarioUbicaciones

class VentanaClientes(tk.Toplevel):
    def __init__(self, parent, nivel_usuario):
        super().__init__(parent)
        self.title("Clientes")
        self.geometry("1200x650")

        # fuente reutilizable para dar jerarquía visual
        fuenteTitulo = ("Segoe UI",10, "bold")

        # Frame principal centrado
        self.configure(background="lightgreen")

        self.framePrincipal = tk.Frame(self, background="lightblue",relief="ridge",bd=4,padx=20,pady=15)
        self.framePrincipal.place(relx=0.5,rely=0.5,anchor="center")

        # Título
        tk.Label(self.framePrincipal,text="CLIENTES",font=fuenteTitulo,background="lightblue").grid(row=0, column=0, columnspan=4, pady=(0, 15))

        # Botones de cliente
        if nivel_usuario in ("admin", "gerente"):
            #Campos de formulario cliente
            tk.Label(self.framePrincipal, text="-Cliente selccionadao:", font=fuenteTitulo, background="lightblue").grid(row=2, column=0, columnspan=4, sticky="w", pady=(5, 10))

            tk.Label(self.framePrincipal, text="Nombre", background="lightblue").grid(row=3, column=0, padx=5, pady=5, sticky="e")
            self.cajaNombre = tk.Entry(self.framePrincipal, width=22)
            self.cajaNombre.grid(row=3, column=1, padx=5, pady=5)

            tk.Label(self.framePrincipal, text="Razón social", background="lightblue").grid(row=3, column=2, padx=5, pady=5, sticky="e")
            self.cajaRazon = tk.Entry(self.framePrincipal, width=22)
            self.cajaRazon.grid(row=3, column=3, padx=5, pady=5)

            tk.Label(self.framePrincipal, text="CUIT", background="lightblue").grid(row=4, column=0, padx=5, pady=5, sticky="e")
            self.cajaCUIT = tk.Entry(self.framePrincipal, width=22)
            self.cajaCUIT.grid(row=4, column=1, padx=5, pady=5)

            tk.Label(self.framePrincipal, text="Página web", background="lightblue").grid(row=4, column=2, padx=5, pady=5, sticky="e")
            self.cajaWeb = tk.Entry(self.framePrincipal, width=22)
            self.cajaWeb.grid(row=4, column=3, padx=5, pady=5)

            frameBotones = tk.Frame(self.framePrincipal, background="lightblue")
            frameBotones.grid(row=5, column=0, columnspan=4, pady=12)

            botonInsertar = tk.Button(frameBotones, text="Insertar", background="white", width=12, command=self.insertar)
            botonInsertar.grid(row=0, column=0, padx=8)

            botonModificar = tk.Button(frameBotones, text="Modificar", background="white", width=12, command=self.modificar)
            botonModificar.grid(row=0, column=1, padx=8)

            botonEliminar = tk.Button(frameBotones, text="Eliminar", background="white", width=12, command=self.eliminar)
            botonEliminar.grid(row=0, column=2, padx=8)

        # separador
        ttk.Separator(self.framePrincipal, orient="horizontal").grid(row=6, column=0, columnspan=4, sticky="ew", pady=10)

        # tabla de clientes
        tk.Label(self.framePrincipal, text="-Tabla de clientes:", font=fuenteTitulo, background="lightblue").grid(row=7, column=0, columnspan=4, sticky="w", pady=(0, 5))




        columnas = ("Id", "Nombre", "Razón social", "CUIT", "Página web", "Compras", "Mails", "Redes", "Teléfonos", "Ubicaciones")
        self.tabla = ttk.Treeview(self.framePrincipal, columns=columnas, show="headings", height=10)
        anchos = {"Id": 45, "Nombre": 120, "Razón social": 140, "CUIT": 100, "Página web": 140,"Compras": 65, "Mails": 90,"Redes": 90, "Teléfonos": 100,"Ubicaciones": 110 }
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=anchos[col], anchor="center")
        self.tabla.grid(row=8, column=0, columnspan=4,padx=5, pady=5)

        # Doble clic en una celda para ver sus detalles
        self.tabla.bind("<Double-1>",self.ver_detalles)

        # Para que al seleccionar una fila, su info aparezca en las cajas
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar_tabla()  # para que al abrir la ventana, aparezca lo que ya está en la tabla


    # Carga solamente clientes y usuarios habilitados
    def cargar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        conex = conectar()
        cursor = conex.cursor()

        sql = """
                SELECT
                    c.id,
                    c.nombre,
                    c.razon_social,
                    c.cuit,
                    c.pagina_web,
                    c.compras,
                    (
                        SELECT COUNT(*)
                        FROM usuarios_mails um
                        WHERE um.id_usuario = c.id_usuario
                          AND um.habilitado = 1
                    ) AS cantidad_mails,
                    (
                        SELECT COUNT(*)
                        FROM usuarios_redes ur
                        WHERE ur.id_usuario = c.id_usuario
                          AND ur.habilitado = 1
                    ) AS cantidad_redes,
                    (
                        SELECT COUNT(*)
                        FROM usuarios_telefonos ut
                        WHERE ut.id_usuario = c.id_usuario
                          AND ut.habilitado = 1
                    ) AS cantidad_telefonos,
                    (
                        SELECT COUNT(*)
                        FROM usuarios_ubicaciones uu
                        WHERE uu.id_usuario = c.id_usuario
                          AND uu.habilitado = 1
                    ) AS cantidad_ubicaciones
                FROM clientes c
                INNER JOIN usuarios u
                    ON u.id = c.id_usuario
                WHERE c.habilitado = 1
                  AND u.habilitado = 1
                ORDER BY c.id
            """
        try:
            cursor.execute(sql)
            registros = cursor.fetchall()

            for registro in registros:
                valores = list(registro)

                # Convertir cantidades en textos más claros
                valores[6] = f"{valores[6]} mail(s) ▾"
                valores[7] = f"{valores[7]} red(es) ▾"
                valores[8] = f"{valores[8]} teléfono(s) ▾"
                valores[9] = f"{valores[9]} ubicación(es) ▾"

                self.tabla.insert("", "end", values=valores)

        except Exception as e:
            messagebox.showerror("Error",f"No se pudieron cargar los clientes:\n{e}")

        finally:
            cursor.close()
            conex.close()

    # Muestra los datos del cliente seleccionado en las cajas
    def seleccionar(self, event):

        seleccion = self.tabla.selection()
        if not seleccion:
            return

        valores = self.tabla.item(seleccion[0], "values")

        self.limpiar_cajas()
        self.cajaNombre.insert(0, valores[1])
        self.cajaRazon.insert(0, valores[2])
        self.cajaCUIT.insert(0, valores[3])
        self.cajaWeb.insert(0, valores[4])

    # Abre los detalles al hacer doble clic en una celda
    def ver_detalles(self, event):

        fila = self.tabla.identify_row(event.y)
        columna = self.tabla.identify_column(event.x)

        if not fila:
            return

        valores = self.tabla.item(fila, "values")
        id_cliente = valores[0]

        conex = conectar()
        cursor = conex.cursor()

        try:
            cursor.execute(
                """
                SELECT id_usuario
                FROM clientes
                WHERE id = %s
                """,
                (id_cliente,)
            )

            resultado = cursor.fetchone()

            if resultado is None:
                return

            id_usuario = resultado[0]

        finally:
            cursor.close()
            conex.close()

        # Abrir la subventana correspondiente
        if columna == "#7":
            VentanaUsuarioMails(self, id_usuario)

        elif columna == "#8":
            VentanaUsuarioRedes(self, id_usuario)

        elif columna == "#9":
            VentanaUsuarioTelefonos(self, id_usuario)

        elif columna == "#10":
            VentanaUsuarioUbicaciones(self, id_usuario)

    # Limpia los campos del formulario
    def limpiar_cajas(self):
        self.cajaNombre.delete(0, tk.END)
        self.cajaRazon.delete(0, tk.END)
        self.cajaCUIT.delete(0, tk.END)
        self.cajaWeb.delete(0, tk.END)

    #funcion para guardar clientes en tabla con boton insertar
    def insertar(self):
        conex = conectar()
        cursor = conex.cursor()
        sql = """INSERT INTO clientes(nombre, apellido, dni, razon_social, ciudad, provincia, telefono, codigo_postal, email)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        valores = (
            self.cajaNombre.get(),
            self.cajaApellido.get(),
            self.cajaDNI.get(),
            self.cajaRazon.get(),
            self.cajaCiudad.get(),
            self.cajaProv.get(),
            self.cajaTelef.get(),
            self.cajaCodpost.get(),
            self.cajaEmail.get()
        )

        cursor.execute(sql, valores)
        conex.commit()

        cursor.close()
        conex.close()

        # insertar nueva fila en tabla
        self.cargar_tabla()

        # limpiar las cajas después de insertar
        self.limpiar_cajas()


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

        sql = """UPDATE clientes SET nombre = %s, apellido = %s, dni = %s, razon_social = %s, ciudad = %s, provincia = %s, telefono = %s, codigo_postal = %s, email = %s
                 WHERE id = %s """

        datos = (
            self.cajaNombre.get(),
            self.cajaApellido.get(),
            self.cajaDNI.get(),
            self.cajaRazon.get(),
            self.cajaCiudad.get(),
            self.cajaProv.get(),
            self.cajaTelef.get(),
            self.cajaCodpost.get(),
            self.cajaEmail.get(),
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
        sql = """DELETE FROM clientes
                 WHERE id = %s """

        cursor.execute(sql, (id,))
        conex.commit()
        cursor.close()
        conex.close()
        self.cargar_tabla()

        # limpiar las cajas después de eliminar
        self.limpiar_cajas()





