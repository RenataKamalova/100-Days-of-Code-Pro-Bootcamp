from turtle import Turtle,Screen
import random

colors = ["red","pink","green","blue","orange","purple"]
names = ["tim","gigi","fura","kila","budi","sewr"]

screen = Screen()
screen.setup(width=500,height=400)
y = 200
user_bet = screen.textinput(title="Make your choice", prompt = "Which turtle will win the race? Enter a color: ")

for i in range(0,6):
    y -= 50
    x = -200
    current_turtle = names[i]
    current_turtle = Turtle(shape="turtle")
    current_turtle.color(colors[i])
    current_turtle.penup()
    
    current_turtle.goto(x,y)


screen.exitonclick()