""" Database model for Hiking Bucket List """

import json
from flask import g, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict

db_url = 'bucketList.db'

database = SqliteDatabase(db_url)


# Table Model for user saved trail records
# id will be unique trail id passed from the api, not an auto increment
class Trail(Model):

    id = IntegerField(primary_key=True)
    name = CharField()
    location = CharField()
    summary = CharField()
    difficulty = CharField()
    stars = DoubleField()
    latitude = DoubleField()
    longitude = DoubleField()
    length = DoubleField()
    imgSmallMed = CharField()
    hasHiked = BooleanField(default=False)

    class Meta:
        database = database

    # overwrite str method to show the information of a Trail record
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Location: {self.location}, Summary: {self.summary}, Difficulty: {self.difficulty}, Stars: {self.stars}, Latitude: {self.latitude}, Longitude: {self.longitude}, Length: {self.length} Photo URL: {self.imgSmallMed}, You have hiked this: {self.hasHiked}'


# Create table model for saved search cache
class Search (Model):

    id = AutoField(primary_key=True)
    location = CharField()

    class Meta:
        database = database


# Create the tables in the database
database.create_tables([Trail, Search])


def open_close_connection(func):
    """
    Decorator used to open and close connections.
    """
    def decorated_function(*args):
        g.db = database
        g.db.connect()

        response = func(*args)

        g.db.close()
        return response
    return decorated_function


# FOR ALL BELOW DATABASE METHODS
# The Following imported functions are applied
# Playhouse shortcut model_to_dict: Converts the record from a table model object (c) to a dictionary object
# Flask function jsonify: Converts the dictionary to JSON to return a JSON object to the api

# return all trail records from the database based on whether they have or have not hiked the trail

@open_close_connection
def get_saved_trails():
    records = Trail.select()
    return jsonify([model_to_dict(c) for c in records])


@open_close_connection
def get_bucket_list():
    records = Trail.select().where(Trail.hasHiked == 0)
    return jsonify([model_to_dict(c) for c in records])


@open_close_connection
def get_hiked():
    records = Trail.select().where(Trail.hasHiked == 1)
    return jsonify([model_to_dict(c) for c in records])


# return a trail record for the passed trail id
# Throw DoesNotExist exception if not found, return 404 not found code
@open_close_connection
def get_by_id(trail_id):
    try:
        c = Trail.get_by_id(trail_id)
        return jsonify(model_to_dict(c)), 200
    except DoesNotExist:
        return 'Trail Not Found', 404


# add a new trail record to the database
# request the trail information from the api
# return 210 if the record was successfully created
@open_close_connection
def add_trail():
    with database.atomic():
        c = Trail.create(**request.json)
        return jsonify(model_to_dict(c)), 201


# update an existing trail record when user changes hiked status
@open_close_connection
def update_trail(trail_id):
    with database.atomic():
        print(request.get_json(force=True))
        Trail.update(**request.get_json(force=True))\
            .where(Trail.id == trail_id)\
            .execute()
        return 'ok', 200

@open_close_connection
def delete_trail(trail_id):
    with database.atomic():
        Trail.delete()\
            .where(Trail.id == trail_id)\
            .execute()

    return 'ok', 200


@open_close_connection
def add_search():
    with database.atomic():
        c = Trail.create(**request.json)
        return jsonify(model_to_dict(c)), 201


# pull from search based on location
# return 404 if not found
@open_close_connection
def get_search(location_entered):
    try:
        c = Trail.select().where(Trail.location == location_entered)
        return jsonify(model_to_dict(c))
    except DoesNotExist:
        return 'not found', 404
