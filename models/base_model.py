#!/usr/bin/python3
"""
BaseModel module
"""
from datetime import datetime
import uuid


class BaseModel():
    """
    Basemodel class for all common attributes/methods
    Public instance attributes:
    id: string - assign with an uuid when an instance is created:
        uuid.uuid4(): generate unique id but dont forget to convert to a string
        the goal is to have unique id for each BaseModel
    created_at: datetime - assign with the current datetime when an instance
        is created
    updated_at: datetime - assign with the current datetime when an instance
        is created and it will be updated every time you change your object
    """
    def __init__(self, *args, **kwargs):
        """
        initializer
        id (int): public instance attribute
        """
        from models import storage
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, time_format)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """
        Human readable format
        __str__ method should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        save method updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method will be the first piece of the serialization/
        deserialization process: create a dictionary representation
        with simple object type of our BaseModel.
        Returns: a dictionary containing all keys/values of __dict__
        (return the dictionary format of instance)
        """
        _dict = dict(self.__dict__)
        _dict["created_at"] = _dict["created_at"].isoformat()
        _dict["updated_at"] = _dict["updated_at"].isoformat()
        _dict["__class__"] = self.__class__.__name__
        return _dict
