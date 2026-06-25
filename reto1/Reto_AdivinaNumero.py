
    
import random


def obtener_numero_valido() -> int:     
    """Solicita y valida que el usuario ingrese un número entero entre 1 y 100."""
    while True:
        try:
            # Se convierte la entrada a entero; si falla, salta al except
            numero: int = int(input("Ingresa tu número (1-100): "))

            # Verificar que el número esté dentro del rango permitido
            if 1 <= numero <= 100:
                return numero
            else:
                print("Número fuera de rango. Ingresa un número entre 1 y 100.\n")

        except ValueError:
            # Se captura el error cuando el usuario ingresa texto u otro valor no entero
            print("Entrada no válida. Por favor ingresa un número entero.\n")


def evaluar_desempeno(intentos: int) -> str:
    """Devuelve un mensaje de evaluación según cuántos intentos usó el jugador."""
    if intentos == 1:
        return "¡¡INCREÍBLE!! ¡Lo adivinaste al primer intento!"
    elif intentos <= 3:
        return "¡Excelente desempeño!"
    elif intentos <= 7:
        return "¡Buen trabajo!"
    else:
        # El jugador adivinó pero usó muchos intentos
        return "¡Por los pelos, pero lo lograste!"


def jugar() -> None:
    """Función principal que ejecuta el juego de adivinar el número."""

    # Número máximo de intentos permitidos
    MAX_INTENTOS: int = 10

    # Generar un número aleatorio secreto entre 1 y 100 (ambos inclusive)
    numero_secreto: int = random.randint(1, 100)

    # Contador de intentos realizados por el jugador
    intentos: int = 0

    # Bandera que indica si el jugador adivinó el número
    adivinado: bool = False

    # Mensaje de bienvenida
    print("_____________________________________________")
    print("   BIENVENIDO AL JUEGO: ADIVINA EL NÚMERO  ")
    print("_____________________________________________")
    print(f"He pensado un número entre 1 y 100.")
    print(f"Tienes {MAX_INTENTOS} intentos para adivinarlo.")
    print("_____________________________________________\n")

    # Ciclo principal: continúa mientras no se adivine y queden intentos
    while intentos < MAX_INTENTOS and not adivinado:

        # Incrementar el contador de intentos en cada turno
        intentos += 1
        print(f"--- Intento {intentos} de {MAX_INTENTOS} ---")

        # Solicitar un número válido al jugador
        intento: int = obtener_numero_valido()

        # Comparar el intento del jugador con el número secreto
        if intento == numero_secreto:
            # El jugador adivinó correctamente
            adivinado = True
            print(f"\n¡¡FELICIDADES!! ¡Adivinaste el número {numero_secreto}!")
            print(f"Lo lograste en {intentos} intento(s).")
            print(evaluar_desempeno(intentos))

        elif intento < numero_secreto:
            # El intento fue menor al número secreto
            print(f"Demasiado BAJO. El número secreto es MAYOR que {intento}.")
            intentos_restantes: int = MAX_INTENTOS - intentos
            if intentos_restantes > 0:
                print(f"   Te quedan {intentos_restantes} intento(s).\n")

        else:
            # El intento fue mayor al número secreto
            print(f"Demasiado ALTO. El número secreto es MENOR que {intento}.")
            intentos_restantes: int = MAX_INTENTOS - intentos
            if intentos_restantes > 0:
                print(f"   Te quedan {intentos_restantes} intento(s).\n")

    # Si se terminaron los intentos sin adivinar, se revela el número secreto
    if not adivinado:
        print("\n_____________________________________________")
        print("¡Se acabaron los intentos!")
        print(f"El número secreto era: {numero_secreto}")
        print("¡Mejor suerte la próxima vez!")
        print("_____________________________________________")

    print("\nGracias por jugar. ¡Hasta la próxima!")


# Punto de entrada del programa
# Solo se ejecuta si se corre este archivo directamente

if __name__ == "__main__":
    jugar()