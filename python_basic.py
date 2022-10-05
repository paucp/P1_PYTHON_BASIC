from random import randrange
import validInt
import gameAdivina
import gamePiedraPapelTijera
import gameAhorcado

#  Menu principal, permite escoger uno de los juegos
print("-------------------------------------")
print("1. Adivina numero")
print("2. Piedra papel tijeras")
print("3. Ahorcado")
print("-------------------------------------")
option = validInt.inputValidInt("Introduce opcion: ")
while option < 1 or option > 3:
    print("Opcion invalida")
    option = validInt.inputValidInt("Introduce opcion: ")
if option == 1: gameAdivina.playGame()
elif option == 2: gamePiedraPapelTijera.playGame()
elif option == 3: gameAhorcado.playGame()