import random

def main():
    gameNum = 1
    dice1 = ["---------","|       |","|   *   |","|       |","---------"]
    dice2 = ["---------","|       |","| *   * |","|       |","---------"]
    dice3 = ["---------","| *     |","|   *   |","|     * |","---------"]
    dice4 = ["---------","| *   * |","|       |","| *   * |","---------"]
    dice5 = ["---------","| *   * |","|   *   |","| *   * |","---------"]
    dice6 = ["---------","| *   * |","| *   * |","| *   * |","---------"]
    dice8 = "---------\n|       |\n|   *   |\n|       |\n---------"
    dice9 = "---------\n|       |\n| *   * |\n|       |\n---------"
    dice10 = "---------\n| *     |\n|   *   |\n|     * |\n---------"
    dice11 = "---------\n| *   * |\n|       |\n| *   * |\n---------"
    dice12 = "---------\n| *   * |\n|   *   |\n| *   * |\n---------"
    dice13 = "---------\n| *   * |\n| *   * |\n| *   * |\n---------"
    dice = [dice1,dice2,dice3,dice4,dice5,dice6]
    z = 0
    for x in range (0,len(dice)-1):
        for y in range (0,len(dice[x])):
            print(dice[z][x],end=" ")
            z = z + 1
        z = 0
        print()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    roll(dice,gameNum)

def roll(dice,gameNum):
    #rand1 = random.randint(0,5)
    #rand2 = random.randint(0,5)
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    print("Game #" + str(gameNum))
    gameNum = gameNum+1
    many = int(input("How many dice do you want to roll? - "))
    #for x in range(0,len(dice[0])):
    #    print(dice[rand1][x]+" ",end="")
    #    print(dice[rand2][x]+" ",end="")
    #    print()
    dieNum = []
    for q in range(0,many):
        dieNum.append(random.randint(0,5))
    for z in range(0,len(dice[0])):
        for y in range(0,many):
            print(dice[dieNum[y]][z],end=" ")
        print()
    for r in range(0,many):
        if dieNum[r] == 0:
            one = one + 1
        if dieNum[r] == 1:
            two = two + 1
        if dieNum[r] == 2:
            three = three + 1
        if dieNum[r] == 3:
            four = four + 1
        if dieNum[r] == 4:
            five = five + 1
        if dieNum[r] == 5:
            six = six + 1
    print()
    print("One:",one,"\nTwo:",two,"\nThree:",three,"\nFour",four,"\nFive",five,"\nSix:",six)
    print()
    ans = input("Would you like to roll again - y or n - ")
    if ans == "y":
        print("\n~~~~~~~~~\n")
        roll(dice,gameNum)

main()
