import json
import os

import requests


def get_current_weather_by_city(api_key: str, city: str) -> dict:
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&unit=metric")
    return json.loads(response.text)


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def print_weather(weather_data: dict):
    print(f"Weather data: {current_city}")
    print(f"Temp, °C: {round(kelvin_to_celsius(weather_data['main']['temp']))}")
    print(f"Temp feels like, °C: {round(kelvin_to_celsius(weather_data['main']['feels_like']))}")
    print(f"Humidity, %: {round(weather_data['main']['humidity'])}")
    print(f"Wind speed, m/s: {round(weather_data['wind']['speed'], 1)}")
    print(f"Pressure, hPa: {weather_data['main']['pressure']}")
    print(f"Visibility, km: {round(weather_data['visibility'] / 1000, 1)}")


if __name__ == "__main__":
    key = os.getenv("WEATHER_API_KEY")
    current_city = "Kyiv"
    print_weather(get_current_weather_by_city(key, current_city))
