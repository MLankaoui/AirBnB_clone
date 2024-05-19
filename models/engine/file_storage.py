#!/usr/bin/python3
import json
from json import dump
from json import load
import os
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """FileStorage class that handles the serialization
    and deserialization of objects to and from a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        which contains all stored objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary
        with a key formatted as <class name>.<id>."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes the __objects dictionary to
        the JSON file specified by __file_path."""
        json_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}

        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """reload"""
        from models.base_model import BaseModel

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r",
                          encoding="utf-8") as jsonF:
                    json_data = load(jsonF)
                    for key, value in json_data.items():
                        if '.' in key:
                            class_name, obj_id = key.split('.')
                            class_obj = globals()[class_name]
                            new_instance = class_obj(**value)
                            self.new(new_instance)
                            self.__objects[key] = new_instance
            except FileNotFoundError:
                pass

    def _to_snake_case(self, name):
        """Converts CamelCase to snake_case."""
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
