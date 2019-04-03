from unittest import TestCase
import model as test_model
from model import Trail
from playhouse.shortcuts import model_to_dict


class TestAddTrailDB(TestCase):
    # create a test database url
    test_db = 'test_db.sqlite'
    old_db = 'bucketList.db'

    def setUp(self):

        test_model.db_url = self.test_db
        test_model.database.connect(self.test_db)
        test_model.database.create_tables([Trail])
        test_model.Trail.delete().execute()

        # Create test data
        test_model.Trail.create(
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
        test_model.database.drop_tables([Trail])
        test_model.database.close()


    # BELOW TESTS - Test that the database is working properly first, not the methods.
    def test_add_trail(self):
        trail = test_model.Trail.get(id=12345)
        self.assertEqual(trail.id, 12345)


    def test_update_trail(self):
        test_model.Trail.update(hasHiked=True).where(test_model.Trail.id == 12345).execute()
        trail = test_model.Trail.get(id=12345)
        self.assertTrue(trail.hasHiked)

    def test_get_bucketlist(self):
        test_model.Trail.create(
            id=23456,
            name='Test Trail Two',
            location='Test New City, Test State',
            summary='This is a test of adding a second Trail to the database',
            difficulty='Test Green',
            stars=4.6,
            latitude=-44.00,
            longitude=56.8,
            length=12.3,
            imgSmallMed='test_photo2.jpg',
            hasHiked=False).save()

        trails = test_model.Trail.select().where(test_model.Trail.hasHiked == 0)
        trail_keys = [model_to_dict(trail) for trail in trails]
        sql_vals = test_model.database.execute_sql('SELECT * FROM Trail WHERE hasHiked = 0').fetchall()
        self.assertEqual(len(trail_keys[0].keys()), len(sql_vals[0]))
        count = 0
        for row in sql_vals:
            self.assertIn(row[count], trail_keys[count].values())
            self.assertEqual(trail_keys[count]['id'], row[0])
            count += 1


















