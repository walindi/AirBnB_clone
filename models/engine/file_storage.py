#!/usr/bin/python3
"""file storage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances

    Private class attributes:
        __file_path (str): path to the JSON file
        __objects (dict): dictionary to store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            dic = {}
            for k, v in self.__objects.items():
                dic[k] = v.to_dict()

            json.dump(dic, f)

    def reload(self):
        """Deserializes the json file to __objects,
        only if the json file (__file_path) exists
        """

        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)

                for key, obj in data.items():
                    self.__objects = {
                            key: eval(obj["__class__"])(**obj)
                            }
        except FileNotFoundError:
            return
