import random 

print()
print()
print("=========================================================")
print("     ¡Bienvenido(a) al juego de 3 en raya !     ")
print("=========================================================")
print()
print()

tablero = ["  -  ","  -  ","  -  ",
           "  -  ","  -  ","  -  ",
           "  -  ","  -  ","  -  " ]

jugador = "X"
ganador = False
juegoEjecutar = True

#Impresion del Tablero
def tablero_visual(tablero):
    print()
    print(" | " + tablero[0] + " | " + tablero[1] + " | " + tablero[2] + " | ")
    print("-------------------------------")
    print(" | " + tablero[3] + " | " + tablero[4] + " | " + tablero[5] + " | ")
    print("-------------------------------")
    print(" | " + tablero[6] + " | " + tablero[7] + " | " + tablero[8] + " | ")
    print()

#Entrada Jugador
def inicio_jugador(tabler_visual):
    num=int(input("Inserta movimiento del 1-9: "))
    print()
    if tablero[num-1] == "  -  ":
        tablero[num-1] = jugador
    else:
        print("Ya está ocupado ese lugar")
        print()

#Comprobacion punto de control horizontal, vertical, diagonal
def horizontal(tablero):
    global ganador
    if tablero[0] == tablero[1] == tablero[2] and tablero[0] != "  -  ":
        ganador = tablero[0]
        return True
    elif tablero[3] == tablero[4] == tablero[5] and tablero[3] != "  -  ":
        ganador = tablero[3]
        return True
    elif tablero[6] == tablero[7] == tablero[8] and tablero[6] != "  -  ":
        ganador = tablero[6]
        return True

def vertical(tablero):
    global ganador
    if tablero[0] == tablero[3] == tablero[6] and tablero[0] != "  -  ":
        ganador = tablero[0]
        return True
    elif tablero[1] == tablero[4] == tablero[7] and tablero[1] != "  -  ":
        ganador = tablero[1]
        return True
    elif tablero[2] == tablero[5] == tablero[8] and tablero[2] != "  -  ":
        ganador = tablero[3]
        return True

def diagonal(tablero):
    global ganador
    if tablero[0] == tablero[4] == tablero[8] and tablero[0] != "  -  ":
        ganador = tablero[0]
        return True
    elif tablero[2] == tablero[4] == tablero[6] and tablero[4] != "  -  ":
        ganador = tablero[2]
        return True

#Comprobación del ganador o perdedor
def verificar_ganador(tablero):
    global juegoEjecutar
    if horizontal(tablero):
        tablero_visual(tablero)
        print (f"El ganador es {ganador}!")
        juegoEjecutar = False
    
    elif vertical(tablero):
        tablero_visual(tablero)
        print(f"El ganador es {ganador}!")
        juegoEjecutar = False

    elif diagonal(tablero):
        tablero_visual(tablero)
        print(f"El ganador es {ganador}!")
        juegoEjecutar = False

def verificar_perdedor(tablero):
    global juegoEjecutar
    if "  -  " not in tablero:
        tablero_visual(tablero)
        print("¡Oh no, Empate!")
        juegoEjecutar = False

#Cambiar jugador
def cambiar_jugador():
    global jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

#Maquina
def computadora(tablero):
    while jugador == "O":
        posicion = random.randint(0, 8)
        if tablero[posicion] == "  -  ":
            tablero[posicion] = "O"
            cambiar_jugador()

while juegoEjecutar:
    tablero_visual(tablero)
    inicio_jugador(tablero)
    verificar_ganador(tablero)
    verificar_perdedor(tablero)
    cambiar_jugador()
    computadora(tablero)
    verificar_ganador(tablero)
    verificar_perdedor(tablero)
