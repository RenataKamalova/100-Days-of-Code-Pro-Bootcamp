from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

os.chdir(r'/home/ren/code/100-Days-of-Code-Pro-Bootcamp/day_24/lesson_219')

       



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        

        with open("data.txt") as data:
            self.high_score = int(data.read())            
            

        self.score = 0        
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()           

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode = "w") as data:
                data.write(f"{ self.high_score}") 
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1        
        self.update_scoreboard()
