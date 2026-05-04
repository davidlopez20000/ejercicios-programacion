"""

EJERCICIO DE PROGRAMACIÓN INTERMEDIA - FUNCIONES

El ejercicio consite en la implementación de una calculadora que permita realizar las siguientes 
operaciones: 

1. Sumar Dos Números
2. Restar Dos Números
3. Multiplicar Dos Números
4. Dividir Dos Números
5. Calcular el factorial de un número
6. Calcular la potencia de un número elevado a otro


Función Multiplicar: se encargará de realizar todo el proceso de multiplicación, incluyendo la solicitud
de los factores al usuario.

Función Dividir: se encargará de realizar todo el proceso de división, incluyendo la solicitud del dividendo
y el divisor al usuario. Validar que no se realice una división por cero.

Función Factorial: Se encargará de solicitar el número del que se quiere calcular el factorial.
Una Vez tenga el numero invocará a la función de calcular factorial, validar que el número sea positivo 
y entero.

Función FactorialCalculo: función recursiva que se realiza en el cálculo del factorial del número que 
recibe por parámetro.

Función Potencia: se encargará de solicitar la base y el exponente al usuario e invocará a la 
función de calcular potencia,validar que el exponente sea un número entero.

Función PotenciaCalculo: función recursiva que se realiza en el cálculo de la potencia de los números
pasados como parámetros.

Función Calculadora: función principal que se encargará de mostrar el menú de opciones al usuario, 
solicitar la opción deseada y llamar a la función correspondiente según la opción seleccionada. 
La función debe continuar mostrando el menú hasta que el usuario decida salir.

Importante: tanto el menú como los mensajes de solicitud de datos y resultados deben ser claros 
y amigables para el usuario, y se deben manejar adecuadamente los casos de error, como la división 
por cero o la entrada de datos no válidos.

Utilizar diseño de Interfaz de Usuario mediante la consola utilizando ASCII Art para hacer el menú 
más atractivo visualmente.
"""

def mostrar_menu():
    print("""
    ================================
    |         CALCULADORA          |
    ================================
    | 1. Sumar Dos Números         |
    | 2. Restar Dos Números        |
    | 3. Multiplicar Dos Números   |
    | 4. Dividir Dos Números       |
    | 5. Calcular Factorial        |
    | 6. Calcular Potencia         |
    | 7. Salir                     |
    ================================
    """)


def ingresar_opcion():
    opcion = int(input("Seleccione una opción (1-7): "))
    if 1 <= opcion <= 7:
        return opcion
    else:
        print("Por favor, ingrese un número entre 1 y 7.")

def calculadora():
    while True:
        mostrar_menu()
        opcion = ingresar_opcion()
        if opcion is None:
            continue
        if opcion == 1:
            opcion_sumar()
        elif opcion == 2:
            opcion_restar()
        elif opcion == 3:
            opcion_multiplicar()
        elif opcion == 4:
            opcion_dividir()
        elif opcion == 5:
            opcion_factorial()
        elif opcion == 6:
            opcion_potencia()
        elif opcion == 7:
            print("Saliendo de la calculadora. Gracias por usarla.")
            break

  
def sumar(num1, num2):
    return num1 + num2


def opcion_sumar():
    print("""
    ╔════════════════════════════════════════╗
    ║        ➕ SUMA DE DOS NÚMEROS         ║
    ║                                        ║
    ║      Ingrese dos valores para sumar    ║
    ║                                        ║
    ╚════════════════════════════════════════╝
    """)
    
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado =sumar (a, b)
    print(f"\nResultado: {a} + {b} = {resultado}\n")
    




def restar(num1, num2):
    return num1 - num2


def opcion_restar():
    print("""
    ╔════════════════════════════════════════╗
    ║        ➖ RESTA DE DOS NÚMEROS         ║
    ║                                        ║
    ║   Ingrese minuendo y sustraendo        ║
    ║                                        ║
    ╚════════════════════════════════════════╝
    """)

    c = float(input("Ingrese el minuendo: "))
    d = float(input("Ingrese el sustraendo: "))
    resultado = restar(c, d)
    print(f"\nResultado: {c} - {d} = {resultado}\n")




def multiplicar(num1, num2):
    return num1 * num2


def opcion_multiplicar():
    print("""
    ╔════════════════════════════════════════╗
    ║     ✖️ MULTIPLICACIÓN DE DOS NÚMEROS   ║
    ║                                        ║
    ║       Ingrese dos factores numéricos   ║
    ║                                        ║
    ╚════════════════════════════════════════╝
    """)
    
    e = float(input("Ingrese el primer número: "))
    f = float(input("Ingrese el segundo número: "))
    resultado = multiplicar(e, f)
    print(f"\nResultado: {e} × {f} = {resultado}\n")




def dividir(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2


def opcion_dividir():
    print("""
    ╔════════════════════════════════════════╗
    ║        ➗ DIVISIÓN DE DOS NÚMEROS      ║
    ║                                        ║
    ║       Ingrese dividendo y divisor      ║
    ║                                        ║
    ║      El divisor no puede ser cero      ║
    ╚════════════════════════════════════════╝
    """)
    
    g = float(input("Ingrese el dividendo: "))
    h = float(input("Ingrese el divisor: "))
    resultado_division = dividir(g, h)
    if resultado_division is None:
        print("No se puede dividir por cero.\n")
    else:
        print(f"\nResultado: {g} ÷ {h} = {resultado_division}\n")
   



def factorial_calculo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_calculo(n - 1)
    

def opcion_factorial():
    print("""
    ╔════════════════════════════════════════╗
    ║        CÁLCULO DE FACTORIAL            ║
    ║                                        ║
    ║     Ingrese un número entero positivo  ║
    ║                                        ║
    ╚════════════════════════════════════════╝
    """)
    
    numero = int(input("Ingrese un número entero: "))
    if numero < 0:
        print("El número debe ser positivo.\n")
    else:
        resultado_factorial = factorial_calculo(numero)
        print(f"\nResultado: {numero}! = {resultado_factorial}\n")








def potencia_calculo(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia_calculo(base, exponente - 1)


def opcion_potencia():
    print("""
    ╔════════════════════════════════════════╗
    ║       ⚡ CÁLCULO DE POTENCIA           ║
    ║                                        ║
    ║        Ingrese base y exponente        ║
    ║                                        ║
    ║     Exponente debe ser un entero       ║
    ╚════════════════════════════════════════╝
    """)
    try:
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente entero: "))
        resultado_potencia = potencia_calculo(base, exponente)
        print(f"\nResultado: {base}^{exponente} = {resultado_potencia}\n")
    except ValueError:
        print("Entrada inválida. Base numérica y exponente entero requeridos.\n")


if __name__ == "__main__":
    calculadora()