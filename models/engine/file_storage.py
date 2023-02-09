#!/usr/bin/python3
import json
import os


"""serializes instances to a JSON file and
    deserializes JSON file to instances
"""


class FileStorage:
    """ File storage Engine
    class Attributes:
        __file_path(str) ->  path to the JSON file
        __objects(dict) ->   store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj(object) -> The object to add to __objects
        """
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__class__.__objects[key] = obj
