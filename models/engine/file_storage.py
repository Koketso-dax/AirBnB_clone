#!/usr/bin/python3
import json

""" File Storage Module """
class FileStorage():
    """ File Storage class implementation """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary of objects(__objects) """
        return self.__objects

    def new(self, obj):
        """ Sets private __objects with key in obj <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to JSON file in path """
        serial_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open (self.__file_path, 'w') as file:
            json.dump(serial_obj, file)

    def reload(self):
        """ Deserializes JSON object """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj - globals()[class_name]
                    instance = class_obj(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
