import mysql.connector
from controllers.conexion import Database_connection

class ProductModel:
    def __init__(self):
        self.conexion_db = Database_connection()

    def obtener_productos(self):
    
        query = "SELECT id, nombre, precio FROM products"
        resultados = self.conexion_db.ejecutar_consulta(query)
        return resultados if resultados is not None else []