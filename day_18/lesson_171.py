from turtle import Turtle, Screen 
import random

tim = Turtle()
screen = Screen()
directions = [0,90,180,270]
sizes = [1,2,3,4,5,6,7,8,9,10]
screen.colormode(255)

def color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return r,g,b

for i in range(200):   
    tim.pencolor(color()) 
    tim.pensize(random.choice(sizes))   
    tim.speed(0)
    tim.setheading(random.choice(directions))
    tim.forward(10)

    

screen.exitonclick()