import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.bearer_token = os.environ.get("SHEETY_BEARER_TOKEN")
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

    def getting_data(self):
        headers = {"Authorization": self.bearer_token}
        response = requests.get(url=self.sheety_endpoint, headers=headers)
        data = response.json()
        locations = []
        for row in data["prices"]:
            city = row['city']
            iata = row["iataCode"]
            idealprice = row['lowestPrice']
            destination = TravelDestination(city, iata, idealprice)
            locations.append(destination)

        return locations





class TravelDestination:
    def __init__(self, city, IATA, lowestprice):
        self.city = city
        self.IATA = IATA
        self.lowestprice = lowestprice