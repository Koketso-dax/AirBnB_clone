#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

""" Base class model module """
class BaseModel:

    """ BaseModel Class implementation """
    
    def __init__(self, *args, **kwargs):
        """ Initialization """
        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, time_format)
                setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs['created_at'], time_format)
            self.updated_at = datetime.strptime(kwargs['updated_at'], time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        " string format """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Save Function update time """
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """ Dictionary view using key / value pairs """
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = self.__class__.__name__
        copy_dict['created_at'] = self.created_at.isoformat()
        copy_dict['updated_at'] = self.updated_at.isoformat()
        return copy_dict
