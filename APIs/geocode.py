import requests

def geocode(city, state):

    encodedCity = city.replace(' ', '%20')

    url = 'https://nominatim.openstreetmap.org/search/?format=json&city='+encodedCity+'&state='+state
    query = {'format':'json','city':encodedCity, 'state':state}
    data = requests.get(url).json()
    lat = data[0]['lat']
    long = data[0]['lon']
    print(lat, long)

    return lat, long
geocode('maple grove', 'mn')