from datetime import datetime
from typing import Dict


class WeatherParser:
    """Parses raw weather API JSON into structured data"""

    @staticmethod
    def parse_current_weather(data: Dict) -> Dict:
        try:
            return {
                "city": data.get("name"),
                "country": data.get("sys", {}).get("country"),
                "temperature": data.get("main", {}).get("temp"),
                "feels_like": data.get("main", {}).get("feels_like"),
                "humidity": data.get("main", {}).get("humidity"),
                "pressure": data.get("main", {}).get("pressure"),
                "wind_speed": data.get("wind", {}).get("speed"),
                "description": data.get("weather", [{}])[0].get("description"),
                "condition": data.get("weather", [{}])[0].get("main"),
                "sunrise": WeatherParser._format_time(data.get("sys", {}).get("sunrise")),
                "sunset": WeatherParser._format_time(data.get("sys", {}).get("sunset")),
                "timestamp": WeatherParser._format_time(data.get("dt"))
            }
        except Exception:
            return {}

    @staticmethod
    def celsius_to_fahrenheit(temp_c: float) -> float:
        return round((temp_c * 9/5) + 32, 2)

    @staticmethod
    def _format_time(timestamp: int) -> str:
        if not timestamp:
            return "N/A"
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
