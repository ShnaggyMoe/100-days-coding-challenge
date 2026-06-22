#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search
import notification_manager

dummy = data_manager.DataManager()
locations = dummy.getting_data()
sms = notification_manager.NotificationManager()

# for location in locations:
#     print(location.city)
#     print(location.IATA)

search = flight_search.FlightSearch()
result = search.search_flights("CDG")
cheapest = min(result["best_flights"], key=lambda flight: flight["price"])
cheapest_price = cheapest["price"]

for location in locations:
    result = search.search_flights(location.IATA)
    cheapest = min(result["best_flights"], key=lambda flight: flight["price"])
    cheapest_price = cheapest["price"]
    destination_id = cheapest["flights"][0]["departure_airport"]["id"]
    arrival_id = cheapest["flights"][0]["arrival_airport"]["id"]
    outbound_date = result["search_parameters"]["outbound_date"]
    inbound_date = result["search_parameters"]["return_date"]
    if cheapest_price < location.lowestprice:
        sms.send_sms("Sent from your Twilio trial account - Join me in WhatsApp!")