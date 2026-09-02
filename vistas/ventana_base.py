import tkinter as tk

def crear_menu(ventana, ventana_actual=None, fila=0):
    #Agrega el menú de botones de navegación a cualquier ventana (Tk o Toplevel).

    botones = [
        ("Empleados", abrir_empleados),
        ("Clientes", abrir_clientes),
        ("Stock", abrir_stock),
        ("Proveedores", abrir_proveedor),
        ("Facturas", abrir_facturas),
        ("Facturación", abrir_facturacion),
    ]

    for columna, (texto, funcion) in enumerate(botones):
        if texto == ventana_actual:
            tk.Button(ventana, text=texto).grid(row=fila, column=columna, padx=10)
        else:
            tk.Button(ventana, text=texto, command=lambda f=funcion, v=ventana: f(v)).grid(row=fila, column=columna, padx=10)

#funciones para abrir cada ventana
def abrir_empleados(parent):
    from ventana_empleados import VentanaEmpleados
    VentanaEmpleados(parent)

def abrir_clientes(parent):
    from ventana_clientes import VentanaClientes
    VentanaClientes(parent)

def abrir_stock(parent):
    from ventana_stock import VentanaStock
    VentanaStock(parent)

def abrir_proveedor(parent):
    from ventana_proveedores import VentanaProveedores
    VentanaProveedores(parent)

def abrir_facturas(parent):
    from ventana_facturas import VentanaFacturas
    VentanaFacturas(parent)

def abrir_facturacion(parent):
    from ventana_facturacion import VentanaFacturacion
    VentanaFacturacion(parent)