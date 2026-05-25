from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.startingscore = 0
        self.goto(0, 270)
        self.color("White")
        self.hideturtle()
        self.write(f"Score: {self.startingscore}")

    def update_score(self):
        self.startingscore += 1
        self.clear()
        self.write(f"Score: {self.startingscore}")

    def game_over(self):
        self.write(f"Game over. Your final score: {self.startingscore}")