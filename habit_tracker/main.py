import requests
from datetime import datetime

USERNAME = "your username"
TOKEN = "your token"
GRAPH_ID = "graph1"

#Create User
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Create Graph in User
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Number of Pages Read",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#Post Pixel Data
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()
today = datetime(year=2023, month=5, day=31)
formatted_day = today.strftime("%Y%m%d")
# print(formatted_day)

post_pixel_data = {
    "date": formatted_day,
    "quantity": "17",
}
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
# print(response.text)

#Update Pixel Data
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_day}"

update_pixel_data = {
    "quantity": "16"
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)

#Delete a Pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_day}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)

