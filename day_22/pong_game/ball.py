from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("black", "white")
        self.penup()
        self.shapesize(3)
        self.x_move = 15
        self.y_move = 15         
        

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        