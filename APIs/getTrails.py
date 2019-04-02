import requests
import os
import APIs.geocode as geoCode

def get_trail(lat, lon):
    key = os.environ.get('TRAIL_KEY')
    query = {'lat':lat, 'lon':lon, 'maxDistance':15, 'maxResults':25, 'key': key}
    url = 'https://www.hikingproject.com/data/get-trails'

    data = requests.get(url, params=query).json()
    return data
