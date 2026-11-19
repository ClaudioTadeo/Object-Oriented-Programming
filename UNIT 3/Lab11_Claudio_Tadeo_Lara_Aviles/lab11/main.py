# main.py
from inventory import Inventario
from products import Producto
from exceptions import ErrorInventario

def main():
    # Inicializar el inventario y agregar productos adicionales (mínimo 3 en total)
    mi_inventario = Inventario()
    mi_inventario.agregar_producto(Producto("P001", "Laptop Gamer", 10))
    mi_inventario.agregar_producto(Producto("P002", "Teclado Mecánico", 25))
    mi_inventario.agregar_producto(Producto("P003", "Mouse Inalámbrico", 50))

    print("=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
    print("Productos disponibles: P001 (Laptop), P002 (Teclado), P003 (Mouse)")

    try:
        # Entrada de datos por el usuario
        codigo_ingresado = input("Ingrese el código del producto: ").strip()
        cantidad_ingresada = input("Ingrese la cantidad a retirar: ")

        # Intentar convertir la cantidad a entero (puede lanzar ValueError si ingresan texto)
        cantidad_int = int(cantidad_ingresada)

        # Realizar la operación de retiro en el inventario
        stock_restante = mi_inventario.retirar(codigo_ingresado, cantidad_int)

    except ValueError:
        # Captura el error si el usuario ingresa letras u otro valor no numérico
        print("\n[EXCEPCIÓN CAPTURADA]: ValueError -> Debe ingresar un número entero válido.")
        
    except ErrorInventario as e:
        # Captura cualquier excepción personalizada del inventario (ProductoNoEncontrado, CantidadInvalida, StockInsuficiente)
        print(f"\n[EXCEPCIÓN CAPTURADA]: {type(e).__name__} -> {e}")
        
    else:
        # Se ejecuta únicamente si no ocurrió ninguna excepción
        print("\n¡Operación exitosa!")
        print(f"El retiro se ha completado correctamente. Stock restante del producto: {stock_restante}")

if __name__ == "__main__":
    main()