import os
import requests
from flask import redirect, url_for
from pprint import PrettyPrinter
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent='app.py')

################################################################################
## SETUP
################################################################################

app = Flask(__name__)

# Get the API key from the '.env' file
load_dotenv()

pp = PrettyPrinter(indent=4)

API_KEY = os.getenv('API_KEY')
API_URL = 'http://api.openweathermap.org/data/2.5/weather'



################################################################################
## ROUTES
################################################################################

@app.route('/')
def home():
    """Displays the homepage with forms for current or historical data."""
    context = {
        'min_date': (datetime.now() - timedelta(days=5)),
        'max_date': datetime.now()
    }
    return render_template('home.html', **context)

def get_letter_for_units(units):
    """Returns a shorthand letter for the given units."""
    return 'F' if units == 'imperial' else 'K' if units == 'kelvin' else 'C'
def get_distance_for_units(units):
    """Returns a shorthand distance unit for the given units."""
    return 'MPH' if units == 'imperial' else 'KM/H'

def call_weather(parameters):
    return requests.get(API_URL, parameters).json()

@app.route('/results')
def results():
    """Displays results for current weather conditions."""
    city = request.args.get('city')
    units = request.args.get('units')

    if not city:
        return redirect(url_for('error', message='Invalid city input'))
    
    params = {

        'q': city,
        'appid': API_KEY,
        'units': units
    }

    result_json = call_weather(params)

    #Time variables
    raw_datenow = datetime.now()
    formatted_datenow = raw_datenow.strftime('%B %d, %Y at %I:%M %p')

    # Convert timestamps to datetime objects
    utc_sunrise = datetime.utcfromtimestamp(result_json['sys']['sunrise'])
    utc_sunset = datetime.utcfromtimestamp(result_json['sys']['sunset'])

    # Apply timezone offset
    timezone_offset = result_json['timezone']
    local_sunrise = utc_sunrise + timedelta(seconds=timezone_offset)
    local_sunset = utc_sunset + timedelta(seconds=timezone_offset)

    formatted_local_sunrise = local_sunrise.strftime('%I:%M %p')
    formatted_local_sunset = local_sunset.strftime('%I:%M %p')

    icon_code = result_json['weather'][0]['icon']
    icon_url = f'https://openweathermap.org/img/wn/{icon_code}@2x.png'


    context = {
        'date': formatted_datenow,
        'city': result_json['name'],
        'description': result_json['weather'][0]['description'].upper(),
        'distance_letter': get_distance_for_units(units),
        'icon': icon_url,
        'temp': result_json['main']['temp'],
        'humidity': result_json['main']['humidity'],
        'wind_speed': result_json['wind']['speed'],
        'sunrise': formatted_local_sunrise,
        'sunset': formatted_local_sunset,
        'units_letter': get_letter_for_units(units)
    }

    return render_template('results.html', **context)


@app.route('/comparison_results')
def comparison_results():
    """Displays the relative weather for 2 different cities."""
    # Use 'request.args' to retrieve the cities & units from the query
    # parameters.
    city1 = request.args.get('city1')
    city2 = request.args.get('city2')
    units = request.args.get('units_c')

    # Make 2 API calls, one for each city. HINT: You may want to write a 
    # helper function for this!
    if not city1 or not city2:
        return redirect(url_for('error', message='Invalid city input'))

    city1_params = {
    # : Enter query parameters here for the 'appid' (your api key),
    # the city, and the units (metric or imperial).
    # See the documentation here: https://openweathermap.org/current
    'q': city1,
    'appid': API_KEY,
    'units': units
}
    city2_params = {
    # : Enter query parameters here for the 'appid' (your api key),
    # the city, and the units (metric or imperial).
    # See the documentation here: https://openweathermap.org/current
    'q': city2,
    'appid': API_KEY,
    'units': units
}

    city1_result = call_weather(city1_params)
    city2_result = call_weather(city2_params)

    # Pass the information for both cities in the context. Make sure to
    # pass info for the temperature, humidity, wind speed, and sunset time!
    # HINT: It may be useful to create 2 new dictionaries, `city1_info` and 
    # `city2_info`, to organize the data.

    raw_datenow = datetime.now()
    formatted_datenow = raw_datenow.strftime('%B %d, %Y at %I:%M %p')

    # Convert timestamps to datetime objects
    utc_sunrise1 = datetime.utcfromtimestamp(city1_result['sys']['sunrise'])
    utc_sunset1 = datetime.utcfromtimestamp(city1_result['sys']['sunset'])
    timezone_offset2 = city2_result['timezone']
    utc_sunrise2 = datetime.utcfromtimestamp(city2_result['sys']['sunrise'])
    utc_sunset2 = datetime.utcfromtimestamp(city2_result['sys']['sunset'])
    local_sunrise2 = utc_sunrise2 + timedelta(seconds=timezone_offset2)
    local_sunset2 = utc_sunset2 + timedelta(seconds=timezone_offset2)
    formatted_local_sunrise2 = local_sunrise2.strftime('%I:%M %p')
    formatted_local_sunset2 = local_sunset2.strftime('%I:%M %p')

    # Apply timezone offset
    timezone_offset1 = city1_result['timezone']
    local_sunrise1 = utc_sunrise1 + timedelta(seconds=timezone_offset1)
    local_sunset1 = utc_sunset1 + timedelta(seconds=timezone_offset1)
    formatted_local_sunrise1 = local_sunrise1.strftime('%I:%M %p')
    formatted_local_sunset1 = local_sunset1.strftime('%I:%M %p')

    #compare temp
    raw_degree_difference = abs(city1_result['main']['temp'] - abs(city2_result['main']['temp']))
    degree_difference = round(raw_degree_difference, 2)
    if city1_result['main']['temp'] > city2_result['main']['temp']:
        city1tempdiff = 'warmer'
    elif city1_result['main']['temp'] < city2_result['main']['temp']:
        city1tempdiff = 'colder'
    else:
        city1tempdiff = 'same'
    
    #compare Humidity
    humid_difference = abs(city1_result['main']['humidity'] - city2_result['main']['humidity'])
    if city1_result['main']['humidity'] > city2_result['main']['humidity']:
        city1humid_diff = 'greater'
    elif city1_result['main']['humidity'] < city2_result['main']['humidity']:
        city1humid_diff = 'less'
    else:
        city1humid_diff = 'same'
    #compare wind
    raw_wind_difference = abs(city1_result['wind']['speed'] - city2_result['wind']['speed'])
    wind_difference = round(raw_wind_difference, 2)
    if city1_result['wind']['speed'] > city2_result['wind']['speed']:
        city1wind_diff = 'greater'
    elif city1_result['wind']['speed'] < city2_result['wind']['speed']:
        city1wind_diff = 'less'
    else:
        city1wind_diff = 'same'

    #compare sunsets
    sunset_difference = divmod((local_sunrise1 - local_sunrise2).seconds, 3600)
    if local_sunrise1 > local_sunrise2:
        sunset1_diff = 'later'
    elif local_sunrise1 < local_sunrise2:
        sunset1_diff = 'earlier'
    else:
        sunset1_diff = 'same'

    context = {
        'date': formatted_datenow,
        'city1': city1_result['name'],
        'description1': city1_result['weather'][0]['description'],
        'distance_letter': get_distance_for_units(units),
        'temp1': city1_result['main']['temp'],
        'humidity1': city1_result['main']['humidity'],
        'wind_speed1': city1_result['wind']['speed'],
        'sunrise1': formatted_local_sunrise1,
        'sunset1': formatted_local_sunset1,
        'units_letter': get_letter_for_units(units),
        'city2': city2_result['name'],
        'description2': city2_result['weather'][0]['description'],
        'temp2': city2_result['main']['temp'],
        'humidity2': city2_result['main']['humidity'],
        'wind_speed2': city2_result['wind']['speed'],
        'sunrise2': formatted_local_sunrise2,
        'sunset2': formatted_local_sunset2,
        'temp_difference': degree_difference,
        'temp_warm_cold': city1tempdiff,
        'humidity_difference': humid_difference,
        'humidity_great_less': city1humid_diff,
        'wind_difference': wind_difference,
        'wind_fast_slow': city1wind_diff,
        'sunset_diff': sunset_difference,
        'sunset_early_late': sunset1_diff,
    }

    return render_template('comparison_results.html', **context)

@app.route('/error')
def error():
    message = request.args.get('message', 'An error occurred.')
    return render_template('error.html', message=message)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
