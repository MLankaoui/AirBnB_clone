#!/usr/bin/python3
import uuid
from datetime import datetime
"""a script that creates a class base_model"""


class BaseModel:
    """
    A base class for other classes to inherit from.

    Attributes:
        id (str): A unique identifier generated using UUID.
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.
    """

    def __init__(self):
        """
        Initializes a BaseModel instance with a unique ID
        and creation/update timestamps.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) ({})".format(
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
