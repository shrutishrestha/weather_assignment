# weather_assignment

## Goal
To get weather according to zip code provided.

## Core Requirements
1. To expose an API server with one endpoint that will calculate and respond with the weather forecast for today in Fahrenheit 
2. Create a Graph Diagram programmatically which creates an HTML (output.html) with a [Mermaid JS].
3. Use GitHub Actions package to create a wheel file and test the weather_api code then publish the code coverage results as an HTML report
4. Interactive command line interface to 
   - run the API server
   - respond with the weather forecast for today
   - create the output.html diagram and optionally open it


## Additional Requirements
1. Maintainability (code organization and structure) User Experience
2. Data Validation
3. Security (API key management)
4. Documentation (End user and internal) Error handling
5. Testability
6. Python modern stack


## Architecture Diagram
<img src="architecure_weather_api.png"></img>

Explanation of Each Component in the Diagram
1. User or Client App: The client sends a GET request with a ZIP code to the Flask app's /get_weather/<Zio_code> endpoint.
2. Flask App:
   1. Receives and validates the ZIP code.
   2. Calls the Weather Data Service (WeatherService) to retrieve weather information using an external weather API.
   3. If successful, the weather data is structured and passed to the Diagram Generator to create a visual repqresentation.
   4. Returns the JSON response containing path to generated diagram file and temperature in fahrenheit.
3. Weather data service 
   1. Calls the external API using the ZIP code to get the weather data
   2. Handles any errors from API and returns structred data back to the Flask app.
4. Diagran Generator:
   1. Receives structured weather data, processes it into a diagram (using MermaiJS) and saves the output to Diagram Storage.
5. Diagram Storage:
   1. Stores generated diagrams temporarily or permanently.
   2. Provides the file path to the Flask app to include in the response back to the user.
