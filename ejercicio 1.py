"""1. El saludo personalizado
Enunciado: Pide al usuario su nombre y su edad. Muestra un mensaje de bienvenida y calcula en qué año nació aproximadamente (restando la edad al año actual)
Conceptos: Variables, entrada/salida de datos, operaciones matemáticas básicas.
"""

# Pedir el nombre al usuario
nombre = input("¿Cómo te llamas? ")

# Pedir la edad y convertir a entero
edad = int(input("¿Cuántos años tienes? "))

# Definir el año actual
año_actual = 2025

# Calcular el año de nacimiento
año_nacimiento = año_actual - edad

# Mostrar mensaje de bienvenida
print(f"¡Hola, {nombre}! Bienvenido/a.")

# Mostrar el año de nacimiento
print(f"Naciste aproximadamente en el año {año_nacimiento}.")




