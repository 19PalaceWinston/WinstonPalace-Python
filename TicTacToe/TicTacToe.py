def main(top1, top2, top3, mid1, mid2, mid3, bot1, bot2, bot3):
    print("Type Cordinates for for move , Player will always be X's\n Example: 1,1 \n")
    print("   |   |  ")
    print("-----------")
    print("   |   |  ")
    print("-----------")
    print(" X |   |  ")
    start(top1, top2, top3, mid1, mid2, mid3, bot1, bot2, bot3)

def roboStart(top1, top2, top3, mid1, mid2, mid3, bot1, bot2, bot3):
    x = 2

def start2(top1, top2, top3, mid1, mid2, mid3, bot1, bot2, bot3):
    player = input("Enter your coordinates")
    x,y = player.split(",")
    x = int(x)
    y = int(y)
    if y == 1:
        if x == 1:
            bot1 = " O "
        if x == 2:
            bot2 = "| O |"
        if x == 3:
            bot3 = " O "
    if y == 2:
        if x == 1:
            mid1 = " O "
        if x == 2:
            mid2 = "| O |"
        if x == 3:
            mid3 = " O "
    if y == 3:
        if x == 1:
            top1 = " O "
        if x == 2:
            top2 = "| O |"
        if x == 3:
            top3 = " O "
    print(top1 + top2 + top3 + "\n-----------\n"+ mid1 + mid2 + mid3 + "\n-----------\n" + bot1 + bot2 + bot3)
    start(top1, top2, top3, mid1, mid2, mid3, bot1, bot2, bot3)

def start(top1, top2, top3, mid1, mid2, mid3, bot1, bot2, bot3):
    player = input("Enter your coordinates")
    x,y = player.split(",")
    x = int(x)
    y = int(y)
    if y == 1:
        if x == 1:
            bot1 = " X "
        if x == 2:
            bot2 = "| X |"
        if x == 3:
            bot3 = " X "
    if y == 2:
        if x == 1:
            mid1 = " X "
        if x == 2:
            mid2 = "| X |"
        if x == 3:
            mid3 = " X "
    if y == 3:
        if x == 1:
            top1 = " X "
        if x == 2:
            top2 = "| X |"
        if x == 3:
            top3 = " X "
    print(top1 + top2 + top3 + "\n-----------\n"+ mid1 + mid2 + mid3 + "\n-----------\n" + bot1 + bot2 + bot3)
    start2(top1, top2, top3, mid1, mid2, mid3, bot1, bot2, bot3)
top1 = "   "
top2 = "|   |"
top3 = "   "
mid1 = "   "
mid2 = "|   |"
mid3 = "   "
bot1 = "   "
bot2 = "|   |"
bot3 = "   "
main(top1, top2, top3, mid1, mid2, mid3, bot1, bot2, bot3)
