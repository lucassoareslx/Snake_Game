from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
       super().__init__()
       self.score = 0
       self.color("white")
       self.penup()
       self.goto(0,370)
       self.hideturtle()
       self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial",15,"normal"))

    def scorepoint(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.hideturtle()
        self.write("GAME OVER",align="center", font=("Arial",35,"normal") )
