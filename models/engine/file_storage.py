#!/usr/bin/python3
import json
import os

""" File Storage Module """
class FileStorage():
    
    """ File Storage class implementation """
    __file_path = "file.json"
    __objects = {}

    def class_names(self):
        """ Defines dictionary of valid cn and safe imports """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {"BaseModel": BaseModel,
                "User": User, "State": State,
                "City": City, "Amenity": Amenity,
                "Place": Place, "Review": Review}

        return class_dict

    def all(self):
        """ Returns the dictionary of objects(__objects) """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets private __objects with key in obj <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to JSON file in path """
        serial_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open (self.__file_path, 'w') as file:
            json.dump(serial_obj, file)

    def reload(self):
        """ Deserializes JSON object """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            old_dict = json.load(file)
            old_dict = {key: self.class_names()[value["__class__"]](**value)
                    for key, value in old_dict.items()}
            FileStorage.__objects = old_dict

