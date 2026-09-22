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
        botones.insert(0, ("Empleados", abrir_empleados))
        botones.insert(3, ("Proveedores", abrir_proveedor))

    #boton solo para admin
    if nivel_usuario == "admin":
        botones.append(("Gerentes", abrir_gerentes))
        botones.append(("Usuarios", abrir_usuarios))

    for columna, (texto, funcion) in enumerate(botones):
        if texto == ventana_actual:
            tk.Button(ventana, text=texto).grid(row=fila, column=columna, padx=5)
        else:
            tk.Button(ventana, text=texto, command=lambda f=funcion, v=ventana, n=nivel_usuario: f(v, n)).grid(row=fila, column=columna, padx=10)

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
    from vistas.admin.ventana_gerentes import VentanaGerentes
    VentanaGerentes(parent, nivel_usuario)

def abrir_usuarios(parent, nivel_usuario):
    from vistas.admin.ventana_usuarios import VentanaUsuarios
    VentanaUsuarios(parent, nivel_usuario)