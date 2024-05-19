#!/usr/bin/python3
"""
This module defines the BaseModel class, a base class for all models
in the application, providing common attributes and methods.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel is a base class for all models in the application.

    Attributes:
        id (str): A unique identifier
        for each instance of the model.
        created_at (datetime):
        The datetime when the instance was created.
        updated_at (datetime):
        The datetime when the instance was last updated.

    Methods:
        __init__(self, *args, **kwargs):
        Initializes a new instance of BaseModel.
        __str__(self): Returns a string representation of the instance.
        save(self): Updates the updated_at attribute
        with the current datetime and saves the instance.
        to_dict(self): Returns a dictionary containing
        all keys/values of the instance's __dict__.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('updated_at', 'created_at'):
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

        from models import storage
        storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current
        datetime and saves the instance.

        The save method should be called to persist
        the instance's state to the storage.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """ dict """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__

        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                new_dict[key] = val.isoformat()
            else:
                new_dict[key] = val
        return new_dict
