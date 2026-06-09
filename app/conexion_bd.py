# Configuración de la base de datos

DATABASE_URL = "sqlite:///clientes.db"



def obtener_conexion():
    return DATABASE_URL