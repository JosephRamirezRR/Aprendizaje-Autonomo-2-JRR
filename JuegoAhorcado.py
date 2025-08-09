#Juego ahorcado
import random    #importamos biblioteca random para que el codigo pueda elegir variables de forma aleatoria

def GetRandomWord():
    words = ["computador","teclado","lapiz","botella","pantalla","guitarra","celular","comida","hogar","parangaricutirimicuaro"]    #definimos variable "words" insertando palabras a decicion procpia
    random_word = random.choice(words)    #defino random_word para darle una seleccion aleatoria a travez de la bibilioteca que inserte antes
    return random_word    #Se devuelve la palabra selecionada
#Aqui empezamos con el tablero, donde mostraremos que palabras el usuario va acertando y cuales no
def ShowBoard(secret_word, letters_guesed):
    board=""    #variable para definir el tablero
    for letter in secret_word:    #Aqui es donde se muestra cada letra registrada
        if letter in letters_guesed:    #Aqui asignamos la accion que se va a realizar si la letra introducida al juego coincide con la aleatoria del juego
            board += letter    #Mostramos el proceso
        else:
            board += "_"    #Aqui si la letra no fue adivinada mosntramos un guion
    print(board)    #Mostramos el estado del tablero

def game_ahorcado():
    secret_word= GetRandomWord()    Obtenemos la palabra secreta aleatoria
    letter_guesed=[]    #Los corchetes representan la lista donde se almacenan las letras que ingrese el jugador
    lifes = 6    #Vidas o intentos disponibles que tiene el jugador
#Aqui inserte un bucle para que: mientras el usuario tenga vidas el codigo le permita ingresar mas letras
    while lifes >0:
        ShowBoard(secret_word, letter_guesed)    #Se muestra el estado del tablero
        letter=input("Coloca una letra:  ")    #se le solicita al usuario ingresar una letra

        if letter in letter_guesed:    #le damos una accion para cuando el usuario repita la palabra
            print("Esa letra ya estaba introducida")    #le mostramos al jugador un mensaje de advertencia
            continue    #se continua el juego sin descontar vidas
        if letter in secret_word:    #definimos accion si la letra ingresada esta en la palabra aleatoria secreta
            letter_guesed.append(letter)    #se anade a la lista de palabras adivinadas
            if set(letter_guesed)== set(secret_word):    #accion de cuando el jugador adivine todas las palabras
                print("Muchas felicidades, has ganado!")    # se printea un mensaje de felicitacion
                break    #termina el juego
        else:
            lifes-=1    #si el jugador no acerto la palabra se le resta una vida
            print(f"Esa letra era incorrecta.   VIDAS:{lifes}")     #se muestran los intentos restantes
    if lifes == 0:    #se define accion de si el usuario se queda sin vidas
        print(f"Perdiste, la palabra secreta era:{secret_word}")    #se le muestra la palabra secreta al usuario
#funcion para iniciar juego
game_ahorcado()
#este codigo no detecta mayusculas, pero creo q es posible asignarlo, de momento esto es lo que tengo
