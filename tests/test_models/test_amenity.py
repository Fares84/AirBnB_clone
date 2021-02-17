#!/usr/bin/python3
"""
   TestAmenity module
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    TestAmenity class
    """
    def test_create_amenity_instance(self):
        """
        Test instance creation
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_variables_of_amenity(self):
        """
        test variables creation
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_id_amenity(self):
        """
        test unique id for amenity
        """
        amenity1_id = Amenity()
        amenity2_id = Amenity()
        self.assertNotEqual(amenity1_id, amenity2_id)

if __name__ == '__main__':
    unittest.main()
