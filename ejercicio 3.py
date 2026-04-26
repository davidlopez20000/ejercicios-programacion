"""3. El peaje
Enunciado: Pregunta al usuario la edad. Si es mayor o igual a 18 años, muestra el mensaje "Puedes conducir", de lo contrario, muestra "Aún no tienes edad para conducir".
Conceptos: Condicional if-else, operadores relacionales (>=).
"""

# Pedir la edad al usuario y convertir a entero
edad = int(input("¿Cuántos años tienes? "))

# Verificar si la edad es mayor o igual a 18
if edad >= 18:
    # Si es mayor de edad, puede conducir
    print("Puedes conducir")
else:
    # Si no, no puede conducir
    print("Aún no tienes edad para conducir")