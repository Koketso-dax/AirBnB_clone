#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
""" Basemodel module """


class BaseModel:
    """ BaseModel Class implementation.
    This class will define all common attributes & methods for all sub classes
    in the AirBnB Project.

    Args:
         args (list): positional arguments
         kwargs (dict): Keyword value arguments

    Attributes:
               id (str): Instance Id
               created_at (str): Time of object instantiation
               updated_at (str): Most recent modification time.
    Methods:
            __str__(): Returns str representation of Model.
            save(): Saves current model state to file.
            to_dict(): dictionary representation of a model.
    Returns:
            obj: Object instance of BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """ Initialization

        Args:
            args (list): positional args.
            kwargs (dict): key value args
        """
        if kwargs:
            t_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, t_format)
                setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs['created_at'], t_format)
            self.updated_at = datetime.strptime(kwargs['updated_at'], t_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        " string format """
        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ Save Function update time """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Dictionary view using key / value pairs """
        copy_dict = self.__dict__.copy()
        copy_dict['__class__'] = type(self).__name__
        copy_dict['created_at'] = self.created_at.isoformat()
        copy_dict['updated_at'] = self.updated_at.isoformat()
        return copy_dict
