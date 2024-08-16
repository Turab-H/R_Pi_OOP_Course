from turtle import Turtle
from random import randint

Humayun = Turtle()

Humayun.color("red")
Humayun.shape("turtle")

Humayun.penup()

Humayun.goto(0, 0)

Humayun.pendown()



Baba = Turtle()

Baba.color("blue")
Baba.shape("turtle")

Baba.penup()

Baba.goto(0, 30)

Baba.pendown()



Mama = Turtle()

Mama.color("yellow")
Mama.shape("turtle")

Mama.penup()

Mama.goto(0, -30)

Mama.pendown()


Turab = Turtle()

Turab.color("green")
Turab.shape("turtle")

Turab.penup()

Turab.goto(0, -60)

Turab.pendown()

for movement in range(100):
    Humayun.forward(randint(1, 5))
    Baba.forward(randint(1, 5))
    Mama.forward(randint(1, 5))
    Turab.forward(randint(1, 5))

input("Enter to close.")
