#/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}


    def all(self):
        key = "{}.{}".format(self.__class__.__name__, self.id)
        FileStorage.__objects[key] = self.to_dict()
    

    def new(self, obj):
        obj = obj[self.__class__.__name__.__objetcs]
        FileStorage.objects = obj


    def save(self):
        with open("file.json", "a", encoding="UTF-8") as json_file:
            json.dumps(FileStorage, json_file, indent=4)


    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as json_file:
                FileStorage.__objects = json.loads(json_file)