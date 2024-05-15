# models/engine/file_storage.py
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        jso_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}

        with open(self.__file_path, 'w') as f:
            json.dump(jso_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                dict_obj = json.load(f)

                for key, value in dict_obj.items():
                    class_name = value["__class__"]

                    if class_name == 'BaseModel':
                        from models.base_model import BaseModel
                        obj_class = BaseModel
                    elif class_name == 'User':
                        from models.user import User
                        obj_class = User

                    else:
                        raise ImportError(f"Class {class_name} is not recognized")

                    obj = obj_class(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
