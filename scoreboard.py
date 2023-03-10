from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(50, 260)
        self.write(arg=f"{self.score_r}", align="center", font=("Arial", 20, "normal"))
        self.goto(-50, 260)
        self.write(arg=f"{self.score_l}", align="center", font=("Arial", 20, "normal"))

    def r_score(self):
        self.score_r += 1
        self.update_score()

    def l_score(self):
        self.score_l += 1
        self.update_score()