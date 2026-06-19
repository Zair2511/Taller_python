import random

def obtener_numero_valido() -> int:
    """Solicita y valida que el usuario ingrese un número entero entre 1 y 100."""
    while True:
        try:
            numero: int = int(input("Ingresa tu número (1-100): "))
            if 1 <= numero <= 100:
                return numero
            else:
                print("Número fuera de rango. Ingresa un número entre 1 y 100.\n")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número entero.\n")


def evaluar_desempeno(intentos: int) -> str:
    """Devuelve un mensaje según cuántos intentos usó el jugador."""
    if intentos == 1:
        return "¡¡INCREÍBLE!! ¡Lo adivinaste al primer intento! "
    elif intentos <= 3:
        return "¡Excelente desempeño! "
    elif intentos <= 7:
        return "¡Buen trabajo! "
    else:
        return "¡Por los pelos, pero lo lograste!"


def jugar() -> None:
    """Función principal que ejecuta el juego de adivinar el número."""
    MAX_INTENTOS: int = 10

    # Generar número aleatorio secreto entre 1 y 100
    numero_secreto: int = random.randint(1, 100)

    intentos: int = 0
    adivinado: bool = False

    print("============================================")
    print("   BIENVENIDO AL JUEGO: ADIVINA EL NÚMERO  ")
    print("============================================")
    print(f"He pensado un número entre 1 y 100.")
    print(f"Tienes {MAX_INTENTOS} intentos para adivinarlo.")
    print("============================================\n")

    # Ciclo principal del juego
    while intentos < MAX_INTENTOS and not adivinado:

        intentos += 1
        print(f"--- Intento {intentos} de {MAX_INTENTOS} ---")

        intento: int = obtener_numero_valido()

        # Comparar el intento con el número secreto
        if intento == numero_secreto:
            adivinado = True
            print(f"\n¡¡FELICIDADES!! ¡Adivinaste el número {numero_secreto}!")
            print(f"Lo lograste en {intentos} intento(s).")
            print(evaluar_desempeno(intentos))

        elif intento < numero_secreto:
            print(f"Demasiado BAJO. El número secreto es MAYOR que {intento}.")
            intentos_restantes: int = MAX_INTENTOS - intentos
            if intentos_restantes > 0:
                print(f"   Te quedan {intentos_restantes} intento(s).\n")

        else:
            print(f"Demasiado ALTO. El número secreto es MENOR que {intento}.")
            intentos_restantes: int = MAX_INTENTOS - intentos
            if intentos_restantes > 0:
                print(f"   Te quedan {intentos_restantes} intento(s).\n")

    # Si se agotaron los intentos sin adivinar
    if not adivinado:
        print("\n============================================")
        print("¡Se acabaron los intentos!")
        print(f"El número secreto era: {numero_secreto}")
        print("¡Mejor suerte la próxima vez!")
        print("============================================")

    print("\nGracias por jugar. ¡Hasta la próxima!")


# Punto de entrada del programa
if __name__ == "__main__":
    jugar()
