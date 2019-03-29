import requests
import os
import APIs.geocode as geoCode

def get_trail(lat, lon):
    key = os.environ.get('TRAIL_KEY')
    query = {'lat':lat, 'lon':lon, 'key':key, 'maxDistance':10, 'maxResults':5}
    url = 'https://www.hikingproject.com/data/get-trails'

    data = requests.get(url, params=query).json()
    return data
