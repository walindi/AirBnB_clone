#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import re
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of 'BaseModel',
        saves (it to the JSON file) and prints the id"""

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
            return

        class_name = match.group(1)
        if c_name not in storage.dictionary():
            print("** class doesn't exist **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
