import os
import requests
from dotenv import load_dotenv
from typing import Tuple

# Load environment variables
load_dotenv()

class WeatherService:
    """Service for interacting with the OpenWeather API."""
    
    def __init__(self):
        self.weather_data = None
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise EnvironmentError("API key for OPENWEATHER_API_KEY is not set in environment variables.")
        self.session = requests.Session()

    def change_kelvin_to_farhenheit(self, kelvin: float) -> float:
        """
        Convert temperature in Kelvin to Fahrenheit.
        
        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature in Fahrenheit.
        """
        return (kelvin - 273.15) * 9/5 + 32
    
    def get_coordinates(self, zip_code: str) -> Tuple[float, float]:
        """
        Get latitude and longitude coordinates for a given ZIP code.
        
        Args:
            zip_code (str): ZIP code of the location.

        Returns:
            Tuple[float, float]: Latitude and longitude.
        
        Raises:
            HTTPError: If the API call fails.
            KeyError: If the response data is missing expected keys.
        """
        url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={self.api_key}"
        response = self.session.get(url)
        response.raise_for_status()
        
        data = response.json()
        return data["lat"], data["lon"]