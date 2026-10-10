import requests
from datetime import datetime

MY_LAT = 51.0989
MY_LNG = 16.9413



parameters = {
    'latitude': MY_LAT,
    'longitude': MY_LNG,
    'current': 'temperature_2m,wind_speed_10m',
    "hourly": "precipitation_probability",
}


response = requests.get(
    url="https://api.open-meteo.com/v1/forecast",
    params=parameters
)
response.raise_for_status()
response = response.json()

def get_weather_data():
    response = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params=parameters
    )
    response.raise_for_status()
    response = response.json()
    now_hour = datetime.now().hour
    temperature = response["current"]["temperature_2m"]
    wind = response["current"]["wind_speed_10m"]
    rain = response['hourly']['precipitation_probability'][now_hour]
    return temperature, wind, rain

temperature, wind, rain = get_weather_data()




