import requests
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()


#time
today = dt.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

#nutrition
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
data = {
    "query": "swam for 2 hours and hiked for 4 hours"
}

response = requests.post(url=URL, json=data, headers=headers)
result = response.json()
exercise = result["exercises"][0]

#sheety
AUTHORIZATION = os.environ.get("AUTHORIZATION")
sheety_URL = "https://api.sheety.co/3fbf2648dfcc52c9119fb269fc0d612a/workoutTracking/workouts"
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": AUTHORIZATION
}


for exercise in result["exercises"]:
    data_2 = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response_2 = requests.post(url=sheety_URL, json=data_2, headers=sheety_headers)
print(result["exercises"])