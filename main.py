import datetime as dt 
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "59bcc052d550424ba96102a26b14662f"
CITY = input("Please enter a City Name:\t")

def Kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.16
    return celsius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_Kelvin = response["main"]["temp"] - 273.16
temp_celsius = Kelvin_to_celsius
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius = Kelvin_to_celsius(feels_like_kelvin)
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = dt.datetime.fromtimestamp(response["sys"]["sunrise"] + response["timezone"])
sunset_time = dt.datetime.fromtimestamp(response["sys"]["sunset"] + response["timezone"])

print(f"General Weather in {CITY}: {description}")
print(f"Temprature in {CITY}: {temp_Kelvin:.2f}C")
print(f"Temprature in {CITY}: feels like: {feels_like_celsius:.2f}C")
print(f"Wind speed {CITY}: {wind_speed}m/s")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Sun rises in {CITY}: at {sunrise_time} local time")
print(f"Sun sets in {CITY}: at {sunset_time} local time")
