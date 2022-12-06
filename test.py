#Juego Tres En Raya

import os
import time
import random

####################### Funciones #######################

def juego_2():

    def presentacion_0():

        #Escoger el tipo de juego
        print("                      \u001b[34m\u001b[1mTRES EN RAYA\u001b[0m")
        print()
        print()
        print("                      1. Un Jugador")
        print("                      2. Multijugador")
        print()
        print()
        print()

        tipo_de_juego = ""
        while tipo_de_juego != 1 and tipo_de_juego != 2:
            tipo_de_juego = input("                      -->")
            return int(tipo_de_juego)


    def presentacion_4():

        #Nombre de los jugadores
        print("                      \u001b[34m\u001b[1mTRES EN RAYA\u001b[0m")
        print()
        print()
        jugador = input("                      Nombre Jugador  = ")

        return jugador


    def presentacion_3():

        #Nombre de los jugadores
        print("                      \u001b[34m\u001b[1mTRES EN RAYA\u001b[0m")
        print()
        print()
        jugador1 = input("                      Nombre Jugador 1 = ")
        jugador2 = input("                      Nombre Jugador 2 = ")

        return jugador1, jugador2


    def presentacion_1():

        #Escoger el nivel
        print("                      \u001b[34m\u001b[1mTRES EN RAYA\u001b[0m")
        print()
        print()
        print("                      1. Fácil")
        print("                      2. Difícil")
        print()
        print()
        print()

        nivel = ""
        while nivel != 1 and nivel != 2:
            nivel = input("                      -->")
            return int(nivel)


    def presentacion_2():

        print("                      \u001b[34m\u001b[1mTRES EN RAYA\u001b[0m")
        print()
        print()
        print("                      Elige: O / X")
        print()
        print()
        print()

        ficha = 'P'
        while ficha != 'O' and ficha != 'X':
            ficha = input("                      -->").upper()
        if ficha == 'O':
            humano = '\u001b[1m\u001b[36mO\u001b[0m'
            ordenador = '\u001b[1m\u001b[31mX\u001b[0m'
        else:
            humano = '\u001b[1m\u001b[31mX\u001b[0m'
            ordenador = '\u001b[1m\u001b[36mO\u001b[0m'

        return humano, ordenador


    def mostrar_tablero(tablero):
        #Muestra el tablero de juego con las casillas vacias y las fichas puestas

        print("                      \u001b[34m\u001b[1mTRES EN RAYA\u001b[0m")
        print()
        print("         1           |2           |3")
        print("               {}     |      {}     |      {}".format(
            tablero[0], tablero[1], tablero[2]))
        print("                     |            |")
        print("         ------------+------------+------------")
        print("         4           |5           |6")
        print("               {}     |      {}     |      {}".format(
            tablero[3], tablero[4], tablero[5]))
        print("                     |            |")
        print("         ------------+------------+------------")
        print("         7           |8           |9")
        print("               {}     |      {}     |      {}".format(
            tablero[6], tablero[7], tablero[8]))
        print("                     |            |")
        print()
        print()


    def seguir_jugando():
        #Devuelve True si el usuario quiere echar otra partida

        print()
        respuesta = input("            ¿Otra partida (si o no)?").lower()
        if respuesta == 'S' or respuesta == 's' or respuesta == 'si' or respuesta == 'Si' or respuesta == 'Sí' or respuesta == 'SI' or respuesta == 'SÍ':
            return True
        else:
            return False


    def revancha_1():
        #Devuelve True si el usuario quiere echar otra partida

        print()
        respuesta = input("            ¿Revancha (si o no)?").lower()
        if respuesta == 'S' or respuesta == 's' or respuesta == 'si' or respuesta == 'Si' or respuesta == 'Sí' or respuesta == 'SI' or respuesta == 'SÍ':
            if revancha == 0:
                return 1
            else:
                return 0
        else:
            return 2


    def casillas_ocupadas(tablero):
        #True si las casillas estan ocupadas
        a = 0
        for i in tablero:
            if i == " ":
                a = a + 1
        if a == 0:
            return True
        else:
            return False


    def hay_ganador(tablero, jugador):

        #Comprobar si alguien ha ganado

        if tablero[0] == tablero[1] == tablero[2] == jugador or \
            tablero[3] == tablero[4] == tablero[5] == jugador or \
            tablero[6] == tablero[7] == tablero[8] == jugador or \
            tablero[0] == tablero[3] == tablero[6] == jugador or \
            tablero[1] == tablero[4] == tablero[7] == jugador or \
            tablero[2] == tablero[5] == tablero[8] == jugador or \
            tablero[0] == tablero[4] == tablero[8] == jugador or \
            tablero[2] == tablero[4] == tablero[6] == jugador:
            return True
        else:
            return False


    def casilla_libre(tablero, casilla):

        #True si la casilla está vacía
        return tablero[casilla] == " "


    def movimiento_jugador(tablero, jugador1, ficha_jugador1):

        #devuelve la casilla elegido por el jugador

        posiciones = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]
        posicion = None
        while True:
            if posicion not in posiciones:
                posicion = input("             ({0}) {1} Te toca (1-9): ".format(
                    ficha_jugador1, jugador1))
            else:
                posicion = int(posicion)
                if not casilla_libre(tablero, posicion - 1):
                    print("           Esta posición está ocupada")
                else:
                    return posicion - 1


    def mov_ordenador_facil(tablero, jugador):

        #Solo se defiende de poder perder

        for i in range(9):
            copia = list(tablero)
            if casilla_libre(copia, i):
                copia[i] = jugador
                if hay_ganador(copia, jugador):
                    return i

        while True:
            casilla = random.randint(0, 8)
            if not casilla_libre(tablero, casilla):
                casilla = random.randint(0, 8)
            else:
                return casilla


    def mov_ordenador_dificil(tablero, maquina, usuario):

        for i in range(9):
            copia = list(tablero)
            if casilla_libre(copia, i):
                copia[i] = maquina
                if hay_ganador(copia, maquina):
                    return i

        for i in range(9):
            copia = list(tablero)
            if casilla_libre(copia, i):
                copia[i] = usuario
                if hay_ganador(copia, usuario):
                    return i

        if ordenador == '\u001b[1m\u001b[31mX\u001b[0m':
            if tablero[4] == " ":
                return 4
            else:
                vacias = []
                for i in [0, 2, 6, 8]:
                    if tablero[i] == " ":
                        vacias.append(i)
                return random.choice(vacias)

        if ordenador == '\u001b[1m\u001b[36mO\u001b[0m':
            contador = 0
            for i in range(9):
                if tablero[i] == " ":
                    contador += 1
            if contador == 7:
                if tablero[4] == " ":
                    return 4

        while True:
            casilla = random.randint(0, 8)
            if not casilla_libre(tablero, casilla):
                casilla = random.randint(0, 8)
            else:
                return casilla


    ####################### Programa Principal #######################

    jugando = True
    while jugando:
        tablero = [" "] * 9

        tipo_de_juego = presentacion_0()
        t = 0
        if tipo_de_juego == 1:

            jugador = presentacion_4()
            nivel = presentacion_1()
            humano, ordenador = presentacion_2()
            mostrar_tablero(tablero)

            revancha = humano
            while revancha == humano or revancha == ordenador:
                tablero = [" "] * 9
                mostrar_tablero(tablero)

                if humano == '\u001b[1m\u001b[31mX\u001b[0m':
                    turno = "humano"
                else:
                    turno = "ordenador"

                partida = True

                while partida:
                    if turno == "humano":
                        if not hay_ganador(tablero,
                                        humano) and casillas_ocupadas(tablero):
                            print("                 Empate\n\n")
                            partida = False
                        if partida:

                            casilla = movimiento_jugador(tablero, jugador, humano)
                            tablero[casilla] = humano
                            turno = "ordenador"
                            mostrar_tablero(tablero)
                            t = t + 1
                            if hay_ganador(tablero, humano):
                                print("                 {} Has Ganado\n\n".format(
                                    jugador))
                                partida = False
                    if turno == "ordenador":
                        if casillas_ocupadas(tablero):
                            print("                 Empate\n\n")
                            partida = False
                        if partida:
                            print("         El ordenador está pensando ...")
                            if nivel == 1:
                                casilla = mov_ordenador_facil(tablero, humano)
                            elif nivel == 2:
                                casilla = mov_ordenador_dificil(
                                    tablero, ordenador, humano)
                            tablero[casilla] = ordenador
                            turno = "humano"
                            mostrar_tablero(tablero)
                            t = t + 1
                            if hay_ganador(tablero, ordenador):
                                print("                 {} Has Perdido\n\n".format(
                                    jugador))
                                partida = False
                print("                 Elige")
                print("                 1) Revancha")
                print("                 2) Menu Principal")
                print()
                opcion = 0
                opcion = int(input("             -->"))
                if opcion == 1:
                    if humano == '\u001b[1m\u001b[31mX\u001b[0m':
                        humano = '\u001b[1m\u001b[36mO\u001b[0m'
                        ordenador = '\u001b[1m\u001b[31mX\u001b[0m'
                    else:
                        humano = '\u001b[1m\u001b[31mX\u001b[0m'
                        ordenador = '\u001b[1m\u001b[36mO\u001b[0m'
                else:
                    break
            jugando = 1

        else:
            
            jugador1, jugador2 = presentacion_3()
            mostrar_tablero(tablero)

            revancha = 1
            while revancha == 1 or revancha == 0:
                tablero = [" "] * 9
                mostrar_tablero(tablero)

                if revancha == 1:
                    turno = "jugador1"
                    ficha_jugador1 = '\u001b[1m\u001b[31mX\u001b[0m'
                    ficha_jugador2 = '\u001b[1m\u001b[36mO\u001b[0m'
                else:
                    turno = "jugador2"
                    ficha_jugador1 = '\u001b[1m\u001b[36mO\u001b[0m'
                    ficha_jugador2 = '\u001b[1m\u001b[31mX\u001b[0m'
                #else:
            #turno = "jugador2"

                partida = True
                while partida:
                    if turno == "jugador1":
                        if not hay_ganador(
                            tablero,
                            ficha_jugador1) and casillas_ocupadas(tablero):
                            print("                 Empate\n\n")
                            partida = False
                        if partida:
                            casilla = movimiento_jugador(tablero, jugador1,
                                                        ficha_jugador1)
                            tablero[casilla] = ficha_jugador1
                            turno = "jugador2"
                            mostrar_tablero(tablero)
                            if hay_ganador(tablero, ficha_jugador1):
                                print("                 {} Has Ganado\n\n".format(
                                    jugador1))
                                partida = False
                    if turno == "jugador2":
                        if not hay_ganador(
                            tablero,
                            ficha_jugador2) and casillas_ocupadas(tablero):
                            print("                 Empate\n\n")
                            partida = False
                        if partida:
                            casilla = movimiento_jugador(tablero, jugador2,
                                                        ficha_jugador2)
                            tablero[casilla] = ficha_jugador2
                            turno = "jugador1"
                            mostrar_tablero(tablero)
                            if hay_ganador(tablero, ficha_jugador2):
                                print("                 {} Has Ganado\n\n".format(
                                    jugador2))
                                partida = False

                #revancha= revancha_1()
                print("                 Elige")
                print("                 1) Revancha")
                print("                 2) Menu Principal")
                print()
                opcion = 0
                opcion = int(input("             -->"))
                if opcion == 1:
                    if revancha == 1:
                        revancha = 0
                    else:
                        revancha = 1
                else:
                    break
        jugando = 1
