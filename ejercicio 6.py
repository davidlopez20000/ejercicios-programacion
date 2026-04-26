"""6. Categoría de edad
Enunciado: Pide la edad al usuario y clasifícalo según las siguientes categorías: 0-12 (Niño), 13-17 (Adolescente), 18-64 (Adulto), 65 o más (Adulto mayor).
Conceptos: Operadores lógicos (and) o anidamiento de elif.
"""

# Pedir la edad al usuario
edad = int(input("¿Cuántos años tienes? "))

# Clasificar según rangos de edad
if edad <= 12:
    print("categoria: Niño")
elif edad <= 17:
    print("Categoria: Adolescente")
elif edad <= 64:
    print("Categoria: Adulto")
else:
    print("Categoria: Adulto mayor")