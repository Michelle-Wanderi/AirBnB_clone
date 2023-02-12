#!/usr/bin/python3
""""This module provides the BaseClass,
from which all other classes will inherit thier properties"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """This is the parent class where all the classes will inherit from

   Attributes:
   id: the basemodel id
   created_at : the datetime at creation
   updated_at : the datetime of last update

    Methods:
    __init__(self, *args, **kwargs)
    __str__(self)
    __save(self)
    __repr__(self)
    to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Initializes class instances, attributes(uuid, created/updated)
        If kwargs is not empty its creates an instance
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    created = datetime.fromisoformat(value)
                    self.created_at = created
                elif key == 'updated_at':
                    updated = datetime.fromisoformat(value)
                    self.updated_at = updated
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the objects of this class"""
        return ("[{}] {} {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """

        properties = self.__dict__.copy()
        properties["__class__"] = self.__class__.__name__
        properties["created_at"] = self.created_at.isoformat()
        properties["updated_at"] = self.updated_at.isoformat()
        return properties
