"""4. El mayor de dos
Enunciado: Pide al usuario dos números diferentes y muestra por pantalla cuál de los dos es el mayor.
Conceptos: Variables, condicional if-else, comparación (>).
"""

# Pedir el primer número
a = int(input("Primer número: "))

# Pedir el segundo número
b = int(input("Segundo número: "))

# Comparar los números
if a > b:
    # Si a es mayor, mostrar a
    print(f"El mayor es {a}")
else:
    # Si no, mostrar b
    print(f"El mayor es {b}")