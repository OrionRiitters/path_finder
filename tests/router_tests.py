from unittest import TestCase, mock
from flask import Flask
from app import app
import handlers.api_handler as api
import APIs.getTrails as getTrails
import APIs.geocode as geo
keys = ['id', 'name', 'summary', 'difficulty', 'stars', 'latitude', 'longitude', 'length', 'imgSmallMed']
un_wanted_keys = ['type', 'summary', 'starVotes', 'url', 'imgSqSmall', 'imgSmall', 'imgMedium', 'length', 'imgSmallMed']

# tests for the router and handlers
class TestHandlers(TestCase):
    def test_get_trails_route(self):
        with app.test_client() as c:
            # response = c.post('/get_trails', data={"city": "minneapolis", "state": "mn"})
            # self.assertEquals(response.status_code, 200)

            response = c.get('/')
            self.assertEquals(response.status_code, 200)


    def test_database_handler(self):
        print("hello")
