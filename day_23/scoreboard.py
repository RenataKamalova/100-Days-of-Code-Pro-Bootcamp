from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.update_level()
        
        

        

    def increase_level(self):
        self.score += 1
        self.clear()
        self.update_level()      

    def update_level(self):
        self.write(f"Level: {self.score}", False, font = FONT)

    def game_over(self):
        self.goto(-50,0)
        self.write("GAME OVER", font = FONT)
        

          

