from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segm_num in range(len(segments) - 1,0,-1):
        new_x = segments[segm_num - 1].xcor()
        new_y = segments[segm_num - 1].ycor()
        segments[segm_num].goto(new_x,new_y) 

    segments[0].forward(20)