print()     
print("================================================")
print("       ¡Bienvenida a Jueglon!     ")
print("   Sé Genial, Sé amante a los juegos  ")
print("================================================")
print()
print()
print()

def pedirNumero():
    correcto=False
    num=0
    while(not correcto):
        print()
        print()
        num=int(input("      Elige un número:       "))
        correcto=True
    return num
salir=False
opcion=0

while not salir:
    print()
    print()
    print ("     --->---> Elige tu juego favorito <---<---     ")
    print ("              1) Ahorcado")
    print ("              2) 3 en raya")
    print ("              3) Piedra, Papel o Tijera")
    print ("              4) Salir")
 
    opcion=pedirNumero()
    
    from juego1 import *
    from juego2 import *
    from juego3 import * 

    if opcion == 1:
       juego_ahorcado()
    elif opcion == 2:
        juegoEjecutar()
    elif opcion == 3:
       Piedra_Papel_Tijera()
    elif opcion == 4:
        salir = True
    else:
        print ("      Introduce un numero entre 1 al 4      ")
 
print()
print("================================================")
print("      Gracias por jugar, Vuelva Pronto      ")
print("================================================")
print()
