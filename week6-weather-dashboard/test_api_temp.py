from weather_app.weather_api import WeatherAPI

api = WeatherAPI()

data = api.get_current_weather("London")

if data:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"])
    print("Condition:", data["weather"][0]["description"])
