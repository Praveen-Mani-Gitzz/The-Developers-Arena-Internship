from colorama import Fore, Style, init

init(autoreset=True)


class WeatherDisplay:
    """Handles formatted weather output"""

    WEATHER_ICONS = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Fog": "🌫️",
        "Haze": "🌫️"
    }

    @staticmethod
    def _color_temperature(temp: float) -> str:
        if temp <= 10:
            return Fore.CYAN + f"{temp}°C" + Style.RESET_ALL
        elif temp <= 25:
            return Fore.GREEN + f"{temp}°C" + Style.RESET_ALL
        else:
            return Fore.RED + f"{temp}°C" + Style.RESET_ALL

    @staticmethod
    def display_current(weather: dict):
        print("\n🌤️  WEATHER DASHBOARD")
        print("=" * 40)

        icon = WeatherDisplay.WEATHER_ICONS.get(weather["condition"], "")
        temp_colored = WeatherDisplay._color_temperature(weather["temperature"])

        print(f"\n📍 Location: {weather['city']}, {weather['country']}")
        print(f"🕐 Last Updated: {weather['timestamp']}")

        print("\nCurrent Weather")
        print("-" * 30)
        print(f"Temperature:   {temp_colored}")
        print(f"Feels Like:    {weather['feels_like']}°C")
        print(f"Condition:     {weather['description']} {icon}")
        print(f"Humidity:      {weather['humidity']}%")
        print(f"Wind Speed:    {weather['wind_speed']} m/s")
        print(f"Pressure:      {weather['pressure']} hPa")
        print(f"Sunrise:       {weather['sunrise']}")
        print(f"Sunset:        {weather['sunset']}")
