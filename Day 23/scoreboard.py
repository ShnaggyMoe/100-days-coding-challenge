from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-270, 280)
        self.current_level = 1
        self.write(f"Level: {self.current_level}")

    def game_over(self):
        self.setpos(0,0)
        self.write("Game Over", align="center", font=FONT)

    def next_level(self):
        self.clear()
        self.current_level += 1
        self.write(f"Level: {self.current_level}")