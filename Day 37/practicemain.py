import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "shu3939s9j3"
USER_NAME = "lamarcusgragas"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response_2 = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response_2)

today = datetime(year=2026, month=6, day=16)
update = today.strftime("%Y%m%d")
postpixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"
postpixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

# response_3 = requests.post(url=postpixel_endpoint, json=postpixel_params, headers=headers)
# print(response_3.text)

put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{update}"
put_params = {
    "quantity": "10",
}

# response_4 = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response_4.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{update}"
response_5 = requests.delete(url=delete_endpoint, headers=headers)
print(response_5)