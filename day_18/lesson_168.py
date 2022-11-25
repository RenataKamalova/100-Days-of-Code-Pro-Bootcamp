from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for i in range(20):
    tim.color("red")
    tim.forward(10)
    tim.color("white")
    tim.forward(10)


screen.exitonclick()

