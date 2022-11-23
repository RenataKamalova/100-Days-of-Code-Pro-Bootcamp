from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.color("red")

for i in range(4):
    timmy.forward(100)
    timmy.left(90)
    
screen.exitonclick()


