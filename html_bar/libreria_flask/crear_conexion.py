import mysql.connector
from mysql.connector import Error
 

def obtener_conexion():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="articulos_bar"
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos.")
        return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None