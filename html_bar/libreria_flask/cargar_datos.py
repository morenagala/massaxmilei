# insertar_datos.py
from crear_conexion import obtener_conexion

# Obtener la conexión
conn = obtener_conexion()
cursor = conn.cursor()

# Datos a insertar
registros = [
('Café jarrito', 'Café servido en jarrito', 500, 'cafeteria', ''),
('Café doble', 'Café con el doble de espresso', 590, 'cafeteria', ''),
('Lagrima jarrito', 'Café con leche servido en jarrito', 500, 'cafeteria', ''),
('Lagrima doble', 'Café con leche y doble de espresso', 590, 'cafeteria', ''),
('Café jarrito cortado', 'Café cortado servido en jarrito', 500, 'cafeteria', ''),
('Cortado', 'Café espresso con un toque de leche', 590, 'cafeteria', ''),
('Café con leche', 'Café con leche caliente', 590, 'cafeteria', ''),
('Capuchino', 'Café con leche y espuma de leche', 750, 'cafeteria', ''),
('Yogurth', 'Yogur con frutas y cereales', 740, 'cafeteria', ''),
('Té', 'Infusión de té caliente', 500, 'cafeteria', ''),
('Té con leche', 'Infusión de té con leche', 500, 'cafeteria', ''),
('Mate cocido', 'Infusión de mate cocido', 500, 'cafeteria', ''),
('Submarino', 'Leche caliente con trozos de chocolate', 750, 'cafeteria', ''),
('Vaso de leche', 'Leche caliente servida en vaso', 500, 'cafeteria', ''),
('Agua para termo', 'Agua en botella para termo', 150, 'cafeteria', ''),
('Madialuna', 'Medialuna de hojaldre', 240, 'pasteleria', ''),
('Brownie con merengue', 'Brownie cubierto con merengue', 780, 'pasteleria', ''),
('Alfajor tranvia', 'Alfajor de dulce de leche y cobertura de chocolate', 420, 'pasteleria', ''),
('Alfajor de almendras', 'Alfajor con dulce de leche y almendras', 590, 'pasteleria', ''),
('Muffin', 'Muffin de frutas o chocolate', 490, 'pasteleria', ''),
('Cookie integral', 'Galleta integral', 420, 'pasteleria', ''),
('Brownie integral', 'Brownie integral con chocolate', 500, 'pasteleria', ''),
('Pasta frola', 'Tarta de dulce de membrillo o batata', 420, 'pasteleria', ''),
('Rogel', 'Postre de dulce de leche con capas de masa', 780, 'pasteleria', ''),
('Lemon pie', 'Tarta de limón con merengue', 780, 'pasteleria', ''),
('Cheesecake', 'Tarta de queso con base de galleta', 780, 'pasteleria', ''),
('Chocopasion', 'Tarta de chocolate con frutas', 780, 'pasteleria', ''),
('Papas boutique', 'Papas fritas gourmet', 450, 'sin_tacc', 'sin_TACC'),
('Barra de ceral', 'Barra de cereal sin gluten', 290, 'sin_tacc', 'sin_TACC'),
('Barra de maní', 'Barra de maní sin gluten', 200, 'sin_tacc', 'sin_TACC'),
('Alfajor', 'Alfajor sin gluten relleno de dulce de leche', 420, 'sin_tacc', 'sin_TACC'),
('Cuadrado coco y ddl', 'Cuadrado de coco con dulce de leche', 690, 'sin_tacc', 'sin_TACC'),
('Cuadrado de brownie', 'Cuadrado de brownie sin gluten', 690, 'sin_tacc', 'sin_TACC'),
('Cuadrado de pasta frola', 'Cuadrado de pasta frola sin gluten', 690, 'sin_tacc', 'sin_TACC'),
('Ensalada de frutas', 'Ensalada con variedad de frutas frescas', 690, 'acompañamientos', ''),
('Tosatadas', 'Porción de tostadas con queso y mermelada', 690, 'acompañamientos', ''),
('Chips vegetales', 'Chips de vegetales crujientes', 390, 'acompañamientos', ''),
('Ensalada caesar con pollo', 'Mix de verdes, pollo y queso parmesano', 1290, 'ensaladas', ''),
('Ensalada saludable', 'Hummus, garbanzos, arroz yamaní, espinaca, zanahoria, pepino y repollo', 1290, 'ensaladas', ''),
('Ensalada del cheff', 'Mix de verdes, jamón, queso, huevo y tomates cherry', 1290, 'ensaladas', ''),
('Tosatado de miga', 'Tostada de pan miga con jamón y queso', 990, 'sanguches', ''),
('Sandwich de jamón y queso', 'Sándwich clásico de jamón y queso', 950, 'sanguches', 'arabe'),
('Sandwich de jamón crudo y queso', 'Sándwich con jamón crudo y queso', 1400, 'sanguches', 'pebete'),
('Sandwich de jamón y queso', 'Sándwich clásico de jamón y queso', 950, 'sanguches', 'pebete'),
('Sandwich de milanesa', 'Sándwich con milanesa de carne', 1400, 'sanguches', 'pebete'),
('Sandwich completo', 'Sándwich con jamón, queso, lechuga, tomate y mayonesa', 1550, 'sanguches', 'baguette'),
('Sandwich de jamón crudo', 'Sándwich con jamón crudo', 1400, 'sanguches', 'baguette'),
('Sandwich vegetariano', 'Sándwich con verduras y queso, sin carne', 990, 'sanguches', 'vegetariano'),
('Sandwich de pollo', 'Sándwich con pechuga de pollo', 1150, 'sanguches', ''),
('Sandwich vegano', 'Sándwich sin productos de origen animal', 990, 'sanguches', 'vegano'),
('Sandwich de salame y queso', 'Sándwich con salame y queso', 890, 'sanguches', 'pebete'),
('Croissant de jamón y queso', 'Croissant relleno de jamón y queso', 990, 'sanguches', ''),
('Wrap vegano', 'Wrap de vegetales y hummus', 1400, 'sanguches', 'vegano'),
('Wrap de pollo', 'Wrap de pollo con verduras', 1390, 'sanguches', ''),
('Tarta de verdura', 'Tarta de verduras variadas', 990, 'tartas', ''),
('Tarta de pollo', 'Tarta con pollo y vegetales', 990, 'tartas', ''),
('Tarta de calabaza', 'Tarta de calabaza con masa crocante', 990, 'tartas', ''),
('Tarta de jamón y queso', 'Tarta con jamón y queso', 990, 'tartas', ''),
('Tarta de espinaca', 'Tarta de espinaca y queso', 990, 'tartas', ''),
('Pizza muzzarella', 'Pizza individual de muzzarella', 1190, 'empanadas_pizzas', ''),
('Pizza cherry y albahaca', 'Pizza individual de cherry y albahaca', 1190, 'empanadas_pizzas', ''),
('Empanada de jamón y queso', 'Empanada rellena de jamón y queso', 320, 'empanadas_pizzas', ''),
('Empanada de pollo', 'Empanada rellena de pollo', 320, 'empanadas_pizzas', ''),
('Empanada de carne', 'Empanada rellena de carne', 320, 'empanadas_pizzas', ''),
('Agua con o sin gas', 'Agua mineral con o sin gas', 420, 'bebidas', ''),
('Agua saborizada', 'Agua con sabor a frutas', 420, 'bebidas', ''),
('Pepsi', 'Lata 473ml de Pepsi', 480, 'bebidas', ''),
('Pepsi light', 'Lata 473ml de Pepsi Light', 480, 'bebidas', ''),
('7up', 'Lata 473ml de 7up', 480, 'bebidas', ''),
('7up light', 'Lata 473ml de 7up Light', 480, 'bebidas', ''),
('Mirinda', 'Lata 473ml de Mirinda', 480, 'bebidas', ''),
('Pomelo', 'Lata 269ml de jugo de pomelo', 480, 'bebidas', ''),
('Tónica', 'Lata 269ml de agua tónica', 480, 'bebidas', ''),
('Jugo de naranja (Citric)', 'Jugo de naranja natural Citric', 500, 'bebidas', ''),
('Jugo Beepure', 'Jugo Beepure 330ml', 500, 'bebidas', ''),
('Jugo Estancias', 'Jugo Estancias 500ml', 500, 'bebidas', ''),
('Cerveza Quilmes', 'Lata 473cc de Cerveza Quilmes', 690, 'bebidas', ''),
('Cerveza Quilmes', 'Porron 330cc de Cerveza Quilmes', 630, 'bebidas', ''),
('Cerveza Stella Artois', 'Porron 330cc de Cerveza Stella Artois', 850, 'bebidas', ''),
('Cerveza Stella Artois', 'Lata 473ml de Cerveza Stella Artois', 850, 'bebidas', ''),
('Cerveza Corona', 'Porron 350cc de Cerveza Corona', 890, 'bebidas', ''),
('Cerveza Patagonia', 'Porron de Cerveza Patagonia', 850, 'bebidas', ''),
('Cerveza Patagonia', 'Lata de Cerveza Patagonia', 850, 'bebidas', ''),
('Cerveza Brahama', 'Lata de Cerveza Brahama', 590, 'bebidas', ''),
('Chandon XB', 'Botella de Chandon XB 187ml', 1200, 'bebidas', ''),
('Energizante', 'Bebida energizante', 550, 'bebidas', ''),
('Ramo estación', 'Ramo de flores estación', 2000, 'flores', ''),
('Bousquet', 'Una (1) rosa de Bousquet', 1400, 'flores', ''),
('Globo corazón', 'Globo con forma de corazón', 1000, 'flores', ''),
('Globo I Love You', 'Globo con mensaje I Love You', 1300, 'flores', '')
]



# Insertar los datos
cursor.executemany('''
    INSERT INTO todo (nombre, descripcion, precio, categoria, seccion)
    VALUES (%s, %s, %s, %s, %s)
''', registros)

print(f"Se han insertado {cursor.rowcount} registros en la tabla 'todo'.")



# Guardar los cambios y cerrar la conexión
conn.commit()
cursor.close()
conn.close()