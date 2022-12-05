import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()        
        self.penup()
        self.height = 300
        self.all_squares = []
        
           
            
    
        for i in range(10):            
            self.shape('square')
            self.color(random.choice(COLORS))
            self.all_squares.append(self) 

    def move(self):       
        for square in self.all_squares:
            x_cord = 250
            y_cord = self.height - 50
            square.setheading(180)
            square.goto(x_cord,y_cord)
                          
            square.forward(10)
            
            
        