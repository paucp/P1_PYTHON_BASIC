from random import randrange

# Funcion que dadas las jugadas de la ia y jugador devuelve el ganador -1 = empate, 0 = ai, 1 = jugador]
def playWinner(aiPlay, playerPlay):
    if aiPlay == playerPlay:
        return -1
    if aiPlay == 0:
        return int(playerPlay == 2)
    if aiPlay == 1:
        return int(playerPlay == 0)
    if aiPlay == 2:
        return int(playerPlay == 1)

# Juego de piedra papel tijera, el usuario escoge una opcion y se enfrenta a una IA
def playGame():
    print("****************************************")
    aiPoints, playerPoints = 0
    playerPoints = 0
    plays = ["tijera","papel","piedra"]
    
    
    # Se juega mientras ni el jugar ni la IA tengan 3 victorias
    while(aiPoints < 3 and playerPoints < 3):
        
        # Se lee una jugada valida del jugador y se genera una aleatoria para la IA
        playerPlay = input("Introduce tu jugada [tijera,papel,piedra]: ")
        while(playerPlay not in plays):
            print("Opcion invalida")
            playerPlay = input("Introduce tu jugada [tijera,papel,piedra]: ")
        aiPlay = randrange(3)
        print("La IA ha escogido " + plays[aiPlay])
        
        # Se calcula el ganador y se añade el punto
        winner = playWinner(aiPlay,plays.index(playerPlay))
        if winner == -1:
            print("Empate")
        elif winner == 0:
            print("La IA gana la jugada")
            aiPoints += 1
        else:
            print("Has ganado la jugada")
            playerPoints += 1 
        print("Jugador [" , playerPoints ,"] - [" , aiPoints , "] IA")
    
    if aiPoints == 3: print("La IA ha ganado la partida!")
    else: print("Has ganado la partida!")
        