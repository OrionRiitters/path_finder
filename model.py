""" Database model for Hiking Bucket List """

from flask import g, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict

# import Flask web app from app.py to connect route requests
from app import app

database = SqliteDatabase('bucketList.db')


# Table Model for user saved trail records
# id will be unique trail id passed from the api, not an auto increment
class Trail(Model):

    id = IntegerField(primary_key=True)
    name = CharField()
    location = CharField()
    description = CharField()
    difficulty = CharField()
    stars = DoubleField()
    latitude = DoubleField()
    longitude = DoubleField()
    length = DoubleField()
    photoUrl = CharField()
    hasHiked = BooleanField(default=False)

    class Meta:
        database = database


# Create table model for saved search cache
class Search (Model):

    id = AutoField(primary_key=True)
    location = CharField()

    class Meta:
        database = database


# Create the tables in the database
database.create_tables([Trail, Search])


# need to connect to the database before every request
# g is one request instance
# decorated to auto call this database connection instance for every request
@app.route.before_request
def before_request():
    g.db = database
    g.db.connect()


# close connection instance once request is completed
# receives the response from the request, returns it to api
# decorated to auto call after request instance
@app.route.after_request
def after_request(response):
    g.db.close()
    return response


# FOR ALL BELOW DATABASE METHODS
# The Following imported functions are applied
# Playhouse shortcut model_to_dict: Converts the record from a table model object (c) to a dictionary object
# Flask function jsonify: Converts the dictionary to JSON to return a JSON object to the api


# return all trail records from the database based on whether they have or have not hiked the trail
def get_bucket_list():
    records = Trail.select().where(Trail.hasHiked == 0)
    return jsonify(model_to_dict(c) for c in records)


def get_hiked():
    hiked = Trail.select().where(Trail.hasHiked == 1)
    return jsonify(model_to_dict(c) for c in hiked)


# return a trail record for the passed trail id
# Throw DoesNotExist exception if not found, return 404 not found code
def get_by_id(trail_id):
    try:
        c = Trail.get_by_id(trail_id)
        return jsonify(model_to_dict(c))
    except DoesNotExist:
        return 'Trail Not Found', 404


# add a new trail record to the database
# request the trail information from the api
# return 210 if the record was successfully created
def add_trail():
    with database.atomic():
        c = Trail.create(**request.form.to_dict())
        return jsonify(model_to_dict(c)), 201


# update an existing trail record when user changes hiked status
def update_trail(trail_id):
    with database.atomic():
        Trail.update(**request.form.to_dict())\
            .where(Trail.id == trail_id)\
            .execute()
        return 'ok', 200


# add a search location to the cache
def add_search():
    with database.atomic():
        c = Trail.create(**request.form.to_dict())
        return jsonify(model_to_dict(c)), 201


# pull from search based on location
# return 404 if not found
def get_search(location_entered):
    try:
        c = Trail.select().where(Trail.location == location_entered)
        return jsonify(model_to_dict(c))
    except DoesNotExist:
        return 'not found', 404
