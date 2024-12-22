import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Your OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'

# OpenWeatherMap base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

@app.route('/weather', methods=['GET'])
def get_weather():
    # Get the city name from query parameters
    city = request.args.get('city')
    
    # If no city is provided, return an error
    if not city:
        return jsonify({"error": "City is required!"}), 400

    # Construct the full URL for the API request
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    
    # Send a request to OpenWeatherMap API
    response = requests.get(url)
    
    # If the request was successful, return the data
    if response.status_code == 200:
        data = response.json()
        
        # Extract the relevant data from the API response
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }
        
        return jsonify(weather)
    
    # If the city is not found or any error occurs, return a message
    else:
        return jsonify({"error": "City not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
