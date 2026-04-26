# Este programa calcula el promedio de calificaciones escolares, clasifica las materias en aprobadas y reprobadas, y muestra estadísticas adicionales.

# Inicializar listas para almacenar las materias y calificaciones
materias = []
calificaciones = []

# Bucle infinito para ingresar materias y calificaciones
while True:
    # Solicitar el nombre de la materia y eliminar espacios en blanco
    materia = input("Ingrese el nombre de la materia: ").strip()
    # Intentar convertir la calificación a float y validar el rango
    try:
        nota = float(input("Ingrese la calificación (0 a 10): "))
        # Verificar si la nota está entre 0 y 10
        if nota < 0 or nota > 10:
            print("Error: la calificación debe estar entre 0 y 10.")
            continue
    except ValueError:
        # Manejar error si no se ingresa un número válido
        print("Error: ingrese un número válido.")
        continue

    # Agregar la materia y calificación a las listas
    materias.append(materia)
    calificaciones.append(nota)

    # Preguntar si desea continuar
    continuar = input("¿Desea ingresar otra materia? (s/n): ").lower()
    # Si no es 's', salir del bucle
    if continuar != "s":
        break

# Verificar si se ingresaron materias
if len(materias) == 0:
    print("No se ingresaron materias. Programa finalizado.")
else:
    # Calcular el promedio de las calificaciones
    promedio = sum(calificaciones) / len(calificaciones)

    # Definir el umbral para aprobar (5.0)
    umbral = 5.0
    # Listas para índices de aprobadas y reprobadas
    aprobadas = []
    reprobadas = []
    # Clasificar cada calificación
    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    # Encontrar los índices de la calificación máxima y mínima
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))

    # Mostrar el resumen final
    print("\n--- RESUMEN FINAL ---")
    # Listar todas las materias con sus calificaciones
    for i in range(len(materias)):
        print(f"{materias[i]}: {calificaciones[i]}")

    # Mostrar el promedio general
    print(f"\nPromedio general: {promedio:.2f}")

    # Mostrar materias aprobadas
    print("\nMaterias aprobadas:")
    for i in aprobadas:
        print(f"{materias[i]} ({calificaciones[i]})")

    # Mostrar materias reprobadas
    print("\nMaterias reprobadas:")
    for i in reprobadas:
        print(f"{materias[i]} ({calificaciones[i]})")

    # Mostrar la mejor y peor materia
    print(f"\nMejor materia: {materias[indice_max]} ({calificaciones[indice_max]})")
    print(f"Peor materia: {materias[indice_min]} ({calificaciones[indice_min]})")

    # Mensaje de despedida
    print("\nGracias por usar la calculadora de promedios. ¡Hasta pronto!")


##Programa completo para calcular promedios escolares, clasificar materias y mostrar estadísticas. El programa solicita al usuario ingresar materias y calificaciones, validando las entradas. Luego calcula el promedio, clasifica las materias en aprobadas y reprobadas, y muestra un resumen final con toda la información ingresada y calculada. El programa se ejecuta de manera interactiva y finaliza con un mensaje de despedida.