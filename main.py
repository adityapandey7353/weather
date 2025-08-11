from flask import Flask, render_template, request, url_for
import requests
from pprint import pprint

app = Flask(__name__, template_folder='templates')
API_key = 'de68d6d818cab0f95b1a0596bca6d6d8' 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_key}&q={city}"
    weather_data = None
    error = None
    try:
        response = requests.get(base_url)
        response.raise_for_status() 
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        error = f"Error fetching weather data: {e}"
    except ValueError:
        error = "Invalid JSON response from the API."

    return render_template('weather.html', city=city, weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)