import requests
import os
import APIs.geocode as geoCode

def get_trail(lat, lon):
    key = os.environ.get('TRAIL_KEY')
    query = {'lat':lat, 'lon':lon, 'key':key, 'maxDistance':10}
    url = 'https://www.hikingproject.com/data/get-trails'
    data = requests.get(url, params=query).json()

    trail_items = data['trails']


    for trail in trail_items:
        trail_ID=trail['id']
        print(trail_ID)
        name = trail['name']
        print(name)
        summary = trail['summary']
        stars = trail['stars']




get_trail(40.0274, -105.2519)


