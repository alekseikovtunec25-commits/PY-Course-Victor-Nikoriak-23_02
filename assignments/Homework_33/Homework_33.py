# Task1

import requests

sites = [
    "https://www.wikipedia.org/robots.txt",
    "https://twitter.com/robots.txt",
    "https://www.google.com/robots.txt"
]

for url in sites:
    response = requests.get(url)

    filename = url.split("//")[1].split("/")[0] + "_robots.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"Saved: {filename}")

#Task3

import requests

API_KEY = "f8f9ca517daa49f4d9c5c3e710de74c9"

CITY = "Brovary"

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={CITY},UA"
    f"&appid={API_KEY}"
    f"&units=metric"
    f"&lang=ru"
)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    city = data["name"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\nТекущая погода")
    print("-" * 30)
    print(f"Город: {city}")
    print(f"Погода: {weather}")
    print(f"Температура: {temperature}°C")
    print(f"Ощущается как: {feels_like}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} гПа")
    print(f"Скорость ветра: {wind_speed} м/с")

else:
    print("Ошибка получения данных.")