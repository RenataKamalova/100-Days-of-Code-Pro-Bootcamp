from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for i in range(3,11):
    angle = 360 / i
    for x in range(i):        
        tim.forward(100)
        tim.right(angle)

screen.exitonclick()
