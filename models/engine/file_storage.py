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
    className = {'BaseModel' : BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place' Place,
            'Review' : Review}
    
    def all(self):
     """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file(path: __file_path)"""
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """
        function that deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                f_contents = f.read()
                dict_obj_dicts = json.loads(f_contents)
            for key in dict_obj_dicts.keys():
                obj_dict = dict_obj_dicts[key]
                # FileStorage.__objects[key] = BaseModel(**obj_dict)
                FileStorage.__objects[key] = FileStorage\
                           .className[key.split('.')[0]](**obj_dict)
        except FileNotFoundError:
            pass
