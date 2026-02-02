from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import WeatherParser
from weather_app.weather_display import WeatherDisplay


def show_help():
    print("\nAvailable commands:")
    print("  search  - Search weather by city")
    print("  refresh - Refresh current city")
    print("  help    - Show help menu")
    print("  quit    - Exit application")


def main():
    api = WeatherAPI()
    parser = WeatherParser()
    display = WeatherDisplay()

    current_city = None

    print("\n🌤️  Welcome to Weather Dashboard")

    while True:
        if not current_city:
            city = input("\nEnter city name (or type 'quit'): ").strip()

            if city.lower() == "quit":
                print("Exiting Weather Dashboard.")
                break

            if not city:
                continue

            current_city = city

        raw_data = api.get_current_weather(current_city)

        if raw_data:
            parsed_data = parser.parse_current_weather(raw_data)
            display.display_current(parsed_data)
        else:
            current_city = None
            continue

        command = input(
            "\nType 'refresh', 'search', 'help', or 'quit': "
        ).strip().lower()

        if command == "quit":
            print("Exiting Weather Dashboard.")
            break

        elif command == "search":
            current_city = None

        elif command == "refresh":
            print("Refreshing weather data...")
            # Force refresh by clearing cache manually
            api.cache_dir.joinpath(f"current_{current_city.lower()}.json").unlink(missing_ok=True)

        elif command == "help":
            show_help()

        else:
            print("Invalid command. Type 'help' for options.")


if __name__ == "__main__":
    main()
