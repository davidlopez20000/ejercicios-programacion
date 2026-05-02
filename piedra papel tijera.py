'''
Reto de programación # 1: Piedra, Papel o Tijera

1. Descripción de problema
Se solicita desarrollar un programa interactivo en Python que permita a un usuario enfrentarse contra la computadora en el 
Clásico juego de Piedra, Papel o Tijera.
El programa debe ser capaz de procesar la entrada del usuario, generar una respuesta aleatoria y determinar un ganador 
basándose en las reglas tradicionales.

2. Requerimientos Técnicos

El algoritmo debe estructurarse de la siguiente manera:

* Interfaz Visual: Mostrar un encabezado decorativo utilizando métodos de cadena como .center() y multiplicación de caracteres.

* Entrada de Datos: Solicitar al usuario su elección. El programa debe ser capaz de reconocer la entrada sin importar si 
se escribe en mayúsculas o minúsculas.

* Inteligencia Aleatoria: La computadora debe elegir una opción de una lista predefinida de opciones (Piedra, Papel, Tijera) 
de forma aleatoria utilizando el módulo random.

* Lógica de comparación:

Implementar las condiciones necesarias para evaluar.

1. Empate: Ambas elecciones son iguales.
2. Victoria: El usuario vence a la PC (Piedra vence a Tijera, Tijera vence a Papel, Papel vence a Piedra).
3. Derrota: La PC vence al usuario.

* Control de Flujo: El juego debe repetirse indefinidamente dentro de un blucle hasta que el usuario decida escribir 
la palabra (Salir).

Solución del Ejercicio Propuesto    
'''
import random
import time

# titulo 
print("=" * 60)
print("   Juego Interactivo: Piedra, Papel o Tijera   ".center(60))
print("=" * 60)

# Opciones válidas del juego.
opciones = ["piedra", "papel", "tijera"]

# Dibujos en ASCII para mostrar cada jugada.
dibujos = {
    "piedra": """
        _______
    ---'   ____)    
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "papel": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "tijera": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

# Bucle principal del juego.
# Se repite hasta que el usuario escriba "salir".
while True:
    # Pedimos la elección del jugador y la normalizamos a minúsculas.
    jugador = input("Elige Piedra, Papel o Tijera (o escribe 'Salir'): ").lower()
    
    if jugador == "salir":
        print("Has decidido salir del juego. ¡Hasta pronto!")
        break
    
    # Validamos que la entrada esté dentro de las opciones aceptadas.
    if jugador not in opciones:
        print("Entrada inválida. Intenta nuevamente.")
        continue
    
    # La computadora elige aleatoriamente una opción.
    computadora = random.choice(opciones)
    time.sleep(0.5)
    
    # Mostramos lo que eligió cada uno con arte ASCII= dibujos 
    print(f"Tú elegiste: {jugador.capitalize()}")
    print(dibujos[jugador])
    print(f"La computadora eligió: {computadora.capitalize()}")
    print(dibujos[computadora])
    time.sleep(1)
    
    # Determinamos el resultado según las reglas del juego.
    if jugador == computadora:
        print("Resultado: ¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "tijera" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
        print("Resultado: ¡Ganaste! ")
    else:
        print("Resultado: La computadora gana ")
    
    print("-" * 60)

# Mensaje final
print("=" * 60)
print("Fin del Juego - Gracias por jugar".center(60))
print("=" * 60)