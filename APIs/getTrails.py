import requests
import os
import APIs.geocode as geoCode

def get_trail(lat, lon):
    key = os.environ.get('TRAIL_KEY')
    query = {'lat':lat, 'lon':lon, 'key':key, 'maxDistance':10, 'maxResults':5}
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
        print(stars)
        starVotes = trail['starVotes']
        print(starVotes)
        image_url = trail['imgMedium']
        length = trail['length']




get_trail(40.0274, -105.2519)


