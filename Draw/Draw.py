import turtle
import random
import time

canvas = turtle.getcanvas()
pen = turtle.Pen()
x, y = canvas.winfo_pointerxy()
turtle.setup(width=1000,height=1000)
pen.speed(0)

def update():
    for z in range(0,100000):
        x, y = canvas.winfo_pointerxy()
        pen.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
        pen.goto(x-500,-(y-500))
    update()

update()
turtle.exitonclick()
