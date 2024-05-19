#!/usr/bin/python3
"""
This module defines the BaseModel class, a base class for all models
in the application, providing common attributes and methods.
"""
import uuid
from datetime import datetime
import models


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
        models.storage.save()
    
    def to_dict(self):
        """Returns a dictionary containing
        all keys/values of the instance's __dict__."""
        new_dictionary = self.__dict__.copy()
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['updated_at'] = self.updated_at.isoformat()
        new_dictionary['created_at'] = self.created_at.isoformat()
        return (new_dictionary)
