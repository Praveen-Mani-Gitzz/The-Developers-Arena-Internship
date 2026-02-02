from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import WeatherParser

api = WeatherAPI()
parser = WeatherParser()

raw = api.get_current_weather("London")

if raw:
    parsed = parser.parse_current_weather(raw)
    print(parsed)
