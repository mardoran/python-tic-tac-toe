from random import randrange

def DisplayBoard(board):
    print("+------+------+------+")
    for fila in range(3):
        print("|      |      |      |")
        print("|  ", board[fila][0], " |  ", board[fila][1], " |  ", board[fila][2], " |")
        print("|      |      |      |")
        print("+------+------+------+")


def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    
    #metemos el input en un bloque try except para seguir pidiendo al usuario el valor hasta que teclee uno correcto
    try:
        casilla = int(input("Inserta casilla: "))
        if casilla not in range(1,10):
            raise Exception()
    except:
        print("Debes introducir un número válido (1-9).")
        EnterMove(board)
        
    #recorremos el tablero hasta encontrar el nº de casilla que ha introducido el usuario para colocar su ficha
    control = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==casilla:
                board[i][j]='O'
                control=True
    #si no se encontró la casilla es que está intentando usar una ocupada
    if not control:    
        print("Movimiento inválido.")
        EnterMove(board)           


def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    lista_tuplas=[]
    for fila in range(len(board)):
        for elem in range(len(board[fila])):
            if board[fila][elem] not in ('X','O'):
                tupla=(fila,elem)
                lista_tuplas.append(tupla)
    return lista_tuplas        


def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    for i in range(3):
        #con all comprobamos si todos los elementos de la fila son iguales
        #en la segunda comprobación comprobamos las columnas
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True

         # Verificar diagonales (los índices iguales por un lado 0-0,1-1,2-2 o 0-2,1-1,2-0)
        if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
            return True

    return False

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.   
    
    #nos devolverá una lista de tuplas disponibles
    casillas_libres = MakeListOfFreeFields(board)
    #si están todas es la primera tirada
    if len(casillas_libres)==9:
        board[1][1] = "X"
        return
    #cogemos un nº al azar entre los disponibles
    casilla = randrange(len(casillas_libres))
    #cogemos el par fila-columna de esa tupla y lo asignamos al tablero con la ficha de la máquina
    tupla_escogida=casillas_libres[casilla]
    fila=tupla_escogida[0]
    col=tupla_escogida[1]
    board[fila][col] = "X"
    

def main():
    
    #creamos la matriz del 1 al 9 que será el tablero
    tablero =[]
    cont=0
    for i in range (3):
        fila =[]
        for j in range (3):
            cont+=1
            fila.append(cont)
        tablero.append(fila)

    while True:
        #empieza la máquina
        DrawMove(tablero)
        DisplayBoard(tablero)
        if VictoryFor(tablero,'X'):
            print("La máquina gana")
            break
        #si no quedan más casillas libres es empate
        if len(MakeListOfFreeFields(tablero))==0:
            print("Empate")
            break        
        #movimiento del usuario
        EnterMove(tablero)
        DisplayBoard(tablero)
        if VictoryFor(tablero,'O'):
            print("Has ganado!")
            break           

if __name__ == "__main__":
    main()
    

