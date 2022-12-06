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
        
        usuario=input("    -->--> Escribe una opción que deseas: 'P' para piedra, 'Pa' para papel, 'T' para tijera. <--<--\n    ").lower()
        print()
        computadora=random.choice(['P', 'Pa', 'T'])

        if usuario==computadora:
            return print("   ¡Bueno! Empate    ")

        if ganó_el_usuario(usuario, computadora):
            return print("    ¡Wao! Ganaste    ")

        return print("    ¡Oh no! Perdiste    ")
    print()

    def ganó_el_usuario(usuario, computadora):
        # Retornar True (verdadero) si gana el jugador.
        # Piedra gana a Tijera (pi > ti).
        # Tijera gana a Papel (ti > pa).
        # Papel gana a Piedra (pa > pi).
        if ((usuario == 'P' and computadora == 'T')
            or (usuario == 'T' and computadora == 'Pa')
            or (usuario == 'Pa' and computadora == 'P')):
            return True
        else:
            return False

    print(jugar())
    print()

    """from menu import pedirNumero 
    def volver_a_jugar():
        print()
        print("            Elige")
        print("       1. Volver a jugar")
        print("       2. Menu Principal")
        print()
        opcion=0
        opcion=int(input("             -->"))
        if opcion == 1:
            Piedra_Papel_Tijera()
                        
        elif opcion == 2:
            pedirNumero() 
    print(volver_a_jugar())"""