"""
===========================================================
  TALLER AUTÓNOMO: EL ARTE DE LAS FUNCIONES EN PYTHON
===========================================================
  Autor   : [Tu Nombre]
  Materia : Fundamentos de Programación
  Fecha   : Mayo 2025
  Fuente  : https://ellibrodepython.com/funciones-python

  Propósito:
      Demostrar los conceptos fundamentales de las funciones
      en Python mediante ejemplos funcionales y comentarios
      explicativos, cubriendo definición, parámetros, retorno,
      valores por defecto, scope y argumentos variables.
===========================================================
"""


# ==========================================================
# --- 1. DEFINICIÓN BÁSICA DE UNA FUNCIÓN ---
# ==========================================================

# Una función es un bloque de código reutilizable que agrupa
# instrucciones bajo un nombre. Se define con 'def' y solo
# se ejecuta cuando es LLAMADA explícitamente.

def saludar():
    """
    Función de bienvenida sin parámetros.

    No recibe datos externos ni devuelve ningún valor;
    simplemente imprime un mensaje en pantalla para
    demostrar la estructura mínima de una función.
    """
    print("¡Hola! Esta es mi primera función en Python.")

# Llamada a la función (sin paréntesis no se ejecuta, solo se referencia)
saludar()


# ==========================================================
# --- 2. PASO DE PARÁMETROS Y ARGUMENTOS ---
# ==========================================================

# Los parámetros son las variables que la función "espera" recibir.
# Los argumentos son los valores concretos que le pasamos al llamarla.

# --- 2a. Argumentos POSICIONALES (el orden importa) ---

# Python asigna cada argumento al parámetro según su posición.
def describir_persona(nombre, edad):
    print(f"Nombre: {nombre} | Edad: {edad} años")

describir_persona("Ana", 25)       # nombre="Ana", edad=25
describir_persona("Carlos", 30)    # nombre="Carlos", edad=30


# --- 2b. Argumentos POR NOMBRE (keyword arguments) ---

# Al indicar el nombre del parámetro, el orden ya no importa.
def registrar_producto(nombre, precio, categoria):
    print(f"Producto: {nombre} | Precio: ${precio} | Categoría: {categoria}")

# Llamada mezclando posicional y por nombre
registrar_producto("Laptop", categoria="Electrónica", precio=1500)


# ==========================================================
# --- 3. SENTENCIA RETURN: DEVOLVER VALORES ---
# ==========================================================

# 'return' finaliza la función y entrega un resultado al código
# que la llamó. Sin 'return', la función devuelve None implícitamente.

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Parámetros:
        base   (float): Longitud de la base.
        altura (float): Longitud de la altura.

    Retorna:
        float: El resultado de base × altura.
    """
    area = base * altura
    return area   # El valor sale de la función y puede ser usado afuera

resultado = calcular_area_rectangulo(5, 3)
print(f"Área del rectángulo: {resultado} unidades²")

# También podemos retornar múltiples valores como una tupla
def operaciones_basicas(a, b):
    # Python empaqueta automáticamente los valores en una tupla
    return a + b, a - b, a * b

suma, resta, producto = operaciones_basicas(10, 4)
print(f"Suma: {suma} | Resta: {resta} | Producto: {producto}")


# ==========================================================
# --- 4. PARÁMETROS POR DEFECTO (OPCIONALES) ---
# ==========================================================

# Un parámetro con valor por defecto es OPCIONAL al llamar la función.
# Si el caller no lo pasa, Python usa el valor predefinido.
# REGLA: los parámetros con valor por defecto van SIEMPRE al final.

def enviar_correo(destinatario, asunto, prioridad="normal"):
    print(f"Para: {destinatario} | Asunto: {asunto} | Prioridad: {prioridad}")

enviar_correo("juan@mail.com", "Reunión mañana")             # usa prioridad="normal"
enviar_correo("jefa@mail.com", "Informe urgente", "alta")    # sobreescribe el default


# ==========================================================
# --- 5. SCOPE: VARIABLES LOCALES VS GLOBALES ---
# ==========================================================

# El SCOPE (alcance) determina desde dónde es visible una variable.
# LOCAL : creada dentro de una función; muere cuando la función termina.
# GLOBAL: creada fuera de toda función; visible en todo el módulo.

empresa = "TechCorp"   # Variable GLOBAL: accesible en cualquier función

def mostrar_departamento():
    # Variable LOCAL: solo existe dentro de esta función
    departamento = "Desarrollo de Software"
    # Podemos LEER la variable global sin problema
    print(f"Empresa: {empresa} | Departamento: {departamento}")

mostrar_departamento()

# Si intentamos acceder a 'departamento' aquí, Python lanzaría NameError
# porque es una variable local que ya no existe fuera de la función.
print(f"Variable global 'empresa' sigue disponible: {empresa}")


# --- Modificar una variable global desde una función ---

# Sin la palabra clave 'global', Python crearía una nueva variable LOCAL
# con el mismo nombre en lugar de modificar la global.
contador_global = 0

def incrementar_contador():
    global contador_global          # Le decimos a Python que use la global
    contador_global += 1            # Ahora sí modifica la variable global
    print(f"Contador actual: {contador_global}")

incrementar_contador()   # → 1
incrementar_contador()   # → 2
incrementar_contador()   # → 3


# ==========================================================
# --- 6. ARGUMENTOS VARIABLES (*args) ---
# ==========================================================

# *args permite que una función acepte un número INDEFINIDO de
# argumentos posicionales. Python los recoge en una TUPLA.
# Útil cuando no sabemos de antemano cuántos valores recibiremos.

def sumar_todos(*numeros):
    # 'numeros' es una tupla con todos los argumentos recibidos
    total = 0
    for n in numeros:
        total += n
    return total

print(f"Suma de 3 números  : {sumar_todos(1, 2, 3)}")
print(f"Suma de 5 números  : {sumar_todos(10, 20, 30, 40, 50)}")
print(f"Suma de 1 número   : {sumar_todos(99)}")


def mostrar_equipo(lider, *integrantes):
    # Se puede combinar un parámetro fijo con *args
    print(f"Líder del equipo : {lider}")
    print(f"Integrantes      : {', '.join(integrantes)}")

mostrar_equipo("María", "Pedro", "Lucía", "Tomás", "Sofía")


