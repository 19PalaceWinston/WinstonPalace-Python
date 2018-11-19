import turtle
import random

def part1(ans):
    if ans == "line":
        pen.backward(50)
        pen.forward(100)
    pen.pencolor("#0000FF")
    if ans == "square":
        for x in range(0,4):
            pen.forward(200)
            pen.left(90)
    if ans == "circle":
        pen.pencolor(1,0,1)
        pen.circle(150)
    if ans == "triangle":
        pen.pencolor("Green")
        for y in range(0,3):
            pen.left(120)
            pen.forward(400)

def part2():
    n = int(input("How many sides do you want?"))
    if n > 20:
        print("20 is the maximum")
        n = 20
    if n < 5:
        print("5 is the minimum")
        n = 5
    color = input("What color?")
    pen = turtle.Pen()
    if color.lower() == "blue":
        pen.pencolor("Blue")
    elif color.lower() == "red":
        pen.pencolor("Red")
    elif color.lower() == "green":
        pen.pencolor("Green")
    else:
        color = ""
    pen.up()
    pen.forward(50)
    pen.down()
    for x in range(0,n):
        if color == "":
            pen.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
        pen.left(360/n)
        pen.forward(50)

def part3():
    pen.up()
    pen.goto(150,150)
    pen.down()
    part1("line")
    pen.up()
    pen.goto(-300,150)
    pen.down()
    part1("square")
    pen.up()
    pen.goto(-50,-300)
    pen.down()
    part1("triangle")
    pen.up()
    pen.goto(200,-300)
    pen.down()
    part1("circle")

def part4():
    pen.speed(0)
    for z in range(10,250,50):
        for x in range(0,50):
            turtle.bgcolor(x/50,z/250,z/250)
            pen.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
            pen.circle(z)
            pen.right(10)

def part5():
    pen.speed(0)
    pen.up()
    pen.goto(0,0)
    pen.down()
    pen.pencolor("Red")
    for z in range(0,500,10):
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-100)
    pen.up()
    pen.goto(0,0)
    pen.right(90)
    pen.down()
    pen.pencolor("Orange")
    for z in range(0,500,10):
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-100)
    pen.up()
    pen.right(90)
    pen.goto(0,0)
    pen.down()
    pen.pencolor("Yellow")
    for z in range(0,500,10):
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-90)
        pen.forward(z)
        pen.right(-100)

ans = input("Which part do you want?\nThe Second Half of part 4 is part 5")
if ans == "1":
    pen = turtle.Pen()
    part1(input("What shape?"))
if ans == "2":
    part2()
if ans == "3":
    pen = turtle.Pen()
    part3()
if ans == "4":
    pen = turtle.Pen()
    part4()
if ans == "5":
    pen = turtle.Pen()
    part5()
turtle.exitonclick()
