from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #bug was here. previous range was (1,6) which is invalid since dice_images[6] doesnt exist
print(dice_images[dice_num])