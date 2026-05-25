from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

right_paddle_spawn = [350, 0]
left_paddle_spawn = [-350, 0]
right_paddle = Paddle(right_paddle_spawn)
left_paddle = Paddle(left_paddle_spawn)

pong_ball = Ball()
score = Score()


screen.listen()
screen.title('pong')
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    pong_ball.move()
    if pong_ball.ycor() >= 300 or pong_ball.ycor() <= -300:
        pong_ball.bounce_y()
    elif pong_ball.distance(right_paddle) < 40 or pong_ball.distance(left_paddle) < 35:
        pong_ball.bounce_x()
    elif pong_ball.xcor() > 400:
        score.left_score += 1
        pong_ball.reset_ball()
        score.score_check()
    elif pong_ball.xcor() < -400:
        score.right_score += 1
        pong_ball.reset_ball()
        score.score_check()





screen.exitonclick()