from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)


def color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return r,g,b

for i in range(60):
    tim.pencolor(color())    
    tim.speed(0)
    tim.circle(100)    
    tim.right(6)
    



screen.exitonclick()
