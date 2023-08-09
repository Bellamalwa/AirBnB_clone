#!/usr/bin/env python3
"""This is the console for AirBnB"""

import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User 
from models.state import State
from models.city import City
from models.amenity import Place
from models.review import Review
from shlex import split

class HBNBCommand(cmd.Cmd):
    """This class is the entry point of the command intepreter"""
    prompt = "(hbnb)"
    all_classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def emptyline(self):
        """Ignores empty spaces"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
