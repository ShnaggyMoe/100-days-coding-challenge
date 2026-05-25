from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Indigo")
        self.shape("circle")

    def food_spawn(self):
        self.penup()
        self.goto(random.randint(-285, 285), random.randint(-285, 285))