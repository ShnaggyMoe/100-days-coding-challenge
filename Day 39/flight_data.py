class FlightData:
    #This class is responsible for structuring the flight data.
    pass

class CheapFlight:
    def __init__(self, price, destination_IATA, home_IATA, departure_date, return_date):
        self.price = price
        self.destination_IATA = destination_IATA
        self.home_IATA = home_IATA
        self.departure_date = departure_date
        self.return_date = return_date