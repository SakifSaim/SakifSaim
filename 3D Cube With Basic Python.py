import turtle
import time
l = int(input("Enter Cube Length: "))
a = int(input("Cube Angle: "))
t = turtle.Turtle()
s = turtle.Screen()

s.title("3D CUBE")
s.screensize(800, 500, bg="black")
t.pencolor("white")
t.pensize(3)


def square(l):
    for i in range(4):
        t.forward(l)
        t.left(90)


def cube(l, a):
    square(l)
    t.left(a)
    t.forward(l)
    time.sleep(1.5)
    t.right(a)
    time.sleep(1.5)
    square(l)
    t.left(90)
    t.forward(l)
    t.left(90+a)
    t.forward(l)
    t.right(a+180)
    t.forward(l)
    time.sleep(1.5)
    t.left(a)
    t.forward(l)
    t.right(a+90)
    t.forward(l)
    time.sleep(1.5)
    t.right(90-a)
    t.forward(l)


cube(l, a)
turtle.done()
