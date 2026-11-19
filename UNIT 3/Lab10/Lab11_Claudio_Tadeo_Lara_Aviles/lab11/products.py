# products.py
from exceptions import CantidadInvalida, StockInsuficiente

class Producto:
    def __init__(self, codigo: str, nombre: str, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    def retirar(self, cantidad: int) -> int:
        """
        Valida y descuenta stock del producto.
        - Lanza CantidadInvalida si la cantidad no es positiva.
        - Lanza StockInsuficiente si supera el stock actual.
        """
        # Validación: Verificar que la cantidad sea un entero positivo mayor a 0
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise CantidadInvalida(f"Error: La cantidad '{cantidad}' no es válida. Debe ser un entero positivo.")
        
        # Validación: Verificar que haya suficiente stock
        if cantidad > self.stock:
            raise StockInsuficiente(f"Error: Stock insuficiente. Stock actual: {self.stock}, solicitado: {cantidad}.")
        
        # Si pasa las validaciones, se descuenta la cantidad y se retorna el stock restante
        self.stock -= cantidad
        return self.stock