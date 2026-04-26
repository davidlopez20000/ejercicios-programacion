"""14. Adivina el PIN
Enunciado: Define una variable con un PIN secreto (ej. "1234"). Usa un bucle while para pedirle al usuario que ingrese el PIN. El programa no debe dejarlo avanzar hasta que ingrese el PIN correcto.
Conceptos: Bucle while, comparación de cadenas.
"""

# Definir el PIN secreto
pin_secreto = "1234"

# Inicializar pin como vacío
pin = ""

# Bucle while para pedir PIN hasta que sea correcto
while pin != pin_secreto:
    # Solicitar el PIN al usuario
    pin = input("Ingrese el PIN: ")

# Una vez correcto, conceder acceso
print("Acceso concedido.")

##Bucle while para solicitar al usuario que ingrese un PIN hasta que ingrese el PIN correcto. El programa compara el PIN ingresado con un PIN secreto predefinido y continúa solicitando el PIN hasta que se ingrese correctamente, momento en el cual se muestra un mensaje de "Acceso concedido".