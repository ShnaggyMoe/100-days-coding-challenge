import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
ALPHA_VANTAGE_API = os.environ.get("ALPHA_VANTAGE_API")
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "15min",
    "apikey" : ALPHA_VANTAGE_API,
}
response = requests.get(STOCK_ENDPOINT, params)
response.raise_for_status()
alpha_data = response.json()

daily_data = alpha_data["Time Series (Daily)"]
daily_list = list(daily_data.keys())
first_entry = daily_data[daily_list[0]]
yesterday_close = first_entry["4. close"]
day_before_yest_close = daily_data[daily_list[1]]["4. close"]
difference = abs(float(yesterday_close) - float(day_before_yest_close))
big_move = float(yesterday_close) * 0.05
if difference > big_move:
    print("Get News")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

    NEWS_AP = os.environ.get("NEWS_AP")
    params_2 = {
        "q": "Tesla",
        "sortBy": "popularity",
        "apikey": NEWS_AP,
    }
    response_2 = requests.get(NEWS_ENDPOINT, params_2)
    response_2.raise_for_status()
    news_data = response_2.json()
    recent_news = news_data["articles"][0:3]
    new_list = [f"{article["title"]} {article["description"]}" for article in recent_news]
    print(new_list)



    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    #HINT 1: Consider using a List Comprehension.
    client = Client(account_sid, auth_token)
    for news in new_list:
        message = client.messages.create(
            body="sms_appointment_reminders",
            from_="+17372583742",
            to="+14084138270",)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

