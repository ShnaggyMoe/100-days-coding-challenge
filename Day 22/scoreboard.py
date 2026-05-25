from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 260)
        self.score_check()

    def score_check(self):
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align='center', font=("Arial", 24, "normal"))