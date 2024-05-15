# models/base_model.py
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('updated_at', 'created_at'):
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

        from models import storage
        storage.new(self)

    def __str__(self):
        return "[{}] ({}) ({})".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        new_dictionary = self.__dict__.copy()
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['updated_at'] = self.updated_at.isoformat()
        new_dictionary['created_at'] = self.created_at.isoformat()
        return new_dictionary
