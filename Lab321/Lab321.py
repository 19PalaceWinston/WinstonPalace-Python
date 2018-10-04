#Main start
def main():
    print("Bellarmine Student current grade point average")
    gradeNum = int(input("What grade are you in? - "))
    print("Congrats you are a", schoolYear(gradeNum))
    grades = [86.5, 75.3, 98.9, 92.3]
    gradeLength = len(grades)
    print("Your current average gade is -",round(avgGrade(grades, gradeLength),2))
    print("Your current Letter Grade is a -",letterGrade(grades, gradeLength))
    print(gradeCheck(grades, gradeLength))

#returns what grade you are in based on number
def schoolYear(gradeNum):
    if gradeNum == 9:
        return "Freshman"
    elif gradeNum == 10:
        return "Sophomore"
    elif gradeNum == 11:
        return "Junior"
    elif gradeNum == 12:
        return "Senior"
    else:
        return "not in Highschool"

#returns average grade
def avgGrade(grades,gradeLength):
    totalGrade = 0;
    for x in range (gradeLength):
        totalGrade = totalGrade + grades[x]
    return totalGrade/gradeLength

#returns letter grade
def letterGrade(grades,gradeLength):
    grade = avgGrade(grades,gradeLength)
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    else:
        return "F"

#returns if you are passing
def gradeCheck(grades, gradeLength):
    letGrade = letterGrade(grades, gradeLength)
    if letGrade == "A" or letGrade == "B" or letGrade == "C":
        return "Congratulations you are passing"
    else:
        return "You better get to work - you are failing"

main()

