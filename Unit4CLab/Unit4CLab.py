def main():
    draw7()
    starsAndStripes()
    incTriangle()
    bonusOne()
    bonusTwo()

def draw7():
    y = 7
    x = 7
    list = ""
    for z in range(0,x):
        list = list + "*"
    for c in range(0,y):
        print(list)
    print()

def starsAndStripes():
    y = 7
    x = 7
    listStars = ""
    listStripes = ""
    for z in range(0,x):
        listStars = listStars + "*"
        listStripes = listStripes + "-"
    for c in range(0,3):
        print(listStars)
        print(listStripes)
    print()

def incTriangle():
    y = 7
    x = 1
    list = ""
    for z in range(0,7):
        for c in range(0,x):
            list = list + str(x)
        print(list)
        x = x+1
        list = ""
    print()

def bonusOne():
    for z in range(0,7):
        print("*",end="")
        for c in range(0,6):
            if z == 0 or z == 6:
                print("*",end="")
            else:
                print("-",end="")
        print("*")


def bonusTwo():
    y = 7
    x = 1
    list = ""
    for z in range(0,8):
        for c in range(1,x):
            list = list + str(c)
        print(list)
        x = x+1
        list = ""
    x = 7
    for z in range(0,7):
        for c in range(1,x):
            list = list + str(c)
        print(list)
        x = x-1
        list = ""
    print()

main()
