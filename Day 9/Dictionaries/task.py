# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."
# }

colors = {                      #dictionary
    "apple": "red",
    "pear": "green",
    "banana": "yellow",
}


colors["grapes"] = "purple"    #adding to dictionary

colors["apple"] = "green" #updating exiting key in dictionary

for key in colors:
    print(key)
    print(colors[key])