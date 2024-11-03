from flask import Flask, abort
import re


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
    
    """
    pass

if __name__ == "__main__":
    app.run(debug=True)
