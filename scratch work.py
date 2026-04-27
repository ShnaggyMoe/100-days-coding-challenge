#first challenge
# numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7]
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

#third challenge
user_choice = int(input('Guess the number!'))
target = 14
while user_choice != target:
    if user_choice > 14:
        print('lower')
        user_choice = int(input('try again'))
    elif user_choice < 14:
        print('higher')
        user_choice = int(input('try again'))
