import os
import unittest
from unittest.mock import patch, MagicMock
from weather_api.utils import WeatherService


class TestWeatherService(unittest.TestCase):
    """
    Unit test cases for the WeatherService class, focusing on API interactions
    for coordinate retrieval and weather data fetching.
    """

    @patch.dict(os.environ, {"OPENWEATHER_API_KEY": "fake_api_key"})
    @patch('weather_api.utils.requests.Session.get')
    def test_get_coordinates_success(self, mock_get):
        """
        Test get_coordinates method in WeatherService with a successful API response.
        
        This test:
        - Mocks the environment to set a fake API key.
        - Mocks the requests.Session.get method to simulate an API call.
        - Configures the mock to return a JSON response with latitude and longitude.
        - Verifies that the get_coordinates method correctly parses and returns coordinates.
        """
        
        # Set up the mock response with latitude and longitude data
        mock_response = MagicMock()
        mock_response.json.return_value = {"lat": 40.7128, "lon": -74.0060}
        mock_response.status_code = 200
        mock_get.return_value = mock_response  # Assign the mock response to Session.get
        
        # Initialize the WeatherService with the mocked API key
        service = WeatherService()
        
        # Call get_coordinates and retrieve latitude and longitude
        lat, lon = service.get_coordinates("10001")
        
        # Assert that latitude and longitude match the mock response data
        self.assertEqual(lat, 40.7128)
        self.assertEqual(lon, -74.0060)


    @patch.dict(os.environ, {"OPENWEATHER_API_KEY": "fake_api_key"})
    @patch('weather_api.utils.requests.Session.get')
    def test_get_weather_data_success(self, mock_get):
        pass


# Run the test suite
if __name__ == '__main__':
    unittest.main()

    
