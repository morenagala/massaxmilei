from flask import Flask, render_template
from crear_conexion import obtener_conexion

app = Flask(__name__)

@app.route('/')
@app.route('/<nombre_categoria>')
def categoria(nombre_categoria=None):
    conn = obtener_conexion()
    cursor = conn.cursor()

    # Obtener las categorías
    cursor.execute('SELECT * FROM todo ')
    articulos = cursor.fetchall()

    conn.close()

    return render_template('tabla.html', articulos=articulos,)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)