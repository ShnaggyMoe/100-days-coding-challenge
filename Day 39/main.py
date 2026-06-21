#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search

dummy = data_manager.DataManager()
locations = dummy.getting_data()

# for location in locations:
#     print(location.city)
#     print(location.IATA)

search = flight_search.FlightSearch()
result = search.search_flights("CDG")
cheapest = min(result["best_flights"], key=lambda flight: flight["price"])