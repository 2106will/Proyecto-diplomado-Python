import sqlite3

def conectar():
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, year INTEGER, isbn INTEGER)")
    conexion.commit()
    conexion.close()
def insertar(titulo, autor, year, isbn):
    conexion = sqlite3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("""
                      INSERT INTO libros VALUES (NULL, ?, ?, ?, ?)      
                            """, (titulo, autor, year, isbn))
    conexion.commit()
    conexion.close()    

def visualizar():
    conexion = sqlite3.connect("libros.db")   
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros") 
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def buscar(titulo='', autor='', year=0, isbn=0):
    conexion = sqlite3.connect("libros.db")   
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros WHERE titulo=? OR autor=? OR year=? OR isbn =?", (titulo, autor, year, isbn))
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def borrar(id):
    conexion = sqlite3.connect("libros.db")   
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?", (id,))
    conexion.commit()
    conexion.close()

def actualizar(titulo, autor, year, isbn, id):
    conexion = sqlite3.connect("libros.db")   
    cursor = conexion.cursor()
    cursor.execute("UPDATE libros SET titulo=?, autor=?, year=?, isbn =? WHERE id =?", (titulo, autor, year, isbn,id))
    conexion.commit()
    conexion.close()

#pruebas

conectar()
# insertar("El señor de los anillos", "RR Martin", 1998, 123465798)
# insertar("Juego de tronos", "RR Martin", 1908, 54654568)
# insertar("Harry Potter", "Lucas film", 1900, 12378)
# resultados = visualizar()
# for resultado in resultados:
#     print(resultado)

# resultados = buscar(titulo ='El señor de los anillos')
# for resultado in resultados:
#     print(resultado)

# borrar(1)
# resultados = visualizar()
# for resultado in resultados:
#     print(resultado)

# actualizar(titulo="El principito", autor="Wilder kmargo", year=2021, isbn=123465789, id=3)
# resultados = visualizar()
# for resultado in resultados:
#     print(resultado)