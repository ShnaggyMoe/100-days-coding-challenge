import colorgram
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(10)
Screen().colormode(255)
timmy.penup()
y_position = 0
x_position = 0

colors = colorgram.extract('dot_painting.jpg' , 25)
colors_list = []
for color in colors:
    my_tuple = (color.rgb.r, color.rgb.b, color.rgb.g)
    colors_list.append(my_tuple)
print(colors_list)

timmy.hideturtle()
timmy.speed(0)
for dot_count in range(25):
    timmy.dot(10, colors_list[dot_count])
    timmy.forward(15)
    if dot_count % 5 == 4:
        y_position += 20
        timmy.goto(0, y_position)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()