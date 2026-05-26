from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(STARTING_POSITION)
        self.shape("turtle")
        self.color("black")
        self.setheading(90)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.setpos(STARTING_POSITION)
