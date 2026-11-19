# exceptions.py
# Mantiene las excepciones personalizadas para el sistema de inventario

class ErrorInventario(Exception):
    """Clase base para todos los errores relacionados con el inventario."""
    pass


class ProductoNoEncontrado(ErrorInventario):
    """Se lanza cuando el código de producto no existe en el inventario."""
    pass


class CantidadInvalida(ErrorInventario):
    """Se lanza cuando la cantidad ingresada es cero, negativa o no válida."""
    pass


class StockInsuficiente(ErrorInventario):
    """Se lanza cuando la cantidad solicitada supera el stock disponible."""
    pass