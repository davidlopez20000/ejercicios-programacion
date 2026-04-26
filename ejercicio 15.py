"""15. Contador de vocales
Enunciado: Pide al usuario que ingrese una frase. Utiliza un bucle for para recorrer cada letra de la frase y cuenta cuántas vocales (a, e, i, o, u) tiene. Imprime el total.
Conceptos: Bucle for sobre una cadena (string), condicionales dentro de un bucle, variable contador.
"""

# Solicitar la frase al usuario y convertir a minúsculas
frase = input("Ingrese una frase: ").lower()

# Inicializar contador de vocales
contador = 0

# Bucle for para iterar sobre cada letra
for letra in frase:
    # Verificar si la letra es una vocal
    if letra in "aeiou":
        # Incrementar contador
        contador += 1

# Imprimir el número de vocales
print(f"La frase tiene {contador} vocales.")

##Bucle for para contar el número de vocales en una frase ingresada por el usuario. El programa convierte la frase a minúsculas para contar tanto mayúsculas como minúsculas, y luego itera sobre cada letra de la frase, incrementando un contador cada vez que encuentra una vocal. Al final, se muestra el número total de vocales encontradas en la frase.