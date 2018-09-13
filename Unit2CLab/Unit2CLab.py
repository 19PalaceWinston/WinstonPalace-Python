numlist = [0,1,2,3,4,5,6,7,8,9]
print(numlist)
print(len(numlist))
print(numlist[0], numlist[len(numlist)-1])

subList = numlist[0:4]
subList[0] = 1
subList.append(1)
subList1 = subList + [10]

myClasses = ["Python","CP","Senior Comp.","Intro to Calc"]
myClasses.remove("Senior Comp.")
favClass = myClasses.pop(0)
print("My favorite class is", favClass)
