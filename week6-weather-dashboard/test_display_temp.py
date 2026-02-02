from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import WeatherParser
from weather_app.weather_display import WeatherDisplay

api = WeatherAPI()
parser = WeatherParser()
display = WeatherDisplay()

raw = api.get_current_weather("London")

if raw:
    parsed = parser.parse_current_weather(raw)
    display.display_current(parsed)
