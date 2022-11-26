from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy"]

def shape(sides_number):
    angle = 360 / sides_number
    for x in range(sides_number):        
        tim.forward(100)
        tim.right(angle)


for i in range(3,11):
    some_color = random.choice(colors)
    tim.color(some_color)
    shape(i)

screen.exitonclick()
