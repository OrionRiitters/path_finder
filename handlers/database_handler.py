# this class will invoke the database classes and methods and get and send them data
from model import *


# method uses trail id to look up if the trail is in the database it will update it if not it will add it
def save_trails(trail_id):
    response, code = get_by_id(trail_id)
    if response == 'Trail Not Found':
        add_trail()
    else:
        update_trail(trail_id)


# getting the saved trails ie the bucket list
def return_bucket_list():
    bucket_list = get_bucket_list()
    return bucket_list


# returning hiked trails
def get_hiked_trails():
    return get_hiked()


# returning the saved trails
def get_all_trails():
    return get_saved_trails()
