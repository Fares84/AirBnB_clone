#!/usr/bin/python3
""" TestBaseModel module for testing the BaseModel class"""
import unittest
from models.base_model import BaseModel
import uuid
import os
import datetime


class TestBaseModel(unittest.TestCase):
    """ Tests for the BaseModel class """

    def test_id(self):
        """ test id """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_str(self):
        """ test string """
        bm = BaseModel()
        self.assertEqual(type(bm.__str__()), str)

    def test_save(self):
        """ test save to json """
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        """ test attributes to dict """
        bm = BaseModel()
        bm.my_name = "Holberton"
        bm.my_number = 89
        bm_to_json = bm.to_dict()
        self.assertIsInstance(bm_to_json["my_number"], int)
        self.assertIsInstance(bm_to_json["my_name"], str)
        self.assertIsInstance(bm_to_json["__class__"], str)
        self.assertIsInstance(bm_to_json["updated_at"], str)
        self.assertIsInstance(bm_to_json["created_at"], str)
        self.assertIsInstance(bm_to_json["id"], str)

    def test_init(self):
        """ test inti """
        test1 = BaseModel()
        test1.number = 89
        test1.name ="holberton"
        test2 = BaseModel(**test1.to_dict())

        self.assertEqual(test1.id, test2.id)
        self.assertEqual(test1.created_at, test2.created_at)
        self.assertEqual(test1.updated_at, test2.updated_at)
        self.assertEqual(test2.number, 89)
        self.assertEqual(test2.name, "holberton")

if __name__ == '__main__':
    unittest.main()