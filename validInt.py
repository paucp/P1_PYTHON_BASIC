# Funcion para leer un numero por pantalla
def inputValidInt(str):
    num = input(str)
    while(not num.isnumeric()):
        print("El valor introducido no es un numero")
        num = input(str)
    return int(num)