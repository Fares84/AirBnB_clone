#!/usr/bin/python3
""" FileStorage class """
import json
from os import path
from models.base_model import BaseModel


class FileStorage():
    """ [FileStorage] serializes instances to a JSON file and deserializes
    JSON file to instances

    ATTRIBUTES:
    __file_pathh is a private class attribute (str) path to the JSON file

     __objects is a private class attribute (dict) that is empty but will
    store all objects by <class name>.id ex: to store a BaseModel object
    with id=12121212, the key will be BaseModel.12121212)

    PUBLIC INSTANCE METHODS
    all():
    new(obj):
    save():
    reload():
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        [all] methods

        Returns:
            [dict]: [dictionary containing objects]
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        [new] new method sets in __objects the obj with
        key <obj class name>.id

        Args:
            obj ([object]): [object to be created]
        """
        _id = obj.id
        key = str(obj.__class__.__name__) + "." + _id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        [save] save method serializes __objects to the JSON file
        (path: __file_path)
        """
        _dict = {}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            for _key, _value in FileStorage.__objects.items():
                _dict[_key] = _value.to_dict()
            json.dump(_dict, file)

    def reload(self):
        """
        [reload] deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised)
        """
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r") as file:
                obj = json.load(file)
                for key, value in obj.items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
        else:
            return
