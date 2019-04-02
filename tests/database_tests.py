from unittest import *
from peewee import *
import model
from model import Trail


class TestAddTrailDB(TestCase):
    # create a test database url
    test_db = 'test_db.sqlite'

    def setUp(self):

        model.db_url = self.test_db
        model.database.connect(self.test_db)
        model.database.create_tables([Trail])
        model.Trail.create(
            id=12345,
            name='Test Trail',
            location='Test City, Test State',
            summary='This is a test of adding a Trail to the database',
            difficulty='Test Blue',
            stars=4.5,
            latitude=44.00,
            longitude=56.5,
            length=5.3,
            imgSmallMed='test_photo.jpg',
            hasHiked=False)

    def tearDown(self):
        model.Trail.delete().where(model.Trail.id == 12345).execute()
        model.db_url = model.db_url

    def test_add_trail(self):
        trail = model.Trail.get(id=12345)
        self.assertEquals(trail.id, 12345)

    def test_update_trail(self):
        success = model.Trail.update(hasHiked=True).where(model.Trail.id == 12345).execute()
        self.assertEquals(success.hasHiked, True)






