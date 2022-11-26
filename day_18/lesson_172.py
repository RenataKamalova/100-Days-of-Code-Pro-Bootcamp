from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.pensize(2)
angle = 10
number_of_circles = 360 // angle


def color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return r,g,b

for i in range(number_of_circles):
    tim.pencolor(color())    
    tim.speed(0)
    tim.circle(100)    
    tim.right(angle)
    



screen.exitonclick()
