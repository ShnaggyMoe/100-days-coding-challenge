import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.STARTING_MOVE_DISTANCE = 15
        self.my_list = []

    def move(self):
        for car in self.my_list:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def create_car(self):
        coin = random.randint(0, 1)
        if coin == 0:
            y = random.randint(-300, 300)
            car = Turtle()
            car.setheading(180)
            car.penup()
            car.sety(y)
            car.setx(320)
            car.color(random.choice(COLORS))
            car.shape("square")
            self.my_list.append(car)

    def new_level(self):
        self.STARTING_MOVE_DISTANCE += 10