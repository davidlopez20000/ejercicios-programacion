import os
import copy

# ============================================================
#  SOKOBAN - Taller Práctico de Programación

# Diccionario de traducción: símbolo interno → emoji visible
EMOJIS = {
    "#": "🧱",
    "@": "🧍",
    "$": "📦",
    ".": "🎯",
    "*": "✅",
    " ": "🟫",
}

# ------------------------------------------------------------------
# NIVELES DEL JUEGO (12 niveles, dificultad creciente)
# La matriz usa los símbolos internos para que la lógica funcione.
# ------------------------------------------------------------------

NIVELES = [
    # Nivel 1 - Tutorial (mapa obligatorio del taller)
    [
        list("#######"),
        list("#     #"),
        list("#  $  #"),
        list("# .@  #"),
        list("#     #"),
        list("#######"),
    ],

    # Nivel 2 - Una caja, meta cerca
    [
        list("#######"),
        list("#.    #"),
        list("#     #"),
        list("#  $@ #"),
        list("#     #"),
        list("#######"),
    ],

    # Nivel 3 - Dos cajas, dos metas
    [
        list("#########"),
        list("#   .   #"),
        list("#  $    #"),
        list("#   @   #"),
        list("#  $    #"),
        list("#   .   #"),
        list("#########"),
    ],

    # Nivel 4 - Pasillos estrechos
    [
        list("#######"),
        list("#     #"),
        list("## $# #"),
        list("#. @  #"),
        list("## $# #"),
        list("#.    #"),
        list("#######"),
    ],

    # Nivel 5 - Tres cajas en fila
    [
        list("##########"),
        list("#        #"),
        list("#  $$$   #"),
        list("#  ...@  #"),
        list("#        #"),
        list("##########"),
    ],

    # Nivel 6 - Forma de L
    [
        list("########"),
        list("#  #   #"),
        list("#  $ . #"),
        list("#  #   #"),
        list("#@$  . #"),
        list("#  #   #"),
        list("########"),
    ],

    # Nivel 7 - Cuatro cajas
    [
        list("##########"),
        list("#   ##   #"),
        list("# $    $ #"),
        list("#  .  .  #"),
        list("#  .  .  #"),
        list("# $    $ #"),
        list("#   @#   #"),
        list("##########"),
    ],

    # Nivel 8 - Laberinto simple
    [
        list("##########"),
        list("#@  #    #"),
        list("#   # $  #"),
        list("# ###  # #"),
        list("# #  .   #"),
        list("#   #    #"),
        list("##########"),
    ],

    # Nivel 9 - Cajas en esquinas
    [
        list("##########"),
        list("# $    $ #"),
        list("#        #"),
        list("#  ....  #"),
        list("#        #"),
        list("# $  @ $ #"),
        list("##########"),
    ],

    # Nivel 10 - Pasillo con obstáculos
    [
        list("############"),
        list("#    #      #"),
        list("# $  #  $   #"),
        list("# .  #  .   #"),
        list("#    #      #"),
        list("#  @        #"),
        list("#    # $    #"),
        list("#    # .    #"),
        list("############"),
    ],

    # Nivel 11 - Cinco cajas
    [
        list("###########"),
        list("#    @    #"),
        list("#  $ $ $  #"),
        list("#         #"),
        list("# . . . . #"),
        list("#    $    #"),
        list("#         #"),
        list("###########"),
    ],

    # Nivel 12 - Jefe final
    [
        list("############"),
        list("#   #  #   #"),
        list("# $ .  . $ #"),
        list("#   #  #   #"),
        list("## $      ##"),
        list("#   # @#   #"),
        list("## $  .   ##"),
        list("#   #  #   #"),
        list("# $ .  . $ #"),
        list("#   #  #   #"),
        list("############"),
    ],
]


# ------------------------------------------------------------------
# FUNCIÓN 1: dibujar_mapa
# Recibe la matriz del nivel actual y la imprime con emojis.
# La traducción símbolo → emoji ocurre aquí, la lógica nunca la ve.
# ------------------------------------------------------------------
def dibujar_mapa(matriz):
    """Imprime el mapa en pantalla usando emojis en lugar de símbolos."""
    for fila in matriz:
        # Convertimos cada carácter interno a su emoji correspondiente
        linea_visual = "".join(EMOJIS.get(celda, celda) for celda in fila)
        print(linea_visual)


# ------------------------------------------------------------------
# FUNCIÓN 2: obtener_posicion_jugador
# Recorre la matriz buscando '@' y retorna (fila, columna).
# Trabaja con el símbolo interno, no con el emoji.
# ------------------------------------------------------------------
def obtener_posicion_jugador(matriz):
    """Recorre la matriz y retorna la posición (fila, columna) del jugador."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "@":
                return i, j
    # Si no se encuentra (no debería pasar), retornamos -1, -1
    return -1, -1


# ------------------------------------------------------------------
# FUNCIÓN 3: contar_cajas_sin_ubicar
# Cuenta cuántas cajas '$' quedan por colocar en una meta.
# ------------------------------------------------------------------
def contar_cajas_sin_ubicar(matriz):
    """Cuenta las cajas que todavía NO están sobre una meta."""
    contador = 0
    for fila in matriz:
        for celda in fila:
            if celda == "$":
                contador += 1
    return contador


# ------------------------------------------------------------------
# FUNCIÓN 4: mover
# Recibe la dirección ('w','a','s','d') y la matriz actual.
# Aplica la lógica de validación de colisiones.
# Retorna la matriz actualizada.
# ------------------------------------------------------------------
def mover(direccion, matriz):
    """
    Mueve al jugador en la dirección indicada.
    Maneja colisiones con paredes y empuje de cajas.
    Retorna la matriz con el estado actualizado.
    """

    # Obtenemos posición actual del jugador
    fila_j, col_j = obtener_posicion_jugador(matriz)

    # Calculamos el desplazamiento según la dirección
    if direccion == "w":
        df, dc = -1, 0   # Arriba: fila disminuye
    elif direccion == "s":
        df, dc = 1, 0    # Abajo: fila aumenta
    elif direccion == "a":
        df, dc = 0, -1   # Izquierda: columna disminuye
    elif direccion == "d":
        df, dc = 0, 1    # Derecha: columna aumenta
    else:
        return matriz    # Dirección inválida → no hacemos nada

    # Posición a la que quiere moverse el jugador
    nueva_fila = fila_j + df
    nueva_col  = col_j + dc

    # --- Verificamos límites del mapa para evitar IndexError ---
    total_filas = len(matriz)
    total_cols  = len(matriz[0])

    if nueva_fila < 0 or nueva_fila >= total_filas:
        return matriz
    if nueva_col < 0 or nueva_col >= total_cols:
        return matriz

    # Celda destino del jugador
    destino = matriz[nueva_fila][nueva_col]

    # --- CASO 1: El destino es una PARED → no se mueve ---
    if destino == "#":
        return matriz

    # --- CASO 2: El destino es SUELO LIBRE o META ---
    if destino == " " or destino == ".":
        matriz[fila_j][col_j]       = " "
        matriz[nueva_fila][nueva_col] = "@"
        return matriz

    # --- CASO 3: El destino tiene una CAJA ('$' o '*') ---
    if destino == "$" or destino == "*":
        # Calculamos la celda detrás de la caja
        fila_tras_caja = nueva_fila + df
        col_tras_caja  = nueva_col  + dc

        # Verificamos límites para la celda detrás de la caja
        if fila_tras_caja < 0 or fila_tras_caja >= total_filas:
            return matriz
        if col_tras_caja < 0 or col_tras_caja >= total_cols:
            return matriz

        celda_tras_caja = matriz[fila_tras_caja][col_tras_caja]

        # Solo se puede empujar si detrás hay suelo libre o meta
        if celda_tras_caja == " " or celda_tras_caja == ".":

            # Movemos la caja al espacio detrás de ella
            if celda_tras_caja == ".":
                matriz[fila_tras_caja][col_tras_caja] = "*"  # caja en meta ✅
            else:
                matriz[fila_tras_caja][col_tras_caja] = "$"  # caja en suelo

            # Si la caja que empujamos estaba sobre una meta, queda la meta libre
            if destino == "*":
                matriz[nueva_fila][nueva_col] = "@"
            else:
                matriz[nueva_fila][nueva_col] = "@"

            # Liberamos la celda de origen del jugador
            matriz[fila_j][col_j] = " "

        # Si detrás hay pared u otra caja → no se mueve nada
        return matriz

    # Cualquier otro caso: no hacer nada
    return matriz


# ------------------------------------------------------------------
# FUNCIÓN: limpiar_pantalla
# ------------------------------------------------------------------
def limpiar_pantalla():
    """Limpia la terminal """
    os.system("cls" if os.name == "nt" else "clear")


# ------------------------------------------------------------------
# FUNCIÓN: mostrar_instrucciones
# ------------------------------------------------------------------
def mostrar_instrucciones(nivel_actual, total_niveles):
    """Muestra los controles y el nivel actual debajo del mapa."""
    print()
    print(f"  Nivel: {nivel_actual} / {total_niveles}")
    print("  Leyenda:  🧍 Jugador  📦 Caja  🎯 Meta  ✅ Caja en meta  🧱 Pared")
    print()
    print("  Controles:")
    print("    W = Arriba    S = Abajo")
    print("    A = Izquierda D = Derecha")
    print("    Q = Salir del juego")
    print()


# ------------------------------------------------------------------
# FUNCIÓN: mostrar_pantalla_inicio
# ------------------------------------------------------------------
def mostrar_pantalla_inicio():
    """Imprime la pantalla de bienvenida."""
    limpiar_pantalla()
    print("=" * 40)
    print("          S O K O B A N  📦")
    print("      Taller Práctico - Python")
    print("=" * 40)
    print()
    print("  Empuja todas las cajas 📦")
    print("  hacia las metas 🎯 para")
    print("  completar cada nivel.")
    print()
    print("  📦 sobre 🎯 se convierte en ✅")
    print("  ¡Todas en meta = nivel superado!")
    print()
    print("  Presiona ENTER para comenzar...")
    input()


# ------------------------------------------------------------------
# FUNCIÓN PRINCIPAL: jugar
# Contiene el Game Loop principal del juego.
# ------------------------------------------------------------------
def jugar():
    """Bucle principal del juego. Maneja niveles y turnos."""

    mostrar_pantalla_inicio()

    total_niveles = len(NIVELES)
    nivel_actual  = 1

    while nivel_actual <= total_niveles:

        # Copia profunda para no modificar el nivel original
        mapa = copy.deepcopy(NIVELES[nivel_actual - 1])

        nivel_completado = False

        # ── BUCLE DE TURNO ──────────────────────────────────────────
        while not nivel_completado:

            # 1. Limpiar pantalla y redibujar con emojis
            limpiar_pantalla()
            print("=" * 40)
            print("          S O K O B A N  📦")
            print("=" * 40)
            print()
            dibujar_mapa(mapa)
            mostrar_instrucciones(nivel_actual, total_niveles)

            # 2. Leer entrada del usuario
            entrada = input("  Tu movimiento: ").strip().lower()

            # 3. Procesar la entrada
            if entrada == "q":
                limpiar_pantalla()
                print()
                print("  Gracias por jugar Sokoban. ¡Hasta pronto! 👋")
                print()
                return

            elif entrada in ("w", "a", "s", "d"):
                mapa = mover(entrada, mapa)

            else:
                # Tecla inválida → el juego NO crashea, simplemente ignora
                pass

            # 4. Verificar condición de victoria del nivel
            if contar_cajas_sin_ubicar(mapa) == 0:
                nivel_completado = True

        # ── NIVEL SUPERADO ───────────────────────────────────────────
        limpiar_pantalla()
        print()
        print("=" * 40)
        print(f"  🎉 ¡NIVEL {nivel_actual} COMPLETADO! 🎉")
        print("=" * 40)
        dibujar_mapa(mapa)
        print()

        if nivel_actual < total_niveles:
            print("  Presiona ENTER para el siguiente nivel...")
            input()
            nivel_actual += 1
        else:
            print("  ╔══════════════════════════════╗")
            print("  ║  🏆 ¡FELICITACIONES! 🏆      ║")
            print("  ║  Completaste los 12 niveles  ║")
            print("  ║  de Sokoban. ¡Eres el mejor! ║")
            print("  ╚══════════════════════════════╝")
            print()
            print("  Presiona ENTER para salir...")
            input()
            return


# ------------------------------------------------------------------
# PUNTO DE ENTRADA
# ------------------------------------------------------------------
if __name__ == "__main__":
    jugar()