#!/usr/bin/env python3
# =====================================================================
# PROYECTO: SIMULADOR FUSIONADO DE COMPUERTAS LÓGICAS Y TABLAS DE VERDAD
# Características: Colores ANSI, Parser Explicito, SOP/POS, Circuitos ASCII
# =====================================================================

import itertools
import re
import os
import time

# ──────────────────────────────────────────
#  COLORES ANSI para la terminal
# ──────────────────────────────────────────
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    RED    = "\033[91m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    BLUE   = "\033[94m"
    MAGENTA= "\033[95m"
    CYAN   = "\033[96m"
    WHITE  = "\033[97m"

def color(text, *codes):
    return "".join(codes) + str(text) + C.RESET

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# ──────────────────────────────────────────
#  BANNER / ENCABEZADO
# ──────────────────────────────────────────
BANNER = f"""
{C.CYAN}{C.BOLD}
╔══════════════════════════════════════════════════════════════╗
║   ██████   ██████   ██████  ██      ███████  █████  ███   ██ ║
║  ██    ██ ██    ██ ██    ██ ██      ██      ██   ██ ████  ██ ║
║  ██████   ██    ██ ██    ██ ██      █████   ███████ ██ ██ ██ ║
║  ██    ██ ██    ██ ██    ██ ██      ██      ██   ██ ██  ████ ║
║  ██████   ██████  ██████  ███████ ███████  ██   ██ ██   ███ ║
╚══════════════════════════════════════════════════════════════╝
     {C.YELLOW}🔌  Simulador de Puertas Lógicas & Circuitos v3.0  🔌
     {C.GREEN}   Fusión: Interfaz Colorida + Análisis Canónico Estándar
{C.RESET}"""

# ──────────────────────────────────────────
#  PARSER DE EXPRESIÓN
# ──────────────────────────────────────────

def extraer_variables(expresion: str) -> list:
    """Extrae variables únicas (letras) ordenadas de la expresión."""
    tokens = re.findall(r"[a-zA-Z]", expresion)
    vars_base = sorted(set(tokens))
    return vars_base

def evaluar_logica(expresion: str, asignacion: dict) -> int:
    """Evalúa una expresión booleana dada una asignación de variables."""
    expr = expresion.strip()

    # Reemplazar NOT: a' → (not a)
    expr = re.sub(r"([a-zA-Z])'", r"(not \1)", expr)

    # Reemplazar operadores textuales por equivalentes de Python
    expr = re.sub(r'\bOR\b',  ' or ',  expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bAND\b', ' and ', expr, flags=re.IGNORECASE)
    expr = re.sub(r'\bNOT\b', ' not ', expr, flags=re.IGNORECASE)

    # Reemplazar operadores simbólicos comunes (+, *, ·)
    expr = expr.replace("+", " or ")
    expr = expr.replace("·", " and ")
    expr = expr.replace("*", " and ")

    # Sustituir las variables con sus valores lógicos (0 o 1)
    # Ordenamos por longitud descendente para evitar conflictos de reemplazo parcial
    for var, val in sorted(asignacion.items(), key=lambda x: -len(x[0])):
        expr = re.sub(rf'\b{re.escape(var)}\b', str(val), expr)

    # Soporte para variables juntas que simulan multiplicación implícita (ej: ab -> a and b)
    # Reemplaza secuencias de números pegados "10" o "1 0" por "1 and 0"
    for _ in range(3): # Pasadas de seguridad para patrones anidados
        expr = re.sub(r'([01])\s*([01])', r'\1 and \2', expr)
        expr = re.sub(r'([01])\s*\(', r'\1 and (', expr)
        expr = re.sub(r'\)\s*([01])', r') and \1', expr)
        expr = re.sub(r'\)\s*\(', r') and (', expr)

    try:
        resultado = int(bool(eval(expr)))
        return resultado
    except Exception as e:
        raise ValueError(f"Error evaluando la sintaxis matemática '{expr}': {e}")

# ──────────────────────────────────────────
#  VISUALIZACIÓN DE TABLA DE VERDAD
# ──────────────────────────────────────────

def mostrar_tabla_verdad(expresion: str, variables: list) -> list:
    """Genera, calcula y muestra de forma colorida la tabla de verdad."""
    n = len(variables)
    ancho_var = 5

    print(f"\n  {color('TABLA DE VERDAD', C.BOLD, C.CYAN)}")
    print(f"  {color('Expresión original:', C.YELLOW)} {color(expresion, C.WHITE, C.BOLD)}\n")

    # Estructura visual de los separadores ASCII superiores e intermedios
    sep = "  ┌" + ("─" * ancho_var + "┬") * n + "─" * 11 + "┐"
    sep_mid = "  ├" + ("─" * ancho_var + "┼") * n + "─" * 11 + "┤"
    sep_bot = "  └" + ("─" * ancho_var + "┴") * n + "─" * 11 + "┘"

    print(color(sep, C.BLUE))
    
    # Cabecera de variables
    encabezado = "  │"
    for v in variables:
        encabezado += color(f"  {v.upper()}  ", C.BOLD, C.YELLOW) + "│"
    encabezado += color(f"   SALIDA   ", C.BOLD, C.MAGENTA) + "│"
    print(encabezado)
    print(color(sep_mid, C.BLUE))

    filas_resultados = []
    # Genera combinaciones binarias de forma descendente (Estilo clásico: 000 hasta 111)
    combinaciones = list(itertools.product([1, 0], repeat=n))
    combinaciones.reverse()

    for comb in combinaciones:
        asignacion = dict(zip(variables, comb))
        res = evaluar_logica(expresion, asignacion)
        filas_resultados.append((comb, res))

        # Impresión de la fila con colores adaptativos
        fila_str = "  │"
        for bit in comb:
            bit_color = C.GREEN if bit == 1 else C.RED
            fila_str += color(f"  {bit}  ", C.BOLD, bit_color) + "│"
        
        res_color = C.GREEN if res == 1 else C.RED
        simbolo = " 1 ✔ " if res == 1 else " 0 ✘ "
        fila_str += color(f"   {simbolo}  ", C.BOLD, res_color) + "│"
        print(fila_str)

    print(color(sep_bot, C.BLUE))
    return filas_resultados

# ──────────────────────────────────────────
#  PROCESAMIENTO DE FORMAS CANÓNICAS
# ──────────────────────────────────────────

def procesar_formas_canonicas(variables: list, filas_resultados: list):
    """Calcula y muestra las expresiones en Minterminos (SOP) y Maxterminos (POS)."""
    minterminos = []
    maxterminos = []
    n = len(variables)

    for idx, (comb, res) in enumerate(filas_resultados):
        if res == 1:
            minterminos.append(idx)
        else:
            maxterminos.append(idx)

    print(f"\n  {color('FORMAS CANÓNICAS ESTÁNDAR', C.BOLD, C.WHITE)}")
    print(f"  {color('─' * 58, C.WHITE)}")
    
    # Imprimir Minterminos
    if minterminos:
        sop_str = f"f({','.join(variables)}) = Σm({', '.join(map(str, minterminos))})"
        print(f"    {color('• Minitérminos (SOP):', C.GREEN)} {color(sop_str, C.BOLD, C.GREEN)}")
    else:
        print(f"    {color('• Minitérminos (SOP):', C.GREEN)} Ninguno (Contradicción total)")

    # Imprimir Maxterminos
    if maxterminos:
        pos_str = f"f({','.join(variables)}) = ΠM({', '.join(map(str, maxterminos))})"
        print(f"    {color('• Maxitérminos (POS):', C.RED)} {color(pos_str, C.BOLD, C.RED)}")
    else:
        print(f"    {color('• Maxitérminos (POS):', C.RED)} Ninguno (Tautología total)")
        
    return minterminos, maxterminos

# ──────────────────────────────────────────
#  DIAGRAMA DE CIRCUITO ADAPTATIVO
# ──────────────────────────────────────────

def dibujar_circuito_adaptativo(expresion: str, variables: list):
    """Dibuja de forma híbrida e inteligente un diagrama secuencial ASCII del circuito."""
    print(f"\n  {color('DIAGRAMA DEL CIRCUITO DE LA COMPUERTA PRINCIPAL', C.BOLD, C.CYAN)}")
    print(f"  {color('═' * 60, C.CYAN)}\n")

    # Detectar el tipo de operación raíz/principal
    tipo_compuerta = "OR " if "+" in expresion else "AND"

    # Generar líneas de entrada dinámicas con inversores si lo requieren
    lineas_entrada = []
    for v in variables:
        if f"{v}'" in expresion.lower() or f"not {v}" in expresion.lower():
            lineas_entrada.append(f"    {color(v.upper(), C.CYAN, C.BOLD)} ───[{color('NOT', C.RED, C.BOLD)}]───┐")
        else:
            lineas_entrada.append(f"    {color(v.upper(), C.CYAN, C.BOLD)} ─────────────┐")

    # Imprimir lógica del circuito acoplado en bloques
    num_entradas = len(lineas_entrada)
    
    if num_entradas == 1:
        print(lineas_entrada[0].replace("┐", ""))
        print(f"                   └───► {color('SALIDA (F)', C.YELLOW, C.BOLD)}")
    elif num_entradas == 2:
        print(lineas_entrada[0])
        print(f"                  ├───╔════════╗")
        print(f"                  │   ║  {color(tipo_compuerta, C.MAGENTA, C.BOLD)}   ╠═════► {color('SALIDA (F)', C.YELLOW, C.BOLD)}")
        print(lineas_entrada[1].replace("┐", "┘") + "   ╚════════╝")
    else:
        # Mayor o igual a 3 variables
        for i, linea in enumerate(lineas_entrada):
            if i == 0:
                print(linea)
            elif i == 1:
                print(f"{linea[:-4]}┼───╔════════╗")
                print(f"                  ├───╣  {color(tipo_compuerta, C.MAGENTA, C.BOLD)}   ╠═════► {color('SALIDA (F)', C.YELLOW, C.BOLD)}")
                print("                  │   ║        ║")
            elif i == 2:
                print(f"{linea[:-4]}┘   ╚════════╝")
            else:
                # Extensiones para 4 o 5 variables agregadas en paralelo
                print(f"    {linea[:-4]} Extendido a Bus Principal")

    print(f"\n  {color('[Leyenda]', C.WHITE)} [NOT] = Inversor lógico | {tipo_compuerta.strip()} = Compuerta base detectada.")

# ──────────────────────────────────────────
#  SINTAXIS Y GUÍA
# ──────────────────────────────────────────

def mostrar_guia_sintaxis():
    limpiar_pantalla()
    print(BANNER)
    print(f"  {color('MANUAL DE SINTAXIS ADMITIDA', C.BOLD, C.CYAN)}")
    print(f"  {color('═' * 55, C.CYAN)}\n")
    print("  El sistema reconoce automáticamente las variables presentes.")
    print(f"\n  {color('Operadores válidos:', C.YELLOW)}")
    print(f"    • {color('SUMA (OR):', C.GREEN)}       +")
    print(f"    • {color('PRODUCTO (AND):', C.GREEN)}  * (o variables juntas como 'ab')")
    print(f"    • {color('NEGACIÓN (NOT):', C.GREEN)}  Usa comilla simple (') después de la letra.")
    print(f"                        Ejemplo:" {color(\"a'\", C.MAGENTA)} significa (NOT A)")
    print(f"\n  {color('Ejemplos listos para copiar y pegar:', C.YELLOW)}")
    print("    -> a + b'")
    print("    -> a * b * c")
    print("    -> a' + b + c'")
    print("    -> ab + c'")
    print(f"  {color('═' * 55, C.CYAN)}")
    input(f"\n  {color('Presiona ENTER para volver al menú principal...', C.YELLOW)}")

# ──────────────────────────────────────────
#  FLUJO CENTRAL
# ──────────────────────────────────────────

def ejecutar_analisis():
    limpiar_pantalla()
    print(BANNER)
    print(f"  {color('INGRESAR EXPRESIÓN CANÓNICA', C.BOLD, C.GREEN)}")
    print(f"  {color('═' * 45, C.GREEN)}\n")
    
    expresion = input(f"  {color('➤ Introduce la fórmula (Ej: a + b\' * c): ', C.WHITE)}").strip()
    
    if not expresion:
        print(color("\n  ❌ Error: No ingresaste nada.", C.RED))
        time.sleep(1.5)
        return

    variables = extraer_variables(expresion)
    
    if not variables:
        print(color("\n  ❌ Error: No se detectaron variables válidas (letras a-z).", C.RED))
        input(f"\n  {color('Presiona ENTER para continuar...', C.YELLOW)}")
        return

    if len(variables) > 5:
        print(color("\n  ⚠ Advertencia: Máximo 5 variables para garantizar legibilidad terminal.", C.YELLOW))
        input(f"\n  {color('Presiona ENTER para continuar...', C.YELLOW)}")
        return

    # Ejecución secuencial de los componentes visuales
    limpiar_pantalla()
    print(BANNER)
    print(f"  Variables detectadas en el sistema: {color(', '.join(v.upper() for v in variables), C.YELLOW, C.BOLD)}")
    
    try:
        filas = mostrar_tabla_verdad(expresion, variables)
        procesar_formas_canonicas(variables, filas)
        dibujar_circuito_adaptativo(expresion, variables)
    except Exception as error:
        print(color(f"\n  ⚠ Ha ocurrido un error en tiempo de ejecución: {error}", C.RED, C.BOLD))
        
    input(f"\n  {color('Presiona ENTER para volver al menú...', C.YELLOW)}")

# ──────────────────────────────────────────
#  MENÚ PRINCIPAL
# ──────────────────────────────────────────

def main():
    while True:
        limpiar_pantalla()
        print(BANNER)
        print(f"  {color('MENÚ DE CONTROL DE INTERFAZ', C.BOLD, C.YELLOW)}")
        print(f"  {color('═' * 45, C.YELLOW)}\n")
        print(f"  {color('[1]', C.GREEN, C.BOLD)} 🔤  Ingresar nueva expresión booleana")
        print(f"  {color('[2]', C.GREEN, C.BOLD)} 📚  Ver guía de sintaxis y operadores")
        print(f"  {color('[3]', C.RED,  C.BOLD)} 🚪  Salir del simulador\n")
        
        opc = input(f"  {color('Selecciona una opción del menú: ', C.CYAN)}").strip()
        
        if opc == "1":
            ejecutar_analisis()
        elif opc == "2":
            mostrar_guia_sintaxis()
        elif opc == "3":
            limpiar_pantalla()
            print(f"\n{color('  ¡Éxito en tus proyectos de programación! Código finalizado. 🚀', C.CYAN, C.BOLD)}\n")
            break
        else:
            print(color("\n  ❌ Opción no válida del menú, intente de nuevo.", C.RED))
            time.sleep(1.2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{color('  Programa interrumpido de manera externa abruptamente. ¡Hasta luego! 👋', C.YELLOW)}\n")

        