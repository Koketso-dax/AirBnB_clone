#!/usr/bin/python
import cmd
""" Main console program entry point """


class HBNBCommand(cmd.Cmd):
    """ Class to define & implement all supported commands """
    prompt = "(hbnb)"

    def _quit(self, arg):
        """ Quit cmd to close shell """
        return True

    def _EOF(self, arg):
        """ Handles EOF cmd to close shell """
        return True

    def _empty_line(self):
        """ Does absolutely nothing """
        pass

if __name__ == '__main__':
    hbnb_console = HBNBCommand()
    hbnb_console.cmdloop()
