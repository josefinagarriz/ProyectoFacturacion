import tkinter as tk

def crear_menu(ventana, ventana_actual=None, fila=0, nivel_usuario=None):
    #Agrega el menú de botones de navegación a cualquier ventana (Tk o Toplevel).

    #botones fijos que se muestran para todos los usuarios
    botones = [
        ("Clientes", abrir_clientes),
        ("Stock", abrir_stock),
        ("Facturas", abrir_facturas),
        ("Facturación", abrir_facturacion),
    ]

    #botones solo para admin y gerente
    if nivel_usuario in ("admin", "gerente"):
        botones.extend([
            ("Empleados", abrir_empleados),
            ("Proveedores", abrir_proveedor),
            ("Entradas", abrir_entradas),
        ])

    #boton solo para admin
    if nivel_usuario == "admin":
        botones.extend([
            ("Gerentes", abrir_gerentes),
            ("Usuarios", abrir_usuarios),
        ])

    # Organizar los botones en filas de 4
    columnas = 4

    for i, (texto, funcion) in enumerate(botones):
        fila_boton = fila + i // columnas
        columna_boton = i % columnas

        boton = tk.Button(
            ventana,
            text=texto,
            width=12,
            bg="white",
            activebackground="#e6e6e6",
            command=lambda f=funcion, v=ventana, n=nivel_usuario: f(v, n)
        )

        if texto == ventana_actual:
            boton.config(state="disabled")

        boton.grid(
            row=fila_boton,
            column=columna_boton,
            padx=10,
            pady=5,
            sticky="ew"
        )

        # Hacer que las 4 columnas tengan el mismo espacio
    for columna in range(columnas):
        ventana.grid_columnconfigure(columna, weight=1)


#funciones para abrir cada ventana
def abrir_empleados(parent, nivel_usuario):
    from ventana_empleados import VentanaEmpleados
    VentanaEmpleados(parent, nivel_usuario)

def abrir_clientes(parent, nivel_usuario):
    from ventana_clientes import VentanaClientes
    VentanaClientes(parent, nivel_usuario)

def abrir_stock(parent, nivel_usuario):
    from ventana_stock import VentanaStock
    VentanaStock(parent, nivel_usuario)

def abrir_proveedor(parent, nivel_usuario):
    from ventana_proveedores import VentanaProveedores
    VentanaProveedores(parent, nivel_usuario)

def abrir_facturas(parent, nivel_usuario):
    from ventana_facturas import VentanaFacturas
    VentanaFacturas(parent, nivel_usuario)

def abrir_facturacion(parent, nivel_usuario):
    from ventana_facturacion import VentanaFacturacion
    VentanaFacturacion(parent, nivel_usuario)

def abrir_gerentes(parent, nivel_usuario):
    from ventana_gerentes import VentanaGerentes
    VentanaGerentes(parent, nivel_usuario)

def abrir_usuarios(parent, nivel_usuario):
    from ventana_usuarios import VentanaUsuarios
    VentanaUsuarios(parent, nivel_usuario)

def abrir_entradas(parent, nivel_usuario):
    from ventana_entradas import VentanaEntradas
    VentanaEntradas(parent, nivel_usuario)