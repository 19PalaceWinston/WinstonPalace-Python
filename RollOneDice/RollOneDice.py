import random

def main():
    gameNum = 1
    dice1 = ["---------","|       |","|   *   |","|       |","---------"]
    dice2 = ["---------","|       |","| *   * |","|       |","---------"]
    dice3 = ["---------","| *     |","|   *   |","|     * |","---------"]
    dice4 = ["---------","| *   * |","|       |","| *   * |","---------"]
    dice5 = ["---------","| *   * |","|   *   |","| *   * |","---------"]
    dice6 = ["---------","| *   * |","| *   * |","| *   * |","---------"]
    dice = [dice1,dice2,dice3,dice4,dice5,dice6]
    for x in range (0,len(dice[0])):
        for y in range (0,len(dice)):
            print(dice[y][x],end=" ")
        print()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    roll(dice,gameNum)

def roll(dice,gameNum):
    print("Game #" + str(gameNum))
    gameNum = gameNum+1
    gameName = input("What game would you like to play?\n#1 - ManyDice\n#2 - Challenge1\n#3 - Challenge2\n")
    print()
    if gameName == "1" or str.lower(gameName) == "manydice":
        manyDice(dice)
    if gameName == "2" or str.lower(gameName) == "challenge1":
        challenge1(dice)
    if gameName == "3" or str.lower(gameName) == "challenge2":
        challenge2(dice)
    print()
    ans = input("Would you like to roll again - y or n - ")
    if ans == "y":
        print("\n~~~~~~~~~\n")
        roll(dice,gameNum)

def manyDice(dice):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    many = int(input("How many dice do you want to roll? - "))
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

def challenge1(dice):
    num1 = int(input("Type First Number - "))-1
    num2 = int(input("Type Second Number - "))-1
    dieNum = [random.randint(0,5),random.randint(0,5)]
    rolls = 0
    done = "false"
    while done == "false":
        if dieNum[0] != num1 and dieNum[0] != num2:
            dieNum[0] = random.randint(0,5)
        if dieNum[1] != num1 and dieNum[1] != num2:
            dieNum[1] = random.randint(0,5)
        if num1 != num2:
            if dieNum[0] == dieNum[1]:
                if dieNum[0] == num1 or dieNum[0] == num2:
                    dieNum[1] = random.randint(0,5)
                else:
                    dieNum[0] = random.randint(0,5)
        for z in range(0,len(dice[0])):
            for y in range(0,2):
                print(dice[dieNum[y]][z],end=" ")
            print()
        rolls = rolls + 1
        if (num1 == dieNum[0] and num2 == dieNum[1]) or (num1 == dieNum[1] and num2 == dieNum[0]):
            done = "true"
    print("Rolls:",rolls)

def challenge2(dice):
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    eleven = 0
    twelve = 0
    many = 2000
    dieNum = []
    for q in range(0,many):
        dieNum.append(random.randint(0,5))
    for b in range(0,len(dieNum)-1,2):
        current = dieNum[b] + dieNum[b+1] + 2
        if current == 2:
            two = two + 1
        if current == 3:
            three = three + 1
        if current == 4:
            four = four + 1
        if current == 5:
            five = five + 1
        if current == 6:
            six = six + 1
        if current == 7:
            seven = seven + 1
        if current == 8:
            eight = eight + 1
        if current == 9:
            nine = nine + 1
        if current == 10:
            ten = ten + 1
        if current == 11:
            eleven = eleven + 1
        if current == 12:
            twelve = twelve + 1
        current = 0

    for z in range(0,len(dice[0])):
        for y in range(0,many):
            print(dice[dieNum[y]][z],end=" ")
        print()
    print()
    print("\nTwo:",two,"\nThree:",three,"\nFour",four,"\nFive",five,"\nSix:",six,"\nSeven:",seven,"\nEight:",eight,"\nNine:",nine,"\nTen:",ten,"\nEleven:",eleven,"\nTwelve:",twelve)

main()
