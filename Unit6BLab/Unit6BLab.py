
def main(weekends):
    month = input("What month is you birth day in? - ")
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
    monthNum = 0
    if int(month) in numbers:
        monthNum = int(month)
        month = int(month)
        print("true")
    if month == 1:
            month = "jan"
    if month == 2:
            month = "feb"
    if month == 3:
            month = "mar"
    if month == 4:
            month = "apr"
    if month == 5:
            month = "may"
    if month == 6:
            month = "jun"
    if month == 7:
            month = "jul"
    if month == 8:
            month = "aug"
    if month == 9:
            month = "sep"
    if month == 10:
            month = "oct"
    if month == 11:
            month = "oct"
    if month == 12:
            month = "dec"
    day = int(input("What day is your birthday on? - "))
    next = "false"
    for x in range(len(weekends[month])):
        if day+1 == weekends[month][x]:
            next = "true"
        if day-1 == weekends[month][x]:
            next = "true"
    if month == "jan":
        monthNum = 1
    if month == "feb":
        monthNum = 2
    if month == "mar":
        monthNum = 3
    if month == "apr":
        monthNum = 4
    if month == "may":
        monthNum = 5
    if month == "jun":
        monthNum = 6
    if month == "jul":
        monthNum = 7
    if month == "aug":
        monthNum = 8
    if month == "sep":
        monthNum = 9
    if month == "oct":
        monthNum = 10
    if month == "nov":
        monthNum = 11
    if month == "dec":
        monthNum = 12
    if day in weekends[month]:
        print(str(monthNum) + "/"+ str(day) +"/2018 falls on a weekend")
    elif next == "true":
        print(str(monthNum) + "/"+ str(day) +"/2018 falls next to a weekend")
    else:
        print(str(monthNum) + "/"+ str(day) +"/2018 does not fall on a weekend")

weekends = {"jan":[6,7,13,14,20,21,27,28],"feb":[3,4,10,11,17,18,24,25],"mar":[3,4,10,11,17,18,24,25,31],"apr":[1,7,8,14,15,21,22,28,29],"may":[5,6,12,13,19,20,26,27],"jun":[2,3,9,10,16,17,23,24,30],"jul":[1,7,8,14,15,21,22,28,29],"aug":[4,5,11,12,18,19,25,26],"sep":[1,2,8,9,15,16,22,23,29,30],"oct":[6,7,13,14,20,21,27,28],"nov":[3,4,10,11,17,18,24,25],"dec":[1,2,8,9,15,16,22,23,29,30]}
main(weekends)
