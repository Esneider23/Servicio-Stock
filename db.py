# config.py
import psycopg2

config = {
    'dbname': 'citus',
    'user': 'citus',
    'password': 'klmdvklsnknskkfehwi2r3edvcdnowqch90b-au3chduiynicsh',
    'host': 'c-database-motorshop.jvspw4ebch4w4x.postgres.cosmos.azure.com',
    'port': '5432',
    'sslmode': 'require'
}

# Función para conectar a PostgreSQL
def get_db_connection():
    try:
        conn = psycopg2.connect(**config)
        print("Conexión exitosa a PostgreSQL")
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        return None