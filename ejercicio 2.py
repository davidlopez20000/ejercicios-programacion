"""2. Par o Impar
Enunciado: Escribe un programa que pida al usuario un número entero y le diga si es par o impar.
Conceptos: Operador módulo (%), condicional if-else.
"""

# Pedir un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Verificar si el número es par usando el operador módulo
if numero % 2 == 0:
    # Si el resto de la división por 2 es 0, es par
    print(f"{numero} es PAR")
else:
    # Si no, es impar
    print(f"{numero} es IMPAR")