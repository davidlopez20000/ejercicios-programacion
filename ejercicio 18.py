"""18. Cajero Automático Básico
Enunciado: Simula un cajero. El saldo inicial es $1000. Usa un bucle while para mostrar un menú con tres opciones: 1. Consultar saldo, 2. Retirar dinero, 3. Salir. Si el usuario elige retirar, verifica que la cantidad sea menor o igual al saldo disponible antes de restar. El bucle termina solo cuando elige "Salir".
Conceptos: Menús interactivos con while, condicionales anidados, actualización de variables.
"""

# Inicializar saldo
saldo = 1000

# Bucle infinito para el menú
while True:
    # Mostrar opciones del menú
    print("\n1. Consultar saldo\n2. Retirar dinero\n3. Salir")
    # Solicitar opción
    opcion = input("Elija una opción: ")

    # Opción 1: Consultar saldo
    if opcion == "1":
        print(f"Saldo: ${saldo}")
    # Opción 2: Retirar dinero
    elif opcion == "2":
        retiro = float(input("Ingrese cantidad a retirar: "))
        # Verificar si hay fondos suficientes
        if retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
        else:
            print("Fondos insuficientes.")
    # Opción 3: Salir
    elif opcion == "3":
        print("Gracias por usar el cajero.")
        # Salir del bucle
        break
    # Opción inválida
    else:
        print("Opción inválida.")

##Bucle while para simular un cajero automático básico. El programa mantiene un saldo inicial y permite al usuario consultar el saldo, retirar dinero o salir del programa. El bucle continúa hasta que el usuario elige salir, y se manejan las opciones de manera condicional para realizar las acciones correspondientes.