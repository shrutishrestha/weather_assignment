import webbrowser
from flask import abort
import requests
import argparse
import os

import requests

def fetch_data(zip_code: str) -> dict:
    """
    Fetch weather data for a specified ZIP code.
    
    Args:
        zip_code (str): ZIP code of the location.
    
    Returns:
        dict: Weather data if successful, or None if an error occurs.
    """
    url = f"http://localhost:5002/get_weather/{zip_code}"  # Assuming the server is running on localhost and port 5002

    try:
        response = requests.get(url)
        
        # Return JSON data if the request is successful
        response.raise_for_status()  # Will raise an HTTPError if the response was unsuccessful
        print("Weather data:", response.json())
        return response.json()

    except requests.ConnectionError:
        print("Error: Unable to connect to the server. Please ensure the Flask server is running on the correct port.")
    except requests.HTTPError as e:
        # Check for specific HTTP status codes and provide custom messages
        if response.status_code == 400:
            print("Error: Invalid request. Please check the ZIP code format.")
        elif response.status_code == 404:
            print("Error: Weather data not found. Please check if the ZIP code exists.")
        elif response.status_code == 500:
            print("Error: Internal server error. Please check the API key configuration or server logs.")
        else:
            # General HTTP error handling for other status codes
            try:
                error_data = response.json()
                print(f"Failed to fetch data: {error_data.get('detail', 'Error')} - {error_data.get('message', 'An unknown error occurred.')}")
            except requests.JSONDecodeError:
                print(f"HTTP error {response.status_code}: Unable to retrieve error details.")
    except requests.RequestException as e:
        print(f"An unexpected error occurred: {e}")


    return None


def main():
    parser = argparse.ArgumentParser(description="Fetch weather data for a specified ZIP code.")
    parser.add_argument("zip_code", type=str, help="ZIP code to fetch the weather for")
    args = parser.parse_args()
    
    weather_data = fetch_data(args.zip_code)

    if weather_data:
        output_file_path = weather_data.get("saved_file_path")

        open_in_browser = input("Do you want to open the diagram in the browser? (yes/no): ").strip().lower()
        if open_in_browser == "yes":
            webbrowser.open("file://" + os.path.abspath(output_file_path))


if __name__ == "__main__":
    main()
