import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_visual

def juego_ahorcado():
    def obtener_palabra_válida(palabras):
        palabra = random.choice(palabras)  #Selecciona una palabra al azar de la lista
        while '-' in palabra or ' ' in palabra: #Si la palabra contiene un guión o un espacio
            palabra = random.choice(palabras)
        return palabra.upper()

    def ahorcado():
        print()
        print()
        print("=======================================")
        print(" ¡Bienvenido(a) al juego del Ahorcado! ")
        print("=======================================")
        print()
        print()

        palabra = obtener_palabra_válida(palabras)
        letras_por_adivinar = set(palabra)  #Conjunto de letras de la palabra que deben ser adivinadas.
        abecedario = set(string.ascii_uppercase) #Conjunto de letras en el abecedario.
        letras_adivinadas = set()

        vidas = 7
        
        while len(letras_por_adivinar) > 0 and vidas > 0: #Letras pendientes y vidas que le quedan al jugador.
            print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}") #Letras adivinadas
            print("================================================")
            print()

            palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra] #Estado actual de la palabra que el jugador debe adivinar (por ejemplo:  H - L A)
            print(vidas_visual[vidas]) #Mostrar el dibujo visual de vidas.
            print(f"Palabra: {' '.join(palabra_lista)}") #Letras separadas

            letra_usuario = input('Escoge una letra: ').upper()

            if letra_usuario in abecedario - letras_adivinadas:  #Si la letra escogida por el usuario está en el abecedario y no está en grupo de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas.
                letras_adivinadas.add(letra_usuario)
                if letra_usuario in letras_por_adivinar: #Si la letra ya está en la palabra, quitarla del grupo de letras que faltan por adivinar. 
                    letras_por_adivinar.remove(letra_usuario)
                    print('')
                else:
                    vidas = vidas - 1
                    print(f"\nTu letra, {letra_usuario} no está en la palabra.")
                    print("================================================")
                    print()
            elif letra_usuario in letras_adivinadas:
                print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
            else:
                print("\nEsta letra no es correcta.")

        if vidas == 0:
            print(vidas_visual[vidas])
            print(f"¡Oh no, Perdiste!  La palabra era: {palabra}") 
        else:
            print(f'¡Ganaste! ¡Adivinaste la palabra {palabra}!')

    print(ahorcado())
    print ()
    print ()
