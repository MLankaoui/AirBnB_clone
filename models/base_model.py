#!/usr/bin/python3
import uuid
from datetime import datetime
"""a script that creates a class base_model"""


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    
    def __str__(self):
        return "[{}] ({}) ({})".format(__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        new_dictonary = self.__dict__.copy()
        new_dictonary['__class__'] = self.__class__.__name__
        new_dictonary['updated_at'] = self.updated_at.isoformat()
        new_dictonary['created_at'] = self.created_at.isoformat()

        return new_dictonary

    def save(self):
        self.updated_at = datetime.now()


    