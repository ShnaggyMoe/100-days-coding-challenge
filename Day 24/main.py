with open("my_file.txt.py") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt.py", mode="w") as file:
    file.write("jalapenos")

with open("my_file.txt.py", mode='a') as file:
    file.write("\nhambugera")

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as file_1:
    letter_file = file_1.read()
with open("Input/Names/invited_names.txt") as file_2:
    names_file = file_2.read()

new_name_file = names_file.splitlines()

for name in new_name_file:
    new_letter = letter_file.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", mode='w') as file:
        file.write(new_letter)