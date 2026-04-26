"""8. Año bisiesto
Enunciado: Pide al usuario que ingrese un año. El programa debe determinar si es bisiesto o no (Un año es bisiesto si es divisible por 4, excepto si es divisible por 100, a menos que también sea divisible por 400).
Conceptos: Operador módulo (%), operadores lógicos anidados (and, or)."""


# Solicitar el año al usuario
año = int(input("Ingrese un año: "))

# Verificar las condiciones para un año bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    # Si cumple las condiciones, es bisiesto
    print("Es bisiesto.")
else:
    # Si no cumple, no es bisiesto
    print("No es bisiesto.")

##Lógica condicional con if y else para determinar si un año ingresado por el usuario es bisiesto o no. Un año es bisiesto si es divisible por 4 pero no por 100, o si es divisible por 400. El resultado se muestra al final.