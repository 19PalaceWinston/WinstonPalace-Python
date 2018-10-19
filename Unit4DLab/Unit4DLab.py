def main():
    shoppingCart = [["toothpaste","q-tips","milk"],["milk","candy","apples"],["paper","pencils","q-tips"]]
    allInOne(shoppingCart)
    countQtips(shoppingCart)
    drinkMoreMilk(shoppingCart)
    mooseCookie(shoppingCart)

def allInOne(shoppingCart):
    oneList = []
    duplicate = []
    other = []
    check = 0
    for x in range(0,len(shoppingCart)):
        for y in range(0,len(shoppingCart[x])):
            duplicate.append(shoppingCart[x][y])
    for z in range(0,len(duplicate)):
        for c in range(0,len(duplicate)):
            if duplicate[z] != duplicate[c]:
                check = check + 1
        if check == len(duplicate)-1:
            oneList.append(duplicate[z])
        else:
            other.append(duplicate[z])
        check = 0
    for b in range(0,int(len(other)/2)):
        oneList.append(other[b])
    print("List:",oneList)

def countQtips(shoppingCart):
    tips = 0
    for x in range(0,len(shoppingCart)):
        for y in range(0,len(shoppingCart[x])):
            if shoppingCart[x][y] == "q-tips":
                tips = tips + 1
    print("q-tips:", tips)

def drinkMoreMilk(shoppingCart):
    milk = 0
    for x in range(0,len(shoppingCart)):
        for y in range(0,len(shoppingCart[x])):
            if shoppingCart[x][y] == "milk":
                milk = milk + 1
        if milk < 1:
            shoppingCart[x].append("milk")
        milk = 0
    print("More Milk:",shoppingCart)

def mooseCookie(shoppingCart):
    for x in range(0,len(shoppingCart)):
        for y in range(0,len(shoppingCart[x])):
            if shoppingCart[x][y] == "milk":
                shoppingCart[x][y] = "milk and cookies"
    print("Moose Cookie:", shoppingCart)

main()
