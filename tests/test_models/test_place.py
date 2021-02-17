#!/usr/bin/python3
"""
   TestPlace module
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    TestPlace class
    """
    def test_create_place_instance(self):
        """
        Test instance creation
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_variables_of_place(self):
        """
        test variables creation
        """
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_id_place(self):
        """
        test unique id for place
        """
        place1_id = Place()
        place2_id = Place()
        self.assertNotEqual(place1_id, place2_id)

if __name__ == '__main__':
    unittest.main()
