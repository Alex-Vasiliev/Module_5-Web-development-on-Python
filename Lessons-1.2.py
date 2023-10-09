import requests
from datetime import datetime


def get_weather(api_key, city):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        print("Помилка: Неможливо отримати погодні дані")
        return

    location = data["location"]["name"]
    condition = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    date_time = data["current"]["last_updated"]
    datetime_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
    date = datetime_obj.date()
    time = datetime_obj.time()

    print(f"Погода у місті {location}: {condition}")
    print(f"Поточна дата: {date}")
    print(f"Поточний час: {time}")
    print(f"Температура: {temperature}°C")


api_key = "f5d181e6e72944ae857231625230610"
city = "Berlin"
get_weather(api_key, city)
