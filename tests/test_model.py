import unittest
from weather_api.model import Coord, Weather, WeatherResponse   # Import the models to be tested

class TestWeatherModels(unittest.TestCase):
    """
    Unit test cases for weather data models, ensuring proper attribute initialization and data integrity.
    """

    def test_coord_model(self):
        """
        Test the Coord model initialization with sample latitude and longitude.
        
        This test:
        - Initializes the Coord model with latitude and longitude values.
        - Asserts that the lat and lon attributes match the expected values.
        """
        # Create an instance of Coord with sample latitude and longitude with values for New York City
        coord = Coord(lat=40.7128, lon=-74.0060)
        
        # Assert that latitude and longitude are set correctly
        self.assertEqual(coord.lat, 40.7128)
        self.assertEqual(coord.lon, -74.0060)

    def test_weather_model(self):
        """
        Test the Weather model with sample weather condition data.
        
        This test:
        - Initializes the Weather model with sample weather condition details.
        - Asserts that the main attribute is set to the expected weather condition.
        """
        # Create an instance of Weather with sample weather data
        weather = Weather(id=800, main="Clear", description="clear sky", icon="01d")
        
        # Assert that the main weather condition is set correctly
        self.assertEqual(weather.main, "Clear")

    def test_weather_response_model(self):
        """
        Test the WeatherResponse model with a full set of sample response data.
        
        This test:
        - Initializes the WeatherResponse model using a dictionary with nested weather data.
        - Asserts that specific attributes are correctly populated based on the input data.
        """
        # Sample response data with nested structures for the WeatherResponse model
        response_data = {
            "coord": {"lat": 40.7128, "lon": -74.0060},
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
        
        # Initialize the WeatherResponse model using unpacked dictionary data
        response = WeatherResponse(**response_data)
        
        # Assert that the name attribute is set correctly based on the input data
        self.assertEqual(response.name, "New York")

# Run tests
if __name__ == '__main__':
    unittest.main()
