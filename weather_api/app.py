from flask import Flask, abort, jsonify
import re

import requests

from diagram.create_diagram import create_mermaid_diagram
from weather_api.model import WeatherResponse
from weather_api.utils import WeatherService


app = Flask(__name__)

def validate_zip_code(zip_code: str):
    """
    Validate ZIP code format.
    
    Args:
        zip_code (str): ZIP code of the location.

    Returns:
        None if valid, aborts with a 400 error if invalid.
    """
    if not re.match(r"^\d{5}(-\d{4})?$", zip_code):
        abort(400, description="Invalid ZIP code format. Valid formats: 12345 or 12345-6789.")


@app.route("/get_weather/<zip_code>", methods=["GET"])
def get_weather(zip_code: str):
    """
    Endpoint to fetch weather data and generate a weather diagram.
    
    Args:
        zip_code (str): ZIP code of the location.

    Returns:
        JSON response with weather data and a diagram path.
    """

    validate_zip_code(zip_code)
    parsed_zip_code = zip_code.split("-")[0]
    
    try:
        weather_service = WeatherService()

        weather_data = weather_service.get_weather_data(parsed_zip_code)
        validated_data = WeatherResponse(**weather_data)
        
        # Create a diagram
        file_path = create_mermaid_diagram(validated_data.model_dump())

        return jsonify({"current_temperature":weather_service.get_current_temperature(), "saved_file_path": file_path}), 200
    
    except KeyError as e:
        abort(500, description=f"Missing data in weather response: {str(e)}")
    except requests.HTTPError as e:
        abort(e.response.status_code, description="Error fetching data from the weather service.")
    except Exception as e:
        abort(500, description=str(e))

if __name__ == "__main__":
    app.run(debug=True)
