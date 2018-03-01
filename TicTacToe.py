#! python
import sys
import random
import time
def printBoard(board):
    visual = []
    for i in board:
        visual.append(i)
    for i in range (0,9):
        if visual[i] == '':
            visual[i] = str(i)

    print('|-----------|')
    print('|   |   |   |')
    print('| ' + visual[0] + ' | ' + visual[1] + ' | ' + visual[2] + ' |')
    print('|   |   |   |')
    print('|-----------|')
    print('|   |   |   |')
    print('| ' + visual[3] + ' | ' + visual[4] + ' | ' + visual[5] + ' |')
    print('|   |   |   |')
    print('|-----------|')
    print('|   |   |   |')
    print('| ' + visual[6] + ' | ' + visual[7] + ' | ' + visual[8] + ' |')
    print('|   |   |   |')
    print('|-----------|')
	
def whoGoFirst():
    if random.randint(0,1)==0:
        return 'computer'
    else:
     return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def boardCopy(board):
    copy = []
    for i in board:
        copy.append(i)
    return copy

def isWinner(b,l):
    #b = board, l=letter
    return((b[0] == l and b[1] == l and b[2] == l) or
    (b[3] == l and b[4] == l and b[5] == l) or
    (b[6] == l and b[7] == l and b [8] == l) or
    (b[0] == l and b[3] == l and b[6] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[3] == l and b[5] == l and b[8] == l) or
    (b[0] == l and b[4] == l and b[8] == l) or
    (b[2] == l and b[4] == l and b[6] == l))

def isSpaceFree(board, move):
    return board[move] == ''

def getPlayerMove(board):
    move = ''
    while move not in '0 1 2 3 4 5 6 7 8'.split(" ") or not isSpaceFree(board, int(move)):
        print('Make a move (0-8)')
        move = input()
    return int(move)

def chooseRandomMove(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def computerMove(board):
    for i in range (0,9):
        copy = boardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,'O',i)
            if isWinner(copy,'O'):
                return i
    for i in range(0,9):
        copy = boardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy,'X', i)
            if isWinner(copy,'X'):
                return i
    move = chooseRandomMove(board, [0,2,6,8])
    if move!= None:
        return move
    if isSpaceFree(board,5):
        return 5
    return chooseRandomMove(board, [1,3,5,7])
        
def isBoardFull(board):
    for i in range(0,9):
        if isSpaceFree(board,i):
            return False
    return True



#Running the game

while True:
    board = [''] * 9
    PLAYERLETTER = 'X'
    COMPUTERLETTER = 'O'
    turn = whoGoFirst()
    print('The ' + turn + ' will go first.')
    print('To make a move, enter the number of the tile you wish to fill.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            printBoard(board)
            move = getPlayerMove(board)
            makeMove(board,'X', move)

            if isWinner(board, 'X'):
                printBoard(board)
                print('Nice job! You won!')
                gameIsPlaying = False

            else:
                if isBoardFull(board):
                    printBoard(board)
                    print('Looks like it\'s a tie!')
                    break
                else:
                    turn = 'computer'
            printBoard(board)
            time.sleep(1)
            print("Hmmm...")
            time.sleep(2)
        else:
            move = computerMove(board)
            makeMove(board,'O', move)
            if isWinner(board, 'O'):
                printBoard(board)
                print('Hah! I have outsmarted the human!')
                gameIsPlaying = False
				
            else:
                if isBoardFull(board):
                    printBoard(board)
                    print('Looks like it\'s a tie!')
                    break
                else:
                    turn = 'player'
    print("Do you want to play again? (Yes or No)")
    answer = input().upper()
    if answer == 'NO':
        break
















