from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.startingscore = 0
        self.goto(0, 270)
        self.color("White")
        self.hideturtle()
        self.write(f"Score: {self.startingscore} High Score : {self.highscore}")

    def update_score(self):
        self.startingscore += 1
        self.clear()
        self.write(f"Score: {self.startingscore} High Score : {self.highscore}")

    def game_over(self):
        self.write(f"Game over. Your final score: {self.startingscore}")

    def reset(self):
        with open("data.txt", mode='w') as file_2:
            if self.startingscore > self.highscore:
                file_2.write(str(self.startingscore))
                self.highscore = self.startingscore
        self.write(f"Game over. Your final score: {self.startingscore}")
        self.startingscore = 0