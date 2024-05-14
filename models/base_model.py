#!/usr/bin/python3
import uuid
from datetime import datetime
from models.__init__ import storage
"""a script that creates a class base_model"""


strptime = datetime.strptime


class BaseModel:
    """
    A base class for other classes to inherit from.

    Attributes:
        id (str): A unique identifier generated using UUID.
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, vl in kwargs.items():
                if key != '__class__':
                    if key in ('updated_at', 'created_at'):
                        vl = strptime(vl, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, vl)
            self.id = kwargs.get('id')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        storage.new()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            __class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""
        new_dictonary = self.__dict__.copy()
        new_dictonary['__class__'] = self.__class__.__name__
        new_dictonary['updated_at'] = self.updated_at.isoformat()
        new_dictonary['created_at'] = self.created_at.isoformat()

        return new_dictonary

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()
