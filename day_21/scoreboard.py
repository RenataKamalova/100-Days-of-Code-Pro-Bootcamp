from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.ht()
        self.penup()

    def score(self):
        self.count += 1
        self.write(f'Score: {self.count}', False, align="center", font=("Times new roman", 20, "normal"))
       
    
        


        
