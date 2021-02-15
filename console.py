#!/usr/bin/python3
"""
[HBNBCommand class
The cmd module is mainly useful for building custom shells
that let a user work with a program interactively.
console.py is the entry point command line interpreter for Airbhb project
"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    [HBNBCommand class]
    entry point of the command interpreter

    Returns:
        [bool]: True or False
    """
    prompt = "(hbnb) "

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
        args = args.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in self.HBNBCommand:
            print("** class doesn't exist **")

        else:
            instance = globals()[args]
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """
        [Show] string representation of an id nstance
        """
        args = args.split()
        _all = storage.all()
        if args is None or args == "":
            print("** class name missing **")

        elif args[0] not in HBNBCommand():
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
        _args = args.split()
        _all = storage.all()
        if not _args:
            print("** class name missing **")

        elif _args[0] not in HBNBCommand():
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        [all] prints all string representation
        """
        args = args.split()
        _list = []
        if args and args[0] not in self.HBNBCommand:
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

        elif args.split()[0] not in HBNBCommand.keys():
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
            setattr(_all[key], args.split()[2], args.split()[3])
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
