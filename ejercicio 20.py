"""20. Sucesión de Fibonacci
Enunciado: Pide al usuario cuántos términos de la sucesión de Fibonacci quiere generar. La sucesión comienza con 0 y 1, y cada número siguiente es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8...). Usa un bucle for para calcular y mostrar la serie.
Conceptos: Intercambio de variables temporales, lógica algorítmica, bucle for.
"""

# Solicitar el número de términos
n = int(input("¿Cuántos términos de Fibonacci desea? "))

# Inicializar los primeros dos términos
a, b = 0, 1

# Bucle for para generar n términos
for i in range(n):
    # Imprimir el término actual
    print(a, end=" ")
    # Actualizar a y b para el siguiente término
    a, b = b, a + b

# Agregar una nueva línea al final para que el prompt aparezca en la siguiente línea
print()

##Bucle for para generar los primeros N términos de la sucesión de Fibonacci, donde N es un número entero positivo ingresado por el usuario. El programa utiliza dos variables para almacenar los términos actuales de la sucesión y actualiza estos valores en cada iteración del bucle, imprimiendo cada término en la misma línea separado por un espacio.
