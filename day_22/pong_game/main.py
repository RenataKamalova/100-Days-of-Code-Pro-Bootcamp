from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

is_game_on = True

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor() > 270 or ball.ycor() <= -270:        
        ball.bounce_y()


    #detect collision with paddle
    if (ball.distance(r_paddle) < 75 and ball.xcor() < 390) or (ball.distance(l_paddle) < 60 and ball.xcor() > -390):
        ball.bounce_x()

    #detect R paddle misses   
    if ball.xcor() > 450:
        scoreboard.increase_score("left")       
        ball.reset_position()

    #detect L paddle misses
    if ball.xcor() < -450:
        scoreboard.increase_score("right")        
        ball.reset_position()




screen.exitonclick()