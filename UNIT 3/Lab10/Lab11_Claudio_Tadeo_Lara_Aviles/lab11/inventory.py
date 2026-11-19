# inventory.py
from products import Producto
from exceptions import ProductoNoEncontrado

class Inventario:
    def __init__(self):
        # Diccionario para almacenar productos usando su código como clave
        self.productos = {}

    def agregar_producto(self, producto: Producto):
        """Agrega un producto al inventario."""
        self.productos[producto.codigo] = producto

    def retirar(self, codigo: str, cantidad: int) -> int:
        """
        Busca el producto por código y delega el retiro.
        - Lanza ProductoNoEncontrado si el código no existe.
        - Permite que las excepciones de Producto (CantidadInvalida, StockInsuficiente) se propaguen.
        """
        # Validación: Verificar que el producto exista en el diccionario
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Error: El producto con código '{codigo}' no fue encontrado en el inventario.")
        
        # Llamada al método retirar del objeto Producto (las excepciones se propagan automáticamente)
        return self.productos[codigo].retirar(cantidad)