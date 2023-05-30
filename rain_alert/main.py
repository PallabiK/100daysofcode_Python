import requests
from twilio.rest import Client
import os
#environment variables

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWM_API_KEY")
MY_LAT = 51.507351
MY_LNG = -0.127758
account_sid = "yours"
auth_token = "yours"

weather_params = {
    "lat": MY_LAT,
    "lon":MY_LNG,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body ="Rain today. Bring umbrella.",
        from_='fromphone#',
        to ='tophone#'
    )
    print(message.status)


