"""11. Cuenta regresiva
Enunciado: Pide al usuario un número entero positivo. Usa un bucle while para mostrar una cuenta regresiva desde ese número hasta 0, y al final imprime "¡Despegue!".
Conceptos: Bucle while, decremento de variables."""

# Solicitar un número positivo
n = int(input("Ingrese un número positivo: "))

# Bucle while para contar desde n hasta 0
while n >= 0:
    # Imprimir el número actual
    print(n)
    # Decrementar n
    n -= 1

# Después del bucle, imprimir mensaje de despegue
print("¡Despegue!")

##Bucle while para crear una cuenta regresiva desde un número positivo ingresado por el usuario hasta cero, imprimiendo cada número en la cuenta regresiva. Al finalizar, se imprime un mensaje de "¡Despegue!".