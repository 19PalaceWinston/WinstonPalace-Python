import random
def schoolSub():
    print("Bellarmine, Python")

def asks():
    x = int(input("What numerical grade are you in?"))
    print("You've be going to school for", x, "years")
def city():
    y = input("What city are you from and what grade are you in?")
    recieve(y)
def recieve(y):
    print(y)
def twoNumbers(z,a):
    print(random.randint(z,a))
def box(b,c):
    return b*c
schoolSub()
asks()
city()
z = int(input("Type a Number"))
a = int(input("Type another Number"))
twoNumbers(z,a)
b = int(input("What is the length of a box?"))
c = int(input("What is the width of a box?"))
print(box(b,c))

