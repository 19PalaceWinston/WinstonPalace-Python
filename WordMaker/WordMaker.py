import random
def randWord(word):
    constants = ["q","w","r","t","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    vowels = ["i","e","a","o","u"]
    for y in range (len(word)):
        for x in range(20):
            if word[y] == constants[x] or word[y] == constants or word[y] == word:
                word[y] = constants[random.randint(0, 19)]
        for z in range(len(vowels)):
            if word[y] == vowels[z]:
                word[y] = vowels[random.randint(0,4)]
    newWord = ""
    for a in range (len(word)):
        newWord = newWord + word[a]
    print("New Word:", newWord)
x = 1
while x == 1:
    word = list(input("Type a word "))
    if len(word) == 4:
        if word[0]+word[1]+word[2]+word[3] == "quit":
            quit()
    randWord(word)
    print()
