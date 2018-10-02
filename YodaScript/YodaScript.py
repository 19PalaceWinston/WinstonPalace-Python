import random

def main():
    y = "true"
    while y == "true":
        x = input("Seek Wisdom ")
        if x == "quit":
            quit()
        yodaBot()
        print()

def yodaBot():
    rand = random.randint(1,7)
    print("Yoda:")
    if rand == 1:
        print("Do or do not do, there is no try")
    elif rand == 3:
        print("May the force be with you")
    elif rand == 4:
        print("Train yourself to let go of everything you fear to lose.")
    elif rand == 5:
        print("Death is a natural part of life. Rejoice for those around you who transform into the Force. \nMourn them do not. Miss them do not. Attachment leads to jealously. \nThe shadow of greed, that is.")
    elif rand == 6:
        print("Always pass on what you have learned.")
    elif rand == 7:
        print("You will know (the good from the bad) when you are calm, at peace. Passive.\nA Jedi uses the Force for knowledge and defense, never for attack.")

main()
