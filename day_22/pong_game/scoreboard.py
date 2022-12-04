from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 22, "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score_right = 0
        self.score_left = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f'{self.score_left}:{self.score_right}', align=ALIGNMENT, font=FONT)        

    def increase_score(self,winner):
        if winner == 'right':
            self.score_right += 1
        else:
            self.score_left += 1

        self.clear()
        self.update_scoreboard()