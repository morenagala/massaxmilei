# crear_tabla.py
from crear_conexion import obtener_conexion

# Obtener la conexión
conn = obtener_conexion()
cursor = conn.cursor()

# Crear la tabla (si no existe)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS todo (
        id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
        nombre VARCHAR(255),
        descripcion VARCHAR(255),
        precio INT,
        categoria VARCHAR(255),
        seccion VARCHAR(255)

    )
''')

print("Tabla 'todo' creada o ya existe.")


# Cerrar la conexión
conn.commit()
cursor.close()
conn.close()