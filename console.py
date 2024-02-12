#!/usr/bin/python3
""" Main console program entry point """
import cmd
import json
import sys
import uuid
import re
from models import *
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class to define & implement all supported commands """
    prompt = "(hbnb)"
    file_path = "file.json"

    def default(self, arg):
        """ Default Idle status """
        self._precmd(arg)

    def _precmd(self, arg):
        """ Intercepts commands to test for class.syntax() """

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not match:
            return arg

        classname, method, args = match.groups()
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid, attr_or_dict = match_uid_and_args.groups()
        else:
            uid, attr_or_dict = args, False
            attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search('^(?:"([^"]*)")?(?:, (.*))?$',
                                             attr_or_dict)
            if match_attr_and_value:
                a = (match_attr_and_value.group(1) or "") + " "
                b = (match_attr_and_value.group(2) or "")
                attr_and_value = a + b
            command = f"{method} {classname} {uid} {attr_and_value}"
            self.onecmd(command)
            return command

    def do_quit(self, arg):
        """ Quit cmd to close shell """
        return True

    def do_help(self, arg):
        """ View Commands and documentation """
        cmd.Cmd.do_help(self, arg)

    def do_EOF(self, arg):
        """ Handles EOF cmd to close shell """
        return True

    def emptyline(self):
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
        if not arg:
            instance_strings = [str(obj) for obj in storage.all().values()]
            print(instance_strings)
        else:
            words = arg.split()
            class_name = words[0]
            if class_name not in storage.class_names():
                print("** class doesn't exist **")
            else:
                instance_list = [str(obj) for obj in storage.all().values()
                                 if type(obj).__name__ == class_name]
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
            class_name = words[0]
            matches = [key for key in storage.all()
                       if key.startswith(f"{class_name}.")]
            print(len(matches))

    def do_update(self, arg):
        """ Updates one or more fields in an instance """
        if not arg:
            print("** class name missing **")
            return
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s"([^"]*)")?)?)?$'
        match = re.search(rex, arg)
        if not match:
            print("** class name missing **")
            return
        classname, uid, attribute, value = match.groups()

        if classname not in storage.class_names():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id doesn't exist **")
        else:
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = float if '.' in value else int
                if re.search('^".*"$', value):
                    value = value.replace('"', '')
                else:
                    cast(value)
                attributes = storage.attributes().get(classname, {})
                if attribute in attributes:
                    value = attributes[attribute](value)
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def postcmd(self, stop, arg):
        """ Print new line after command exercution in non-interactive mode """
        if not sys.stdin.isatty():
            print()
        return stop


if __name__ == '__main__':
    """ Will run an instance of the console """
    hbnb_console = HBNBCommand()
    hbnb_console.cmdloop()
