import requests
import requests_cache

requests_cache.install_cache()

def geocode(city, state):

    # encodedCity = city.replace(' ', '%20')

    try:
        url = 'https://nominatim.openstreetmap.org/search'
        query = {'format':'json','city':city, 'state':state}
        data = requests.get(url, params=query).json()
        lat = data[0]['lat']
        long = data[0]['lon']
    except IndexError as ie:
        return data
    except requests.exceptions.HTTPError as http_error:
        print("There's a Http Error", http_error)
    except requests.exceptions.ConnectionError as conn:
        print("There's a connection error", conn)
    except requests.exceptions.Timeout as timeout:
        print("There is a timeout Error", timeout)
    except requests.exceptions.RequestException as error:
        print("Something went wrong", error)

    return lat, long
