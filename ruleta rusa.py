"""1 descripcion del problema
se requiere desarrollar un programa en python que simule un sistemade azar basado en un revolver de 6 recamaras. el programa debe gestionar eventos aleatorios pausasde ejecucion para mejorar la experiencia del usuario"""

"""
2 requerimientos tecnicos: 
el algoritmo debe cumplir con los siguientes requisitos:
inicializacion: definir una recamara ganadora (bala) de forma aleatoria entre 1 y 6

bucle de juego : el usuario : el usuRIO DEBE INTERACTUAR  manualmente (while)para girar el tambor y disparar
mecanica de azar : en cada turno ,la posicion de la recamara que queda al frente al percutor  debe ser aleatoria , simulando el giro del tambor 
condicion de derrota :simla recamara seleccionada coincide con la de la bala , el programa termina inmediatamente

condicion de victoria : el jugador gana si logra sobrevivir a 5 intentos (ya que el sexto intento seria el fatal)"""


import random,time

print("="*50)
print( "bienvenidos a la ruleta rusa")
print("="*50)

input("poner bala en el tambor (presione enter)")
bala = random.randint(1, 6)  
time.sleep(0.5)

disparos = 0

while True:
    input("girar el tambor ( presiona enter)")
    recamara = random.randint(1, 6)

    input("apuntar y disparar (presiona enter)")
    time.sleep(1)

    if recamara == bala:
        print("¡Bang! Has perdido. La bala estaba en la recamara" "numero",bala)
        break
    else:
        disparos += 1
        print(" Has sobrevivido a este intento.")
        print("Intentos de disparos:", disparos)

    if disparos == 5:
        print("¡Felicidades! Has ganado. Has sobrevivido a 5 intentos.")
        break

print("="*50)
print("fin del juego-gracias por jugar") 
print("="*50)   



