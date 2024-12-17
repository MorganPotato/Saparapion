import sqlite3

# Función para conectar a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('app/data/vacunacion.db')
    conn.row_factory = sqlite3.Row  # Para obtener resultados como diccionarios
    return conn
