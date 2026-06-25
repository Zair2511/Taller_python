
# Lista principal que almacena todos los libros de la biblioteca
biblioteca: list = []

# Diccionario que registra los libros prestados por cada usuario
usuarios: dict = {}


# ── 1. AGREGAR LIBRO ─────────────────────────────────────────────────
def agregar_libro(titulo: str, autor: str, genero: str, copias: int = 1) -> None:
    """
    Agrega un nuevo libro a la biblioteca.
    Si el libro ya existe (mismo título), aumenta las copias disponibles.
    El parámetro 'copias' es opcional; por defecto vale 1.
    """
    # Buscar si el libro ya está registrado
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            # El libro existe: solo se aumentan las copias
            libro["copias"] += copias
            print(f"El libro '{titulo}' ya existe. Copias actualizadas: {libro['copias']}")
            return

    # El libro no existe: crear nuevo diccionario y agregarlo a la lista
    nuevo_libro: dict = {
        "titulo" : titulo,
        "autor"  : autor,
        "genero" : genero,
        "copias" : copias,
        # Tupla con los datos principales (dato inmutable como referencia)
        "info"   : (titulo, autor, genero)
    }
    biblioteca.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado correctamente con {copias} copia(s).")


# ── 2. BUSCAR LIBROS (con yield) ──────────────────────────────────────
def buscar_libros(criterio: str, valor: str):
    """
    Iterador que busca libros por 'titulo', 'autor' o 'genero'.
    Usa yield para generar los resultados uno a uno de forma eficiente,
    sin necesidad de cargar todos los resultados en memoria a la vez.
    """
    # Recorrer cada libro y comparar el campo indicado (sin importar mayúsculas)
    for libro in biblioteca:
        if valor.lower() in libro[criterio].lower():
            yield libro   # ← yield entrega el libro y pausa la función


def mostrar_busqueda(criterio: str, valor: str) -> None:
    """Muestra en pantalla los resultados de una búsqueda."""
    # Se obtiene el iterador generado por buscar_libros
    resultados = list(buscar_libros(criterio, valor))

    if not resultados:
        print(f" No se encontraron libros con {criterio} = '{valor}'.")
        return

    print(f"\n Resultados de búsqueda por {criterio} = '{valor}':")
    print("-" * 50)
    for libro in resultados:
        print(f"  Título  : {libro['titulo']}")
        print(f"  Autor   : {libro['autor']}")
        print(f"  Género  : {libro['genero']}")
        print(f"  Copias  : {libro['copias']}")
        print("-" * 50)


# ── 3. PRESTAR LIBRO ─────────────────────────────────────────────────
def prestar_libro(titulo: str, usuario: str) -> None:
    """
    Presta un libro a un usuario si hay copias disponibles.
    Reduce en 1 las copias del libro y registra el préstamo en el diccionario usuarios.
    """
    # Verificar si el usuario ya está registrado; si no, crearlo con lista vacía
    if usuario not in usuarios:
        usuarios[usuario] = []

    # Buscar el libro en la biblioteca
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            # Verificar que haya copias disponibles
            if libro["copias"] > 0:
                libro["copias"] -= 1                   # Descontar una copia
                usuarios[usuario].append(libro["titulo"])  # Registrar el préstamo
                print(f"Libro '{libro['titulo']}' prestado a '{usuario}'. Copias restantes: {libro['copias']}")
            else:
                print(f"No hay copias disponibles de '{titulo}'.")
            return

    # Si el ciclo terminó sin encontrar el libro
    print(f"El libro '{titulo}' no existe en la biblioteca.")


# ── 4. DEVOLVER LIBRO ────────────────────────────────────────────────
def devolver_libro(titulo: str, usuario: str) -> None:
    """
    Registra la devolución de un libro.
    Aumenta en 1 las copias disponibles y elimina el préstamo del usuario.
    """
    # Verificar que el usuario exista y tenga ese libro prestado
    if usuario not in usuarios or titulo not in usuarios[usuario]:
        print(f"error'{usuario}' no tiene prestado el libro '{titulo}'.")
        return

    # Buscar el libro y devolver la copia
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            libro["copias"] += 1                        # Devolver la copia
            usuarios[usuario].remove(titulo)            # Quitar de la lista del usuario
            print(f"✅ Libro '{titulo}' devuelto por '{usuario}'. Copias disponibles: {libro['copias']}")
            return


# ── 5. MOSTRAR LIBROS DISPONIBLES (con yield) ────────────────────────
def libros_disponibles():
    """
    Iterador que genera únicamente los libros con al menos 1 copia disponible.
    Usa yield para recorrer la lista de forma eficiente.
    """
    for libro in biblioteca:
        if libro["copias"] > 0:
            yield libro   # ← solo entrega libros con copias disponibles


def mostrar_disponibles() -> None:
    """Muestra en pantalla todos los libros con copias disponibles."""
    print("\n LIBROS DISPONIBLES EN LA BIBLIOTECA")
    print("=" * 50)

    # Convertir el iterador a lista para poder verificar si está vacío
    disponibles = list(libros_disponibles())

    if not disponibles:
        print("No hay libros disponibles en este momento.")
        return

    for i, libro in enumerate(disponibles, start=1):
        # Se accede a la tupla 'info' para mostrar los datos principales
        titulo, autor, genero = libro["info"]
        print(f"{i}. {titulo}")
        print(f"   Autor  : {autor}")
        print(f"   Género : {genero}")
        print(f"   Copias : {libro['copias']}")
        print("-" * 50)


# ── 6. MOSTRAR LIBROS DE UN USUARIO ──────────────────────────────────
def mostrar_prestamos(usuario: str) -> None:
    """Muestra los libros que tiene prestados un usuario."""
    if usuario not in usuarios or not usuarios[usuario]:
        print(f"'{usuario}' no tiene libros prestados.")
        return

    print(f"\n Libros prestados a '{usuario}':")
    for titulo in usuarios[usuario]:
        print(f"  - {titulo}")


# ── MENÚ PRINCIPAL ────────────────────────────────────────────────────
def mostrar_menu() -> None:
    """Muestra el menú de opciones del sistema."""
    print("\n___________________________________________")
    print("       SISTEMA DE GESTIÓN DE BIBLIOTECA    ")
    print("_____________________________________________")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar libros disponibles")
    print("6. Ver préstamos de un usuario")
    print("7. Salir")
    print("______________________________________________")


def main() -> None:
    """Función principal que controla el flujo del programa."""

    # Cargar algunos libros de ejemplo para no empezar con la biblioteca vacía
    agregar_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 3)
    agregar_libro("El principito",         "Antoine de Saint-Exupéry", "Ficción", 2)
    agregar_libro("Don Quijote",           "Miguel de Cervantes",      "Clásico", 1)
    agregar_libro("1984",                  "George Orwell",            "Distopía", 2)

    salir: bool = False

    # El programa solo termina cuando el usuario elige la opción 7
    while not salir:
        mostrar_menu()

        try:
            opcion: int = int(input("Elige una opción (1-7): "))
        except ValueError:
            # Si el usuario escribe algo que no es número
            print("Ingresa un número del 1 al 7.")
            continue

        if opcion == 1:
            # ── Agregar libro ──
            print("\n-- Agregar Libro --")
            titulo  = input("Título  : ").strip()
            autor   = input("Autor   : ").strip()
            genero  = input("Género  : ").strip()
            try:
                copias = int(input("Copias (Enter = 1): ") or "1")  # argumento opcional
            except ValueError:
                copias = 1
            agregar_libro(titulo, autor, genero, copias)

        elif opcion == 2:
            # ── Buscar libro ──
            print("\n-- Buscar Libro --")
            print("Buscar por: 1) Título   2) Autor   3) Género")
            try:
                sub = int(input("Elige (1-3): "))
            except ValueError:
                sub = 0

            # Mapear la elección al nombre de clave del diccionario
            campos = {1: "titulo", 2: "autor", 3: "genero"}
            if sub in campos:
                valor = input(f"Ingresa el {campos[sub]}: ").strip()
                mostrar_busqueda(campos[sub], valor)
            else:
                print("Opción no válida.")

        elif opcion == 3:
            # ── Prestar libro ──
            print("\n-- Prestar Libro --")
            titulo  = input("Título del libro : ").strip()
            usuario = input("Nombre de usuario: ").strip()
            prestar_libro(titulo, usuario)

        elif opcion == 4:
            # ── Devolver libro ──
            print("\n-- Devolver Libro --")
            titulo  = input("Título del libro : ").strip()
            usuario = input("Nombre de usuario: ").strip()
            devolver_libro(titulo, usuario)

        elif opcion == 5:
            # ── Mostrar disponibles ──
            mostrar_disponibles()

        elif opcion == 6:
            # ── Ver préstamos de usuario ──
            print("\n-- Préstamos de Usuario --")
            usuario = input("Nombre de usuario: ").strip()
            mostrar_prestamos(usuario)

        elif opcion == 7:
            # ── Salir ──
            salir = True
            print("\n¡Hasta luego! Gracias por usar el sistema de biblioteca.")

        else:
            print("Opción no válida. Elige del 1 al 7.")


# Punto de entrada: solo se ejecuta si se corre el archivo directamente
if __name__ == "__main__":
    main()
