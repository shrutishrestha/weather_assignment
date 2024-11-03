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
