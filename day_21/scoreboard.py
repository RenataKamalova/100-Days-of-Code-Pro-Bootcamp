from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.update_scoreboard()
        self.ht()

    def update_scoreboard(self):
        self.write(f'Score: {self.count}', False, align="center", font=("Courier", 22, "normal"))        
        
    def increase_score(self):
        self.count += 1
        self.clear()
        self.update_scoreboard()
        
        

    
        
       
    
        


        
