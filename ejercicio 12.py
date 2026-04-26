"""12. Suma de los primeros N números
Enunciado: Solicita un número N. Usa un bucle for para sumar todos los números desde el 1 hasta N y muestra el resultado final.
Conceptos: Bucle for con range(), variable acumuladora.
"""

# Solicitar el número N
N = int(input("Ingrese un número: "))

# Inicializar la suma en 0
suma = 0

# Bucle for para sumar desde 1 hasta N
for i in range(1, N+1):
    # Agregar i a la suma
    suma += i

# Imprimir el resultado
print(f"La suma es {suma}")

##Bucle for para calcular la suma de los primeros N números enteros, donde N es un número positivo ingresado por el usuario. El resultado se muestra al final.
