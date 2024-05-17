# models/engine/file_storage.py
import json


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
        with a key formatted as <class name>.<id>.
"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes the __objects dictionary to
        the JSON file specified by __file_path."""
        jso_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}

        with open(self.__file_path, 'w') as f:
            json.dump(jso_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(self.__file_path, 'r') as f:
                dictionary_objj = json.load(f)

                for key, value in dictionary_objj.items():
                    clss_nm = value["__class__"]

                    if clss_nm == 'BaseModel':
                        from models.base_model import BaseModel
                        obj_class = BaseModel
                    elif clss_nm == 'User':
                        from models.user import User
                        obj_class = User
                    elif clss_nm == 'Place':
                        from models.place import Place
                        obj_class = Place
                    elif clss_nm == 'State':
                        from models.state import State
                        obj_class = State
                    elif clss_nm == 'City':
                        from models.city import City
                        obj_class = City
                    elif clss_nm == 'Amenity':
                        from models.amenity import Amenity
                        obj_class = Amenity
                    elif clss_nm == 'Review':
                        from models.review import Review
                        obj_class = Review
                    else:
                        raise ImportError(
                            f"Class {clss_nm} is not recognized")

                    obj = obj_class(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
