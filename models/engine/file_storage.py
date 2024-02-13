#!/usr/bin/python3
import json
import os
import datetime
""" File Storage Module """


class FileStorage():
    """ File Storage class implementation """
    __file_path = "file.json"
    __objects = {}

    def class_names(self):
        """ Defines and returns dictionary of valid classnames """
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
        s_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(s_obj, file)

    def reload(self):
        """ Deserializes JSON object """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            old_dict = json.load(file)
            old_dict = {key: self.class_names()[value["__class__"]](**value)
                        for key, value in old_dict.items()}
            FileStorage.__objects = old_dict
    
    def attributes(self):
        """ Defines and returns dict of valid attr """
        attributes = {
                "BaseModel":
                {"id": str, "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},

                "User":
                {"email": str, "password": str,
                    "first_name": str, "last_name": str},

                "State":
                {"name": str},

                "City":
                {"state_id": str, "name": str},

                "Amenity":
                {"name": str},

                "Place":
                {"city_id": str, "user_id": str,
                    "name": str, "description": str,
                    "number_rooms": int, "number_bathrooms": int,
                    "max_guest": int, "price_by_night": int,
                    "latitude": float, "longitude": float,
                    "amenity_ids": list},

                "Review":
                {"place_id": str, "user_id": str,
                    "text": str}
                }
        return attributes
