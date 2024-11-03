import os
import unittest
from unittest.mock import patch


class TestWeatherService(unittest.TestCase):
    """
    Unit test cases for the WeatherService class, focusing on API interactions
    for coordinate retrieval and weather data fetching.
    """

    @patch.dict(os.environ, {"OPENWEATHER_API_KEY": "fake_api_key"})
    @patch('weather_api.utils.requests.Session.get')
    def test_get_coordinates_success(self, mock_get):
        pass

    @patch.dict(os.environ, {"OPENWEATHER_API_KEY": "fake_api_key"})
    @patch('weather_api.utils.requests.Session.get')
    def test_get_weather_data_success(self, mock_get):
        pass


# Run the test suite
if __name__ == '__main__':
    unittest.main()

    
