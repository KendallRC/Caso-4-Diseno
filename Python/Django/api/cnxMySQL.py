import mysql.connector
from mysql.connector import pooling

# Configuración del pool de conexiones
DATABASE_SETTINGS = {
    'host': 'localhost',
    'user': 'root',
    'password': 'l1ttl3K0d3r',
    'database': 'products',
    'raise_on_warnings': True,
}

# Crear el pool de conexiones
pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    **DATABASE_SETTINGS
)

def get_connection():
    return pool.get_connection()

def fetch_products_from_db(query):
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    finally:
        connection.close()
