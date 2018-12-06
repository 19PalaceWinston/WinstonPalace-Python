
def main():
    myPet1 = pet("Dog","Gracie","Great Dane")
    print(myPet1.pName)
    print(myPet1.petType)
    myPet1.whatIsIt()
    myPet2 = pet("Cat","River","Ragdoll")
    print(myPet2.pName)
    print(myPet2.petType)
    myPet2.whatIsIt()
    myCage1 = cage("snake","True")
    print(myCage1.cType)
    print(myCage1.petType)
    myCage1.whatDanger()
    myCage2 = cage("rat","False")
    print(myCage2.cType)
    print(myCage2.petType)
    myCage2.whatDanger()



class pet:
    petType = "cage free pet"

    def __init__(self,type,name,breed):
        self.pType = type
        self.pName = name
        self.pBreed = breed

    def whatIsIt(self):
        print(self.pType,self.pName,self.pBreed)

class cage:
    petType = "caged pet"

    def __init__(self,type,danger):
        self.cType = type
        self.cDanger = danger

    def whatDanger(self):
        if self.cDanger == "True":
            print("danger")
        if self.cDanger == "False":
            print("no danger")

main()
