"""16. Adivina el número (con intentos)
Enunciado: El programa define un número secreto entre 1 y 20. El usuario tiene 5 intentos para adivinarlo (usando un bucle while o for). En cada intento, el programa debe decirle si el número ingresado es mayor o menor al número secreto. Si acierta, el bucle se detiene.
Conceptos: Bucle con límite, if-elif-else, interrupción de bucles (break).
"""

# Importar el módulo random para generar números aleatorios
import random

# Generar un número secreto entre 1 y 20
secreto = random.randint(1, 20)

# Definir el número de intentos
intentos = 5

# Bucle for para los intentos
for i in range(intentos):
    # Solicitar un número al usuario
    num = int(input("Adivina el número (1-20): "))
    # Verificar si es correcto
    if num == secreto:
        print("¡Correcto!")
        # Salir del bucle
        break
    elif num < secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
else:
    # Si no adivinó en los intentos, mostrar el número
    print(f"Se acabaron los intentos. El número era {secreto}.")

##Bucle for para implementar un juego de adivinar el número. El programa genera un número aleatorio entre 1 y 20, y el usuario tiene 5 intentos para adivinarlo. En cada intento, el programa indica si el número ingresado es correcto, mayor o menor que el número secreto. Si el usuario adivina correctamente, se muestra un mensaje de felicitación; si se agotan los intentos sin adivinar, se revela el número secreto.