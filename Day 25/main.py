# my_list = []
#
# with open("weather_data.csv") as file:
#     weather_line = file.readlines()
#     for lines in weather_line:
#         my_list.append(lines)
#
# print(my_list)
#
import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     next(data)
#     for row in data:
#         temp_num = row[1]
#         temp_num_int = int(temp_num)
#         temperature.append(temp_num_int)
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(data["temp"].max())
# print(data.temp)
# print(data["temp"])
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])
# monday = data[data["day"] == "Monday"]
# monday_temp = monday["temp"] * 1.8 + 32
# print(monday_temp)

# data = pandas.read_csv("squirrel_count.csv")
# print(data["Primary Fur Color"].value_counts())

# squirrel_dict = {"color":[ "Gray", "Cinnamon", "Black"], "color_count" : [2473, 392, 103],
#                  }
# squirrel_dataframe = pandas.DataFrame(squirrel_dict)
# # print(squirrel_dataframe)
# squirrel_dataframe.to_csv("squirrel_color_count")

from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("states.csv")
states_list = data["state"].to_list()
correct_guess = []

game_on = True
while game_on:
    user_guess = screen.textinput("Question", "guess a state: ")
    if len(correct_guess) == len(states_list):
        game_on = False
        break
    elif user_guess in states_list and user_guess not in correct_guess:
        correct_guess.append(user_guess)
        state_row = data[data["state"] == user_guess]
        x_location = state_row["x"].values[0]
        y_location = state_row["y"].values[0]
        state_turtle = Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(x_location, y_location)
        state_turtle.write(user_guess)

screen.exitonclick()