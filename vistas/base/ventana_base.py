import tkinter as tk

def crear_menu(ventana, ventana_actual=None, fila=0, nivel_usuario=None):
    #Agrega el menú de botones de navegación a cualquier ventana (Tk o Toplevel).

    """
    1: empleado
    2: gerente
    3: admin
    4: cliente
    5: proveedor
    """

    #botones para todos
    botones = [
        ("Productos", abrir_productos)
    ]

    #botones para 1, 2 y 3
    if nivel_usuario in ("empleado","gerente", "admin"):
        botones.extend([
            ("Clientes", abrir_clientes)
        ])

    #botones para 2 y 3
    if nivel_usuario in ("gerente", "admin"):
        botones.extend([
            ("Comprar", abrir_comprar),
            ("Proveedores", abrir_proveedor),
            ("Logins", abrir_logins)
        ])

    #botones para 3
    if nivel_usuario == "admin":
        botones.extend([
            ("Admins", abrir_admins),
            ("Gestionar", abrir_gestionar)
        ])

    #botones para 1, 2, 3 y 4
    if nivel_usuario in ("empleado", "gerente", "admin","cliente"):
        if nivel_usuario == "cliente":
            botones.extend([
                ("Compras", abrir_ventas)
            ])
        else:
            botones.extend([
                ("Ventas", abrir_ventas)
            ])

    #botones para 1 y 3
    if nivel_usuario in ("empleado", "admin"):
        botones.extend([
            ("Vender", abrir_vender)
        ])

    #botones para 2, 3 y 5
    if nivel_usuario in ("gerente", "admin", "proveedor"):
        if nivel_usuario == "proveedor":
            botones.extend([
                ("Ventas", abrir_compras)
            ])
        else:
            botones.extend([
                ("Compras", abrir_compras)
            ])

    #botones para 2, 3 y 4
    if nivel_usuario in ("gerente", "admin", "cliente"):
        botones.extend([
            ("Empleados", abrir_empleados)
        ])

    #botones para 3 y 5
    if nivel_usuario in ("admin", "proveedor"):
        botones.extend([
            ("Gerentes", abrir_gerentes)
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
    from ventanas.ventana_empleados import VentanaEmpleados
    VentanaEmpleados(parent, nivel_usuario)

def abrir_clientes(parent, nivel_usuario):
    from ventanas.ventana_clientes import VentanaClientes
    VentanaClientes(parent, nivel_usuario)

def abrir_productos(parent, nivel_usuario):
    from ventanas.ventana_productos import VentanaProductos
    VentanaProductos(parent, nivel_usuario)

def abrir_proveedor(parent, nivel_usuario):
    from ventanas.ventana_proveedores import VentanaProveedores
    VentanaProveedores(parent, nivel_usuario)

def abrir_ventas(parent, nivel_usuario):
    from ventanas.ventana_ventas import VentanaVentas
    VentanaVentas(parent, nivel_usuario)

def abrir_vender(parent, nivel_usuario):
    from ventanas.ventana_vender import VentanaVender
    VentanaVender(parent, nivel_usuario)

def abrir_gerentes(parent, nivel_usuario):
    from ventanas.ventana_gerentes import VentanaGerentes
    VentanaGerentes(parent, nivel_usuario)

def abrir_admins(parent, nivel_usuario):
    from ventanas.ventana_admins import VentanaAdmins
    VentanaAdmins(parent, nivel_usuario)

def abrir_compras(parent, nivel_usuario):
    from ventanas.ventana_compras import VentanaCompras
    VentanaCompras(parent, nivel_usuario)

def abrir_logins(parent, nivel_usuario):
    from ventanas.ventana_logins import VentanaLogins
    VentanaLogins(parent, nivel_usuario)

def abrir_comprar(parent, nivel_usuario):
    from ventanas.ventana_comprar import VentanaComprar
    VentanaComprar(parent, nivel_usuario)

def abrir_gestionar(parent, nivel_usuario):
    from ventanas.ventana_gestionar import VentanaGestionar
    VentanaGestionar(parent, nivel_usuario)