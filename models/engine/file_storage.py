#!/usr/bin/python3
"""file storage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances

    Private class attributes:
        __filepath (str): path to the JSON file
        __objects (dict): dictionary to store all objects by <class name>.id
    """

    __filepath = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path)"""
