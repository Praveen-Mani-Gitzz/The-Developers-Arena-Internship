import requests
import json
import time
from pathlib import Path
from typing import Optional, Dict

from .config import API_KEY, BASE_URL, CACHE_DURATION


class WeatherAPI:
    """Handles communication with OpenWeatherMap API"""

    def __init__(self):
        self.cache_dir = Path("data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    # ----------------------------
    # Internal Helpers
    # ----------------------------

    def _get_cache_file(self, cache_key: str) -> Path:
        return self.cache_dir / f"{cache_key}.json"

    def _get_cached_data(self, cache_key: str) -> Optional[Dict]:
        cache_file = self._get_cache_file(cache_key)

        if cache_file.exists():
            if time.time() - cache_file.stat().st_mtime < CACHE_DURATION:
                try:
                    with open(cache_file, "r") as f:
                        print("Using cached data.")
                        return json.load(f)
                except:
                    pass

        return None

    def _save_to_cache(self, cache_key: str, data: Dict):
        cache_file = self._get_cache_file(cache_key)
        try:
            with open(cache_file, "w") as f:
                json.dump(data, f, indent=2)
        except:
            pass

    def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        try:
            params["appid"] = API_KEY
            params["units"] = "metric"

            response = requests.get(
                f"{BASE_URL}/{endpoint}",
                params=params,
                timeout=10
            )

            if response.status_code == 200:
                return response.json()

            elif response.status_code == 401:
                print("Invalid API key.")
            elif response.status_code == 404:
                print("City not found.")
            elif response.status_code == 429:
                print("API rate limit exceeded.")
            else:
                print(f"API error: {response.status_code}")

        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.ConnectionError:
            print("Network connection error.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        return None

    # ----------------------------
    # Public Methods
    # ----------------------------

    def get_current_weather(self, city: str) -> Optional[Dict]:
        cache_key = f"current_{city.lower()}"

        # Check cache first
        cached = self._get_cached_data(cache_key)
        if cached:
            return cached

        params = {"q": city}
        data = self._make_request("weather", params)

        if data:
            self._save_to_cache(cache_key, data)

        return data
