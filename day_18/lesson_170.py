from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy"]
right_left = ["right", "left", "forward"]

def direction():
    direction = random.choice(right_left)
    if direction == "right":
        return tim.right(90)
    elif direction == "left":
        return tim.left(90)
    elif direction == "forward":
        return tim.forward(30)
    else:
        return tim.backward(30)

for i in range(100):
    some_color = random.choice(colors)    
    tim.color(some_color)
    direction()
    tim.speed(0)
    

screen.exitonclick()
