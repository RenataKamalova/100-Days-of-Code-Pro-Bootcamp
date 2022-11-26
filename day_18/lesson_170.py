from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy"]
directions = [0,90,180,270]
sizes = [5,6,7, 8, 10,12,14]
tim.pensize(5)

for i in range(200):   
    tim.color(random.choice(colors)) 
    tim.pensize(random.choice(sizes))   
    tim.speed(0)
    tim.setheading(random.choice(directions))
    tim.forward(10)

    

screen.exitonclick()
