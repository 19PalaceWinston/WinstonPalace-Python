import random
def main():
    print("Type Cordinates for for move , Player will always be X's\n Example: 1,1 \n")
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print("-----------")
    print(" X |   |  ")
    play = int(input("1 or 2 Player - "))
    if play == 1 or play ==2:
        print(play,"Player Selected")
    else:
        print("Invalid Player Number")
        quit()
    usedX = []
    usedY = []
    board = ["   ","|   |", "   ", "   ", "|   |", "   ","   ", "|   |", "   ",]
    player1(board,usedX,usedY,play)

def player1(board, usedX, usedY, play):
    coords = input("Enter Your Coordinates - ").split(",")
    x = int(coords[0])
    y = int(coords[1])
    for a in range(len(usedX)):
        if x == usedX[a] and y == usedY[a]:
                print("Coordinates Already Used, Try Again")
                player1(board, usedX, usedY, play)
                return
    usedX.append(x)
    usedY.append(y)
    if x == 1:
        if y == 1:
            board[6] = " X "
        elif y == 2:
            board[3] = " X "
        elif y == 3:
            board[0] = " X "
    if x == 2:
        if y == 1:
            board[7] = "| X |"
        elif y == 2:
            board[4] = "| X |"
        elif y == 3:
            board[1] = "| X |"
    if x == 3:
        if y == 1:
            board[8] = " X "
        elif y == 2:
            board[5] = " X "
        elif y == 3:
            board[2] = " X "
    print()
    print(board[0]+board[1]+board[2]+"\n-----------\n"+board[3]+board[4]+board[5]+"\n-----------\n"+board[6]+board[7]+board[8])
    print()
    if play == 1:
        robot(board, usedX, usedY, play)
    elif play == 2:
        player2(board, usedX, usedY, play)
    else:
        quit()

def player2(board, usedX, usedY, play):
    coords = input("Enter Your Coordinates - ").split(",")
    x = int(coords[0])
    y = int(coords[1])
    for a in range(len(usedX)):
        if x == usedX[a] and y == usedY[a]:
                print("Coordinates Already Used, Try Again")
                player2(board, usedX, usedY, play)
                return
    usedX.append(x)
    usedY.append(y)
    if x == 1:
        if y == 1:
            board[6] = " O "
        elif y == 2:
            board[3] = " O "
        elif y == 3:
            board[0] = " O "
    if x == 2:
        if y == 1:
            board[7] = "| O |"
        elif y == 2:
            board[4] = "| O |"
        elif y == 3:
            board[1] = "| O |"
    if x == 3:
        if y == 1:
            board[8] = " O "
        elif y == 2:
            board[5] = " O "
        elif y == 3:
            board[2] = " O "
    print()
    print(board[0]+board[1]+board[2]+"\n-----------\n"+board[3]+board[4]+board[5]+"\n-----------\n"+board[6]+board[7]+board[8])
    print()
    player1(board, usedX, usedY, play)


def robot(board, usedX, usedY, play):
    x = random.randint(1,3)
    y = random.randint(1,3)
    for a in range(len(usedX)):
        if x == usedX[a] and y == usedY[a]:
                robot(board, usedX, usedY, play)
                return
    usedX.append(x)
    usedY.append(y)
    if x == 1:
        if y == 1:
            board[6] = " O "
        elif y == 2:
            board[3] = " O "
        elif y == 3:
            board[0] = " O "
    if x == 2:
        if y == 1:
            board[7] = "| O |"
        elif y == 2:
            board[4] = "| O |"
        elif y == 3:
            board[1] = "| O |"
    if x == 3:
        if y == 1:
            board[8] = " O "
        elif y == 2:
            board[5] = " O "
        elif y == 3:
            board[2] = " O "
    print()
    print(board[0]+board[1]+board[2]+"\n-----------\n"+board[3]+board[4]+board[5]+"\n-----------\n"+board[6]+board[7]+board[8])
    print()
    player1(board, usedX, usedY, play)

main()
