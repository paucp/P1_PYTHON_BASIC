from random import randrange

# Muestra la palabra, "_" si la letra no se ha adivinado
def displayWord(word, guessedChars):
    for char in word:
        if char in guessedChars: print(char , end = '')
        else: print("_" , end = '')
    print("")
        
# Juego de ahorcado escoge una palabra al azar de un archivo, y el jugador intenta adivinar cada letra
def gameAhorcado():
    print("****************************************")
    file = open('words.txt', 'r', encoding="utf8")
    lines = file.read().splitlines()
    word = lines[randrange(15)].upper()
    tries = len(word)*2
    guessedChars = []
    guessedNum = 0
    
    # Se realiza un intento mientras quden restantes y no se haya adivinado todas las letras
    while tries > 0 and guessedNum < len(word):
        displayWord(word, guessedChars)
        char = input("Introduce una letra: ").upper()
        while len(char) != 1 or char.isnumeric():
            print("Opcion invalida. Tiene que ser una letra")
            char = input("Introduce una letra: ").upper()
        if char in word:
            print("La palabra contiene la letra " , char)
            guessedChars.append(char)
            guessedNum += word.count(char)
        else:
            print("La palabra no contiene la letra " , char)
            tries -= 1
        print("Intentos restantes: " , tries)
        
    print("La palabra es: " , word)
    if tries == 0: print("Se han acabado los intentos")
    else: print("Has acertado la palabra!")