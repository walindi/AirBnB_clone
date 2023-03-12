#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, line):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
