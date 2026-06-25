
def agregar_producto(inventario: list) -> None:
    """Agrega un nuevo producto o aumenta el stock si ya existe."""
    print("\n-- Agregar Producto --")
    nombre: str = input("Nombre del producto: ").strip()

    # Validar que el nombre no esté vacío
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    # Validar la cantidad
    while True:
        try:
            cantidad: int = int(input("Cantidad a agregar: "))
            if cantidad > 0:
                break
            else:
                print(" La cantidad debe ser mayor a 0.")
        except ValueError:
            print(" Ingresa un número entero válido.")

    # Buscar si el producto ya existe en el inventario
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            producto[1] += cantidad
            print(f"Producto '{producto[0]}' actualizado. Ahora tiene {producto[1]} unidades.")
            return

    # Si no existe, agregar como nuevo producto
    inventario.append([nombre, cantidad])
    print(f"Producto '{nombre}' agregado con {cantidad} unidades.")


def mostrar_inventario(inventario: list) -> None:
    """Muestra todos los productos del inventario sin repetir nombres."""
    print("\n-- INVENTARIO ACTUAL --")

    if not inventario:
        print("El inventario está vacío.")
        return

    print(f"{'Producto':<25} | {'Cantidad':>8}")
    print("-" * 25 + "-+-" + "-" * 8)

    for producto in inventario:
        print(f"{producto[0]:<25} | {producto[1]:>8}")

    print("-" * 36)
    print(f"Total de productos distintos: {len(inventario)}")


def vender_producto(inventario: list) -> None:
    """Vende una unidad de un producto y lo retira si el stock llega a 0."""
    print("\n-- Vender Producto --")

    if not inventario:
        print("El inventario está vacío. No hay productos para vender.")
        return

    nombre: str = input("Nombre del producto a vender: ").strip()

    # Buscar el producto en el inventario
    for i, producto in enumerate(inventario):
        if producto[0].lower() == nombre.lower():
            if producto[1] > 1:
                producto[1] -= 1
                print(f"Venta exitosa. Quedan {producto[1]} unidades de '{producto[0]}'.")
            else:
                # Última unidad: se vende y se elimina del inventario
                inventario.pop(i)
                print(f" Venta exitosa. '{nombre}' fue retirado del inventario (sin stock).")
            return

    print(f"Producto '{nombre}' no encontrado en el inventario.")


def mostrar_menu() -> None:
    """Muestra el menú principal del sistema."""
    print("\n_______________________________________________")
    print("         INVENTARIO BÁSICO")
    print("_______________________________________________")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4. Salir")
    print("_______________________________________________")


def main() -> None:
    """Función principal que controla el flujo del programa."""

    # Inventario representado como lista de listas: [[nombre, cantidad], ...]
    inventario: list = []

    print("_______________________________________________")
    print("   BIENVENIDO AL SISTEMA DE INVENTARIO     ")
    print("_______________________________________________")

    # El programa solo termina cuando el usuario elige la opción 4
    while True:
        mostrar_menu()

        # Validar que la opción del menú sea un entero válido
        try:
            opcion: int = int(input("Elige una opción (1-4): "))
        except ValueError:
            print("Ingresa un número del 1 al 4.")
            continue

        if opcion == 1:
            agregar_producto(inventario)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            vender_producto(inventario)

        elif opcion == 4:
            print("\n¡Hasta luego! Gracias por usar el sistema de inventario.")
            break

        else:
            print("Opción no válida. Por favor elige una opción del 1 al 4.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
