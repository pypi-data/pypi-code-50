import requests
import json

BASE_URL = "https://www.metaweather.com/api/"
LOCATION_SEARCH_URL = BASE_URL + "location/search/"
WEATHER_INFO_URL = BASE_URL + "location/{}/"

"""
	get location id
"""
def get_location_id(query):
    r = requests.get(LOCATION_SEARCH_URL, params={'query': query})
    data = r.json()
    # json_dict = json.loads(data)[0]
    if len(data):
        return data[0]['woeid']


"""
get weather_report data
"""
def get_weather(query, days=1):
    location_id = get_location_id(query)
    if location_id is None:
        return "Location not found."
    r = requests.get(WEATHER_INFO_URL.format(location_id))
    data =r.json()
    result = {}
    result['location'] = data['title']
    result['weather_report'] = []
    for day_weather in data['consolidated_weather'][:days]:
        result['weather_report'].append({
            'date': day_weather['applicable_date'],
            'min_temp': round(day_weather['min_temp'], 2),
            'max_temp': round(day_weather['max_temp'], 2),
            'weather_state_name': day_weather['weather_state_name']
        })
    return result


"""
	print weather_report details
"""
def print_weather_details(data):
    print("Location:", data['location'], end='\n\n')
    for row in data['weather_report']:
        print("Date:", row['date'])
        print("Weather Type:", row['weather_state_name'])
        print("Min Temp.:", row['min_temp'])
        print("Max Temp.:", row['max_temp'])
        print()
