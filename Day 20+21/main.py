from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

snake_food = Food()
snake_food.food_spawn()

user_score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(snake_food) <= 15:
        snake_food.food_spawn()
        user_score.update_score()
    if snake.segments[0].xcor() >= 300 or snake.segments[0].xcor() <= -300:
        user_score.clear()
        user_score.reset()
        break
    elif snake.segments[0].ycor() >= 300 or snake.segments[0].ycor() <= -300:
        user_score.clear()
        user_score.reset()
        break

screen.exitonclick()