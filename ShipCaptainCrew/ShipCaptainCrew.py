import random
import sys

def main():
    gameNum = 1
    dice1 = ["---------","|       |","|   *   |","|       |","---------"]
    dice2 = ["---------","|       |","| *   * |","|       |","---------"]
    dice3 = ["---------","| *     |","|   *   |","|     * |","---------"]
    dice4 = ["---------","| *   * |","|       |","| *   * |","---------"]
    dice5 = ["---------","| *   * |","|   *   |","| *   * |","---------"]
    dice6 = ["---------","| *   * |","| *   * |","| *   * |","---------"]
    playerCount = input("How many players? ")
    die = []
    dice = [dice1,dice2,dice3,dice4,dice5,dice6]
    for x in range(0,int(playerCount)):
        die.append([])
        for y in range(0,5):
            die[x].append(random.randint(0,5))
    currentPlayer = 1
    print("Player:",currentPlayer)
    print("Roll:",gameNum)
    print("    1         2         3         4         5")
    for z in range(0,len(dice[0])):
        for b in range(0,5):
            print("",end="")
            print(dice[die[currentPlayer-1][b]][z],end=" ")
        print()
    roll(dice,die,gameNum,currentPlayer,playerCount)

def roll(dice,die,gameNum,currentPlayer,playerCount):
    gameNum = gameNum + 1
    print("Which dice to you want to re-roll?")
    print("Example: 1,4,5")
    ans = input("Re-roll: ")
    re = ans.split(",")
    for x in range(0,len(re)):
        if re[x] == " ":
            re[x] = ""
    print()
    for y in range(0,len(re)):
        die[currentPlayer-1][int(re[y])-1] = random.randint(0,5)
    print("Player:", currentPlayer)
    print("Roll:",gameNum)
    print("    1         2         3         4         5")
    for z in range(0,len(dice[0])):
        for b in range(0,5):
            print(dice[die[currentPlayer-1][b]][z],end=" ")
        print()
    if gameNum == 3:
        if int(currentPlayer) >= int(playerCount):
             end(die)
             return
        gameNum = 0
        currentPlayer = currentPlayer+1
        print()
        print("=========")
        print("PLAYER:",currentPlayer)
        print("=========")
        print()
        for z in range(0,len(dice[0])):
            for b in range(0,5):
                print("",end="")
                print(dice[die[currentPlayer-1][b]][z],end=" ")
            print()
        roll(dice,die,gameNum,currentPlayer,playerCount)
    else:
        roll(dice,die,gameNum,currentPlayer,playerCount)

def end(die):
    scores = []
    temp = 0
    six = "false"
    five = "false"
    four = "false"
    for x in range(0,len(die)):
        for y in range(0,len(die[x])):
            temp = temp+die[x][y]+1
            if die[x][y]+1 == 6:
                six = "true"
            if die[x][y]+1 == 5:
                five = "true"
            if die[x][y]+1 == 4:
                four = "true"
        if six != "true" or five != "true" or four != "true":
            temp = 0
        scores.append(temp)
        temp = 0
        six = "false"
        five = "false"
        four = "false"
    print("Scores:")
    for z in range(0,len(scores)):
        if scores[z] != 0:
            print("Player",str(z+1)+":",scores[z])
        if scores[z] == 0:
            print("Player",str(z+1)+" failed to set up their ship!")

main()
