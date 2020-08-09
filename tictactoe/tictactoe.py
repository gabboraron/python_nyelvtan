import os
import random

clear = lambda: os.system('cls')
board = [' ' for x in range(10)]

def insertLetter(letter,position):
    board[position] = letter

def isItFree(pos):
    return board[pos] == ' '

def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def printBoard(board):
    clear()
    print("")
    print(" "+str(board[1])+" | "+str(board[2])+" | "+str(board[3]))
    print("---+---+---")
    print(" "+str(board[4])+" | "+str(board[5])+" | "+str(board[6]))
    print("---+---+---")
    print(" "+str(board[7])+" | "+str(board[8])+" | "+str(board[9]))
    print("")

def whoIsWinner(board):
    if board[1] != ' ':
        if board[1] == board[2] == board[3]:
            return str(board[1])
        if board[1] == board[4] == board[7]:
            return str(board[1])
        if board[1] == board[5] == board[9]:
            return str(board[1])
    if board[2] != ' ':
        if board[2] == board[5] == board[8]:
            return str(board[2])
    if board[3] != ' ':
        if board[3] == board[5] == board[7]:
            return str(board[3])
        if board[3] == board[6] == board[9]:
            return str(board[3])
    if board[4] != ' ':
        if board[4] == board[5] == board[6]:
            return str(board[4])
    if board[7] != ' ':
        if board[7] == board[8] == board[9]:
            return str(board[7])
    return False

def playerMove():
    run = True
    while run == True:
        print("                                                   1 2 3")
        print("Add your next position [between 1-9] in this form: 4 5 6")
        print("                                                   7 8 9")
        position = input("your next position: ")
        try:
            position = int(position)
            if position>0 and position<10:
                if isItFree(position):
                    run = False
                    insertLetter("X", position)
                else:
                    print("\t Occupied space, choose another!")
            else:
                print("Not a valid position! Add a number between 1-9")
        except:
            print("Type a number! Add a number between 1-9")

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]

    for let in ['O', 'X']:
        for idx in possibleMoves:
            boardcp = board[:]
            boardcp[idx] = let
            if whoIsWinner(boardcp) != False:
                return idx

    openCorners = []
    for idx in possibleMoves:
        if idx in [1,3,7,9]:
            openCorners.append(idx)
    if len(openCorners) > 0:
        return selectRandom(openCorners)

    if 5 in possibleMoves:
        return 5
    edgesOpen = []
    for idx in possibleMoves:
        if idx in [2,4,6,8]:
            edgesOpen.append(idx)
    if len(edgesOpen) > 0 :
        return selectRandom(edgesOpen)

def selectRandom(list):
    ln = len(list)
    rdx = random.randrange(0,ln)
    return list[rdx]

any = True
while (whoIsWinner(board) == False):
    printBoard(board)
    if isBoardFull(board):
        print("\n\tNo one has win this game!")
        print("")
        any = False
        break
    else:
        playerMove()
        try:
            insertLetter("O", computerMove())
        except:
            print("")

if any:
    printBoard(board)
    print("\n\tThe winner is: " + whoIsWinner(board))
    print("")
