import random

def Piedra_Papel_Tijera():
    def jugar():
        print()
        print()
        print("=========================================================")
        print("     ¡Bienvenido(a) al juego Piedra, Papel y Tijera!     ")
        print("=========================================================")
        print()
        print()
        
        jugador=input("    -->--> Escribe una opción que deseas: 'Pi' para piedra, 'Pa' para papel, 'Ti' para tijera. <--<--\n    ").lower()
        print()
        maquina=random.choice(['Pi', 'Pa', 'Ti'])

        if jugador==maquina:
            return print("   ¡Bueno! Empate    ")

        if ganó_el_jugador(jugador, maquina):
            return print("    ¡Wao! Ganaste    ")

        return print("    ¡Oh no! Perdiste    ")
    print()

    def ganó_el_jugador(jugador, maquina):
        # Retornar True (verdadero) si gana el jugador.
        # Piedra gana a Tijera (pi > ti).
        # Tijera gana a Papel (ti > pa).
        # Papel gana a Piedra (pa > pi).
        if ((jugador == 'Pi' and maquina == 'Ti')
            or (jugador == 'Ti' and maquina == 'Pa')
            or (jugador == 'Pa' and maquina == 'Pi')):
            return True
        else:
            return False

    print(jugar())
    print()