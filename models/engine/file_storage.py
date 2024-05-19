#!/usr/bin/python3
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
        """Deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens."""
        try:
            with open(self.__file_path, 'r') as f:
                dictionary_obj = json.load(f)
                for key, value in dictionary_obj.items():
                    class_name = value["__class__"]
                    module_name = f"models.{self._to_snake_case(class_name)}"
                    module = __import__(module_name, fromlist=[class_name])
                    obj_class = getattr(module, class_name)
                    obj = obj_class(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
        except KeyError as e:
            print(f"KeyError: {e}")
        except ImportError as e:
            print(f"ImportError: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _to_snake_case(self, name):
        """Converts CamelCase to snake_case."""
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
