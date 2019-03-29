# this class will invoke the database classes and methods and get and send them data
from model import *


# method uses trail id to look up if the
def save_trails(trail_id):
    response, code = get_by_id(trail_id)
    if response != 'Trail Not Found':
        add_trail()
    elif response == 'Trail Not Found':
        update_trail(trail_id)


def get_bucket_list():
    bucket_list = get_bucket_list()
    return bucket_list
