import turtle
from datetime import datetime
# turtle module
# s = turtle.getscreen()
# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.


def square(x, y, width, color):
    tur = turtle.Turtle()
    turtle.title("Square")
    # tur.penup()
    tur.shape("turtle")
    tur.speed(3)
    tur.pen(pencolor="purple", fillcolor="orange", pensize=10)
    tur.goto(x, y)
    # tur.fillcolor(color)
    # tur.color("red", "green")
    tur.pendown
    tur.begin_fill()
    for count in range(4):
        tur.speed(1)
        tur.forward(width)
        tur.left(90)
    tur.end_fill()
 # Simple Circle


def circle(x, y, radius, color):
    tur = turtle.Turtle()
    tur.shape("turtle")
    tur.speed(1)
    # tur.hideturtle()
    tur.pen(pencolor="purple", fillcolor="orange", pensize=10)
    tur.penup()
    tur.goto(x, y)
    # tur.fillcolor('red')
    tur.begin_fill()
    tur.pendown()
    tur.circle(radius)
    tur.end_fill()


def triangle(x, y):
    tur = turtle.Turtle()
    tur.shape("turtle")

    tur.pen(pencolor="purple", fillcolor="orange", pensize=10)
    tur.penup()
    tur.goto(x, y)
    tur.begin_fill()
    tur.pendown()
    for count in range(2):
        tur.speed(1)
        tur.forward(100)
        tur.right(90)
        if count == 1:
            tur.left(60)

    tur.end_fill()


def pentagone(x, y):
    tur = turtle.Turtle()
    tur.shape("turtle")

    tur.pen(pencolor="purple", fillcolor="orange", pensize=10)
    tur.penup()
    tur.goto(x, y)
    tur.begin_fill()
    tur.pendown()
    for count in range(5):
        tur.speed(1)
        tur.fd(100)
        tur.lt(72)

    tur.end_fill()


def hexagone(x, y):
    tur = turtle.Turtle()
    tur.shape("turtle")

    tur.pen(pencolor="purple", fillcolor="orange", pensize=10)
    tur.penup()

    tur.goto(x, y)
    tur.begin_fill()
    tur.pendown()
    for count in range(5):
        tur.fd(100)
        tur.lt(72)
        tur.speed(1)

    tur.end_fill()
# Python program to draw
# Rainbow Benzene
# using Turtle Programming


def rainbow(x, y):
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    tur = turtle.Turtle()
    tur.shape("turtle")
    tur.goto(x, y)
    # tur.penup()
    tur.screen.bgcolor('black')
    for c in range(150):
        tur.pencolor(colors[c % 6])
        tur.width(c//100 + 1)
        tur.forward(c)
        tur.left(59)


def main():
    shape = input(
        "Hi! Write the name of shape you want to draw\nSquare,\nCircle,\nTriangle,\
            \nPentagone,\nHexagone\nRainbow\nSnowman:\n>")
    # color = input("Choose a color?\n")
    # x = input("Choose x-cordinate:\n>")
    # y = input("Choose y-cordinate:\n>")
    if shape.lower() == "square":
        square(0, 0, 100, 'red')
    if shape.lower() == "circle":
        circle(0, 0, 100, 'red')
    if shape.lower() == "triangle":
        triangle(0, 0)
    if shape.lower() == "pentagone":
        pentagone(0, 0)
    if shape.lower() == "rainbow":
        rainbow(0, 0)
    else:
        print("Invalid shape name")

    # square(-150, -100, 200, 'blue')
    # square(-200, 150, 75, 'green')
    turtle.done()


main()
