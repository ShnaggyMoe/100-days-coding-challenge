import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
my_lat = 37.338207
my_lon = -121.886330
api_key = os.environ.get("OWM_API_KEY")
weather_params = {
    "lat" : 22.396427,
    "lon" : 114.109497,
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

bring_umbrella = False
for data in weather_data["list"]:
    if data["weather"][0]["id"] <= 700:
        bring_umbrella = True

if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="sms_appointment_reminders",
        from_="+17372583742",
        to="+14084138270",)

    print(message.status)