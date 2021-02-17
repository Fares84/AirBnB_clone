#!/usr/bin/python3
"""
   TestCity module
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    TestCity class
    """
    def test_create_city_instance(self):
        """
        Test instance creation
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_variables_of_city(self):
        """
        test variables creation
        """
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_id_city(self):
        """
        test unique id for city
        """
        city1_id = City()
        city2_id = City()
        self.assertNotEqual(city1_id, city2_id)

if __name__ == '__main__':
    unittest.main()
