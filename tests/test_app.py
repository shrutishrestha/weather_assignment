import unittest
from unittest.mock import patch
from weather_api.app import app


class TestApp(unittest.TestCase):
    """
    Test cases for the Flask app endpoints to verify functionality and error handling.
    """

    @patch('weather_api.utils.WeatherService.get_current_temperature')
    @patch('weather_api.utils.WeatherService.get_weather_data')
    @patch('diagram.create_diagram.create_mermaid_diagram')
    def test_get_weather(self, mock_create_diagram, mock_get_weather_data, mock_current_temp):
        """
        Test case for a valid ZIP code, mocking the weather data retrieval, diagram creation, and temperature.

        This test:
        - Mocks the WeatherService.get_weather_data method to return predefined weather data.
        - Mocks the create_mermaid_diagram function to return a dummy file path for the generated diagram.
        - Mocks get_current_temperature to return a predefined temperature.
        - Sends a GET request to the /get_weather endpoint with a valid ZIP code.
        - Asserts that the response status code is 200 (OK).
        - Asserts that the response JSON contains both 'saved_file_path' and 'current_temperature'.
        """

        # Define mock return values
        mock_weather_data = {
            "coord": {"lon": -74.0060, "lat": 40.7128},
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "base": "stations",
            "main": {"temp": 289.5, "feels_like": 287.8, "temp_min": 288.7, "temp_max": 290.4, "pressure": 1013, "humidity": 50},
            "visibility": 10000,
            "wind": {"speed": 4.1, "deg": 80},
            "clouds": {"all": 0},
            "dt": 1605182400,
            "sys": {"type": 1, "id": 1414, "country": "US", "sunrise": 1605169985, "sunset": 1605206585},
            "timezone": -18000,
            "id": 5128581,
            "name": "New York",
            "cod": 200
        }
        mock_get_weather_data.return_value = mock_weather_data
        mock_create_diagram.return_value = "diagram.html"
        mock_current_temp.return_value = 68.0  # Mock temperature in Fahrenheit
        
        # Create a test client to simulate HTTP requests to the Flask app
        with app.test_client() as client:
            # Send a GET request to the endpoint with a valid ZIP code
            response = client.get("/get_weather/10001")

            # Check if the response status code is 200 (successful request)
            self.assertEqual(response.status_code, 200)
            
            # Check if 'saved_file_path' and 'current_temperature' are present in the JSON response
            self.assertIn("saved_file_path", response.json)
            self.assertIn("current_temperature", response.json)

            # Assert the temperature value
            self.assertEqual(response.json["current_temperature"], 68.0)  # Check the mocked temperature value

    def test_invalid_zip_code(self):
        """
        Test case for an invalid ZIP code to validate error handling.

        This test:
        - Sends a GET request to the /get_weather endpoint with an invalid ZIP code format.
        - Asserts that the response status code is 400 (Bad Request), indicating a validation error.
        """

        # Create a test client to simulate HTTP requests to the Flask app
        with app.test_client() as client:
            # Send a GET request to the endpoint with an invalid ZIP code
            response = client.get("/get_weather/123")
            
            # Check if the response status code is 400 (indicating a bad request due to invalid ZIP code)
            self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
