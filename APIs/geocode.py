import requests

def geocode(city, state):

    # encodedCity = city.replace(' ', '%20')

    url = 'https://nominatim.openstreetmap.org/search'
    query = {'format':'json','city':city, 'state':state}
    data = requests.get(url, params=query).json()
    lat = data[0]['lat']
    long = data[0]['lon']
    print(lat, long)

    return lat, long
geocode('maple grove', 'mn')