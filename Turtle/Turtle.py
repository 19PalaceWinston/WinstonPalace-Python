import turtle

pen = turtle.Pen()
turtle.bgcolor("Blue")
for x in range(0,4):
    pen.forward(50)
    pen.left(90)
pen.pencolor(1,1,1)
pen.up()
pen.goto(-10,-10)
pen.down()
for x in range(0,4):
    pen.backward(50)
    pen.left(90)
pen.pencolor(1,0,0)
pen.up()
pen.goto(10,-10)
pen.down()
for x in range(0,2):
    pen.forward(50)
    pen.left(90)
    pen.backward(30)
    pen.left(90)
pen.pencolor(0,1,0)
pen.up()
pen.goto(-10,10)
pen.down()
for x in range(0,2):
    pen.backward(50)
    pen.left(90)
    pen.forward(30)
    pen.left(90)

turtle.exitonclick()
