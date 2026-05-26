import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.onkey(player.move, "Up")
screen.listen()

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.25)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.my_list:
        if player.distance(car) < 13:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 300:
        player.reset()
        scoreboard.next_level()
        car_manager.new_level()



screen.exitonclick()