import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 to 100.")
game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
lives = 0
user_guess = 0
chosen_num = random.randint(1, 100)

if game_mode == 'easy':
    lives = 10
else:
    lives = 5

while lives > 0 and user_guess != chosen_num:
    user_guess = int(input("Make a guess: "))
    if user_guess != chosen_num:
        lives -= 1
        if user_guess < chosen_num:
            print("Too low.\n"
                  "Guess again.")
        elif user_guess > chosen_num:
            print("Too high.\n"
                  "Guess again.")
    elif user_guess == chosen_num:
        print(f"You got it! The answer was {chosen_num}")

if lives == 0 and user_guess != chosen_num:
    print(f"You lose. The answer was {chosen_num}")