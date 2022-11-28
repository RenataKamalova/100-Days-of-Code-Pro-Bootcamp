from turtle import Turtle,Screen
import random

colors = ["red","pink","green","blue","orange","purple"]
names = ["tim","gigi","fura","kila","budi","sewr"]
all_turtles = []
is_race_on = False

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
    all_turtles.append(current_turtle)

if user_bet:
    is_race_on =True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()