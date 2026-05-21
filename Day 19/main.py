from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
screen = Screen()

screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race: ")
colors = ["red", "blue", "orange", "purple", "indigo", "green"]

# tim.penup()
# tim.goto(x=-230, y=-100)

names = []
y = -100
for color in colors:
    racer = Turtle(shape="turtle")
    names.append(racer)
    racer.color(color)
    racer.penup()
    racer.goto(-230, y)
    y += 30

race_on = True
while race_on:
    for name in names:
        if name.xcor() != 230:
            name.speed(4)
            name.forward(random.randint(4,10))
    for name in names:
        if name.xcor() >= 230:
            winner = name
            race_on = False

if winner.color() == user_choice:
    print(f"Congrats! You are victorious.")
else:
    print(f"Your turtle was too slow :(")

# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def move_left():
#     tim.left(10)
# def move_right():
#     tim.right(10)
# def clear_drawing():
#     tim.clear()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()

