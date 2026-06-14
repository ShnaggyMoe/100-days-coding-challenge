import smtplib
import datetime as dt
import random


my_email = 'rp6154485@gmail.com'
password = 'pqbujqddceplnmjk'
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="phoenixaltair5285@gmail.com",
#                         msg="Subject: Hello\n\nThis is the body of my email.")

today = dt.datetime.now()
day_of_today = today.weekday()

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    if day_of_today == 5:
        random_quote = random.choice(quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection_2:
            connection_2.starttls()
            connection_2.login(user=my_email, password=password)
            connection_2.sendmail(from_addr=my_email,
                                  to_addrs="phoenixaltair5285@gmail.com",
                                  msg=f'Subject: Hello\n\n{random_quote}')