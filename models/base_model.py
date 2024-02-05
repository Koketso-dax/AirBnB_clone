#!/usr/bin/python3
import uuid
from datetime import datetime

""" Base class model module """

class BaseModel:

    """ BaseModel implementation """
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        od = self__dict__.copy()
        od['__class__'] = self.__class__.__name__
        od['created_at'] = self.created_at.isoformat()
        od['updated_at'] = self.updated_at.isoformat()
        return od

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
