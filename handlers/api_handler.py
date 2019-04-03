# this class will invoke the api classes and methods and send it and get data from it
import APIs.geocode as geocode
import APIs.getTrails as getTrails
import json
# dict keys that are wanted
keys = ['id', 'name', 'summary', 'difficulty', 'stars', 'latitude', 'longitude', 'length', 'imgSmallMed']


# gets trails from location
# parameter: city and state returned from the user
def get_trails_from_location(city, state):
    loc = geocode.geocode(city, state)
    if len(loc) == 0:
        return json.dumps(loc)
    trails = getTrails.get_trail(loc[0], loc[1])
    if len(trails['trails']) == 0:
        return json.dumps(trails['trails'])
    location = make_location(city, state)
    new_trails = json.dumps(filter_trails(trails, location))
    return new_trails


# filters trail json for rendering and saving in database
def filter_trails(trails, location):
    new_trails = []
    for trail in trails['trails']:
        new_dict = {key: trail[key] for key in keys}
        new_dict['location'] = location
        new_trails.append(new_dict)
    return new_trails


# concatenating city and state together
def make_location(city, state):
    location = city + ", " + state
    return location
