import unittest
from unittest.mock import patch, MagicMock
from weather_api.cli import fetch_data, main  # Import functions to be tested from cli.py

class TestCLI(unittest.TestCase):
    """
    Unit test cases for CLI functions, specifically fetch_data and main, to ensure proper handling of
    API requests and command-line argument parsing.
    """

    @patch('weather_api.cli.requests.get')
    def test_fetch_data_success(self, mock_get):
        """
        Test fetch_data function with a successful API response.
        
        This test:
        - Mocks the requests.get function to simulate an API call.
        - Creates a mock response with a JSON payload and a 200 OK status code.
        - Asserts that fetch_data correctly parses the JSON and returns the expected data.
        """
        
        # Configure the mock response object to simulate a successful API call
        mock_response = MagicMock()
        mock_response.json.return_value = {"weather": "sunny"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response  # Set the mock as the return value for requests.get

        # Call fetch_data with a test ZIP code and verify the returned data
        data = fetch_data("10001")
        
        # Assert that the function returned the expected data from the mock response
        self.assertEqual(data["weather"], "sunny")


# Run the test suite
if __name__ == '__main__':
    unittest.main()
