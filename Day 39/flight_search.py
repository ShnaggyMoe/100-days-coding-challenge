import os
import requests
from dotenv import load_dotenv
from datetime import datetime , timedelta

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.app_id = os.environ.get("APP_ID")
        self.api_key = os.environ.get("APIKEY")
        self.tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.six_months = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

    def search_flights(self, destination_iata):
        params = {
            "engine": "google_flights",
            "api_key": self.api_key,
            "departure_id": "LHR",
            "arrival_id": destination_iata,
            "outbound_date": self.tomorrow,
            "return_date": self.six_months,
            "type": 1,
            "stops": 1,
        }
        response = requests.get(url="https://app.100daysofpython.dev/v1/flights/search", params=params)
        data = response.json()
        print(data)