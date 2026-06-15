import requests
from datetime import datetime
import smtplib

my_lat = 37.338207
my_long = -121.886330

my_email = 'rp6154485@gmail.com'
password = 'pqbujqddceplnmjk'

iss_response = requests.get(url="https://api.wheretheiss.at/v1/satellites/25544")
iss_response.raise_for_status()
iss_data = iss_response.json()

longitude = float(iss_data["longitude"])
latitude = float(iss_data["latitude"])
iss_position = (longitude, latitude)

parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0,
}
sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()
sunrise = int(sun_data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
now_hour = time_now.hour

if (latitude > my_lat - 5 and latitude < my_lat + 5
        and longitude > my_long - 5 and longitude < my_long + 5
        and (now_hour > sunset or now_hour < sunrise)):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addr=my_email, msg=f"Subject: ISS Overhead\n\nLook up!")