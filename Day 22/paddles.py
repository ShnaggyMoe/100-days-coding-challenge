from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, spawn_point):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(spawn_point)
        self.color("White")

    def move_up(self):
        self.sety(self.ycor() + 35)

    def move_down(self):
        self.sety(self.ycor() - 35)