import requests
import os

import requests_cache

requests_cache.install_cache()

def get_trail(lat, lon):
    key = os.environ.get('TRAIL_KEY')
    try:
        query = {'lat':lat, 'lon':lon, 'maxDistance':10, 'maxResults':5, 'key': key}
        url = 'https://www.hikingproject.com/data/get-trails'

        data = requests.get(url, params=query).json()
    except requests.exceptions.HTTPError as http_error:
        print("There's a Http Error", http_error)
    except requests.exceptions.ConnectionError as conn:
        print("There's a connection error", conn)
    except requests.exceptions.Timeout as timeout:
        print("There is a timeout Error", timeout)
    except requests.exceptions.RequestException as error:
        print("Something went wrong", error)
    return data
