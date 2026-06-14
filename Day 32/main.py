##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




import smtplib
import datetime as dt
import pandas as pd
import random


my_email = 'rp6154485@gmail.com'
password = 'pqbujqddceplnmjk'

file = pd.read_csv("birthdays.csv")
today = dt.datetime.now()
current_day = today.day
current_month = today.month
birth_date = file[(file["month"] == 6) & (file["day"] == 14)]

with open("letter_templates/letter_1.txt") as file_1:
    letter_1 = file_1.read()
with open("letter_templates/letter_2.txt") as file_2:
    letter_2 = file_2.read()
with open("letter_templates/letter_3.txt") as file_3:
    letter_3 = file_3.read()

for index, row in birth_date.iterrows():
    random_letter = random.choice([letter_1, letter_2, letter_3])
    letter = random_letter.replace('[NAME]', row["name"])
    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(user=my_email, password=password)
        connections.sendmail(from_addr=my_email,
                             to_addrs=row["email"],
                             msg=f"Subject: Happy Birthday!\n\n{letter}")

# print(file)