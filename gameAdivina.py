from random import randrange
import validInt

# Juego de adivinar numero
def playGame():
    print("****************************************")
    num = randrange(1, 10)
    tries = 3
    while tries > 0:
        tries -= 1
        guess = validInt.inputValidInt("Introduce numero: ")
        if(num < guess):
            print("El numero es menor")
        elif num > guess:
            print("El numero es mayor")
        else:          
            print("Has acertado!")
            return
    print("Se han acabado los intentos. El numero era" , num)