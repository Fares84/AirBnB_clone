#!/usr/bin/python3
"""
   TestFileStorage module
"""
import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """
       The unittest module provides a rich set of tools for
    constructing and running tests
    """
    def test_instance(self):
        """
        if it's a FileStorage instance
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_obj_dict(self):
        """
        test object must be dictionary
        """
        obj = storage.all()
        self.assertIsInstance(obj, dict)

    def test_file_path(self):
        """
        check file path
        """
        file_path = FileStorage()._FileStorage__file_path
        self.assertIsInstance(file_path, str)

    def test_file_exists(self):
        """
        Test if file exist
        """
        self.assertTrue(os.path.exists("file.json"))

    def test_all(self):
        """
        Test all method
        """
        _all = storage.all()
        self.assertIsInstance(_all, dict)

    def test_new(self):
        """
        test new method
        """
        obj = BaseModel()
        storage.new(obj)
        obj_id = "BaseModel.{}".format(obj.id)
        self.assertIn(obj_id, storage.all())

    def test_save(self):
        """
        test save method
        """
        storage.save()
        t1 = os.path.getsize(FileStorage._FileStorage__file_path)
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        t2 = os.path.getsize(FileStorage._FileStorage__file_path)
        self.assertNotEqual(t1, t2)

    def test_reload_method(self):
        """
        test reload method
        """
        t1 = len(FileStorage._FileStorage__objects)
        storage.reload()
        t2 = len(FileStorage._FileStorage__objects)
        self.assertEqual(t1, t2)

    def test_save_2_datetime(self):
        """
        test 2 date not equal
        """
        date = BaseModel()
        updat_at1 = date.updated_at
        updat_at2 = datetime.now()

if __name__ == '__main__':
    unittest.main()
