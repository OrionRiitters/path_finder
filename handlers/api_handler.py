# this class will invoke the api classes and methods and send it and get data from it
import APIs.geocode as geocode
import APIs.getTrails as getTrails
import json

keys = ['id', 'name', 'summary', 'difficulty', 'stars', 'latitude', 'longitude', 'length', 'imgSmallMed']


def get_trails_from_location(city, state):
    lat, lon = geocode.geocode(city, state)
    trails = getTrails.get_trail(lat, lon)
    new_trails = json.dumps(filter_trails(trails))
    return new_trails


# filters trail json for rendering and saving in database
def filter_trails(trails):
    new_trails = []
    for trail in trails['trails']:
        new_dict = {key: trail[key] for key in keys}
        new_trails.append(new_dict)
    return new_trails
