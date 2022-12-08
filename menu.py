print()     
print("================================================")
print("       ¡Bienvenida!     ")
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
    print ("              2) Piedra, Papel o Tijera ")
    print ("              3) 3 en raya")
    print ("              4) Salir")
 
    opcion=pedirNumero()
    
    from juego1 import * 
    from juego3 import *
    from enraya import *

    if opcion == 1:
        juego_ahorcado()
    elif opcion == 2:
        Piedra_Papel_Tijera()
    elif opcion == 3:
        window=tk.Tk()
    elif opcion == 4:
        salir = True
    else:
        print ("      Introduce un numero entre 1 al 4      ")
 
print()
print("================================================")
print("      Gracias por jugar, Vuelva Pronto      ")
print("================================================")
print()
