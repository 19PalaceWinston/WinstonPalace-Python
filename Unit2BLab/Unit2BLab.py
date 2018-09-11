numGrade = int(input("Type a Grade"))
print(numGrade)
if numGrade >= 90:
    print("Yahoo you got an A!")
elif numGrade >= 80:
    print("Good you got a B!")
elif numGrade >= 70:
    print("Okay you got a C!")
else:
    print("You better study harder")

userInput = input("Whats your favorite color?")
color = userInput
print(userInput)
userInput = userInput.lower()
if userInput == "blue":
    print("The sky is blue")
elif userInput == "green":
    print("the Forest is green")
elif userInput == "red":
    print("I love red")
elif userInput == "yellow":
    print("Yuck yellow")
else:
    print("I am a dumb computer - I don't know " + color)

