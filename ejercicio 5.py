"""5. Positivo, negativo o cero
Enunciado: Solicita un número al usuario. El programa debe imprimir si el número es positivo, negativo o si es exactamente cero.
Conceptos: Condicionales múltiples (if, elif, else).
"""

# Pedir un número al usuario (usando float para decimales)
numero = float(input("Ingresa un número: "))

# Verificar si es positivo
if numero > 0:
    print("El número es POSITIVO")
# Si no, verificar si es negativo
elif numero < 0:
    print("El número es NEGATIVO")
# Si no es ninguno, es cero
else:
    print("El número es CERO")