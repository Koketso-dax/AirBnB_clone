#!/usr/bin/python3
import cmd
import json
import uuid
from models.base_model import BaseModel
from models import storage
""" Main console program entry point """


class HBNBCommand(cmd.Cmd):
    """ Class to define & implement all supported commands """
    prompt = "(hbnb)"
    file_path = "file.json"

    def do_quit(self, arg):
        """ Quit cmd to close shell """
        return True

    def do_EOF(self, arg):
        """ Handles EOF cmd to close shell """
        return True

    def do_emptyline(self):
        """ Does absolutely nothing """
        pass

    def do_create(self, arg):
        """ Create new instance of Object type specified """
        if not arg:
            print("** class name missing **")
        elif arg not in storage.class_names():
            print("** class doesn't exist **")
        else:
            new_instance = storage.class_names()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ Print the str representation of an instance gived its id. """
        if not arg:
            print("** class name missing **")
        else:
            words = arg.split()
            if words[0] not in storage.class_names():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                instance_dict = storage.all()
                print(instance_dict.get(key, "** no instance found **"))
    
    def do_all(self, arg):
        """ Print str representation of all current entries """
        words = arg.split()
        if words and words[0] not in storage.class_names():
            print("** class doesn't exist **")
        else:
            instance_list = [str(obj) for obj in storage.all().values()
                    if not in words or type(obj).__name == words[0]]
            print(instance_list)

    def do_destroy(self, arg):
        """ Deletes an instance based on the classname and id. """
        if not arg:
            print("** class name missing **")
        else:
            words = arg.split()
            class_name = words[0]
            if class_name not in storage.class_names():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                instance_id = words[1]
                key = f"{class_name}.{instance_id}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
    
    def do_count(self, arg):
        """ Counts current number of instances of a class """
        words = arg.split()

        if not words or not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.class_names():
            print("** class doesn't exist **")
        else:

if __name__ == '__main__':
    hbnb_console = HBNBCommand()
    hbnb_console.cmdloop()
