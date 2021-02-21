#!/usr/bin/python3
"""
[HBNBCommand class
The cmd module is mainly useful for building custom shells
that let a user work with a program interactively.
console.py is the entry point command line interpreter for Airbhb project
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
    [HBNBCommand class]
    entry point of the command interpreter

    Returns:
        [bool]: True or False
    """
    prompt = "(hbnb) "
    airbnb_classes = {"BaseModel": BaseModel,
                      "User": User,
                      "State": State,
                      "City": City,
                      "Amenity": Amenity,
                      "Place": Place,
                      "Review": Review}

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        [empty line]
        method called when an empty line is entered in
        response to the prompt.
        onecmd help us to implement an empty line + ENTER
        shouldnt execute anything
        """
        pass

    def do_create(self, args):
        """
        [Create] creates a new instance of BAseModel, saves it
        (to the JSON file) and prints the id.

        Args:
            arg(str): given class in the command line interpreter
        if the class name is missing, print ** class name missing **
        if the class name doesnt exist, print ** class doesn't exist **
        """
        if not args:
            print("** class name missing **")

        elif args not in self.airbnb_classes:
            print("** class doesn't exist **")

        else:
            instance = globals()[args]
            new = instance()
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        [Show] string representation of an id nstance
        """
        args = args.split()
        _all = storage.all()
        if args is None or args == "":
            print("** class name missing **")

        elif args[0] not in self.airbnb_classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args[0], args[1]) not in _all:
            print("** no instance found **")

        else:
            print(_all["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """
        [Destroy] is a command to destroy an instance
        """
        arg = args.split()
        _all = storage.all()
        if not arg:
            print("** class name missing **")

        elif arg[0] not in self.airbnb_classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            del _all["{}.{}".format(args.split()[0], args.split()[1])]
            storage.save()

    def do_all(self, args):
        """
        [all] prints all string representation
        all instances based or not on the class name
        """
        args = args.split()
        _list = []
        if args and args[0] not in self.airbnb_classes.keys():
            print("** class doesn't exist **")

        elif not args:
            for obj in storage.all().values():
                _list.append(str(obj))

        else:
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    _list.append(str(obj))
        if len(_list):
            print(_list)

    def do_update(self, args):
        """
        [Update] is command to update attributes
        """
        _all = storage.all()
        if len(args.split()) == 0:
            print("** class name missing **")

        elif args not in self.airbnb_classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        elif len(args.split()) == 2:
            print("** attribute name missing **")

        elif len(args.split()) == 3:
            print("** value missing **")

        else:
            key = "{}.{}".format(args.split()[0], args.split()[1])
            obj_update = args.split()[2]
            value = args.split()[3]
            setattr(storage.all()[key], obj_update, value)
            storage.save()

    def default(self, line):
        """
        [default method]

        Args:
        line ([str]): user's input
        Returns:
        [method]: returns the method needed or error
        """
        _list = (line.replace("(", ".").replace(",", ".").replace(" ", "")
                 [:-1].split("."))
        if len(_list) > 1:
            if _list[1] == "all":
                return self.do_all(_list[0])

            elif _list[1] == "show":
                return self.do_show(_list[0] + " " + _list[2])

            elif _list[1] == "destroy":
                return self.do_destroy(_list[0] + " " + _list[2])

            elif _list[1] == "update":
                return self.do_update(_list[0] + " " + _list[2] + _list[3] +
                                      " " + _list[4])

            elif _list[1] == "count":
                return self.do_count(_list[0])

        else:
            print("*** Unknown syntax: {}".format(line))
            return False

    def do_count(self, args):
        """
        retrieve the number of instance of a class: <class name>.count
        """
        counter = 0
        instances = storage.all()
        for key, obj in instances.items():
            if args in obj.__str__():
                counter += 1
        print(counter)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
