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
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_str(self):
        """ test string """
        base = BaseModel()
        self.assertEqual(type(base.__str__()), str)

    def test_save(self):
        """ test save to json """
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict_format(self):
        """
        Tests to_dict method
        """
        base = BaseModel()
        base.name = "Betty"
        base.number = 89
        base_model = base.to_dict()
        crea_at = base.created_at.isoformat()
        upda_at = base.updated_at.isoformat()
        base_id = base.id
        expected = {
            "name": "Betty",
            "number": 89,
            "id": base_id,
            "__class__": "BaseModel",
            "created_at": crea_at,
            "updated_at": upda_at
            }

    def test_to_dict(self):
        """ test attributes to dict """
        base = BaseModel()
        base.my_name = "Holberton"
        base.my_number = 89
        base_to_json = base.to_dict()
        self.assertIsInstance(base_to_json["my_number"], int)
        self.assertIsInstance(base_to_json["my_name"], str)
        self.assertIsInstance(base_to_json["__class__"], str)
        self.assertIsInstance(base_to_json["updated_at"], str)
        self.assertIsInstance(base_to_json["created_at"], str)
        self.assertIsInstance(base_to_json["id"], str)

    def test_instance_kwargs(self):
        """
        test instance with multiple args
        """
        kwargs = {"name": "Holberton", "number": 89}
        base = BaseModel(**kwargs)
        self.assertEqual(base.name, "Holberton")
        self.assertEqual(base.number, 89)

if __name__ == '__main__':
    unittest.main()
