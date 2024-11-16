from flask import Flask, render_template
from crear_conexion import obtener_conexion

app = Flask(__name__)

@app.route('/')
@app.route('/<nombre_categoria>')
def categoria(nombre_categoria=None):
    # Obtener conexión a la base de datos
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Obtener todas las categorías
    cursor.execute('SELECT DISTINCT categoria FROM todo')
    categorias = cursor.fetchall()
    
    # Obtener los productos por categoría
    productos_por_categoria = {}
    for categoria in categorias:
        cursor.execute('SELECT * FROM todo WHERE categoria=%s', (categoria[0],))
        productos_por_categoria[categoria[0]] = cursor.fetchall()

    
    # Obtener productos de la categoría seleccionada
    productos_de_categoria = {}
    cursor.execute('SELECT * FROM todo WHERE categoria = %s', (nombre_categoria,))
    productos_de_categoria = cursor.fetchall()
    # Cerrar la conexión a la base de datos
    conn.close()

    # Renderizar la plantilla y pasarle los datos
    return render_template('index.html', 
                           categorias=categorias, 
                           productos_por_categoria=productos_por_categoria, 
                           nombre_categoria=nombre_categoria, 
                           productos_de_categoria=productos_de_categoria)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
