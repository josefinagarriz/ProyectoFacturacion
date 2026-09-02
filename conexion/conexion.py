import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="wilson",
        database="almacen"
    )

    return conexion

conexion = conectar()

#para ver si funciona :)
#if conexion.is_connected():
    #print("Conexión exitosa")