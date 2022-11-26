from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for i in range(20):
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.forward(10)


screen.exitonclick()

