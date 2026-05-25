from turtle import Turtle

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.color("White")
            new_segment.shape("square")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)- 1 , 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def turn_left(self):
        if self.segments[0].heading() == 0:
            pass
        else:
            self.segments[0].setheading(180)

    def turn_right(self):
        if self.segments[0].heading() == 180:
            pass
        else:
            self.segments[0].setheading(0)

    def turn_up(self):
        if self.segments[0].heading() == 270:
            pass
        else:
            self.segments[0].setheading(90)

    def turn_down(self):
        if self.segments[0].heading() == 90:
            pass
        else:
            self.segments[0].setheading(270)
