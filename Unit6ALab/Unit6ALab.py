def check(textCodes):
    go = "true"
    while go == "true":
        ans = input("Name a text code - ")
        if ans == "/menu":
            main(textCodes)
            return
        if ans in textCodes:
            print(textCodes[ans])
        else:
            define = input("What does that mean?")
            if define == "/menu":
                main(textCodes)
                return
            textCodes[ans] = define

def change(textCodes):
    go = "true"
    while go == "true":
        print("What Text Code would you like to change?")
        print(textCodes)
        key = input("")
        if key == "/menu":
                main(textCodes)
                return
        if key in textCodes:
            text = input("Type your change\n")
            if text == "/menu":
                    main(textCodes)
                    return
            textCodes[key] = text
        else:
            print("Text Code not found, please try again")

def delete(textCodes):
    go = "true"
    while go == "true":
        print("What would you like to delete")
        print(textCodes)
        ans = input("")
        if ans == "/menu":
            main(textCodes)
            return
        if ans in textCodes:
            deleted = textCodes.pop(ans)
            print(textCodes)
            print("Done")
        else:
            print("Text Code not found, please try again")

def main(textCodes):
    designate = input("What function would you like? - check - change - delete \n")
    print("Type /menu to go back to the menu at any point")
    if designate == "check":
        check(textCodes)
    if designate == "change":
        change(textCodes)
    if designate == "delete":
        delete(textCodes)

textCodes = {"jk": "just kidding", "gtg": "got to go", "brb": "be right back"}
main(textCodes)
