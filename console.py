#!/usr/bin/python3
"""A python script for the console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """commands for hbnb"""
    classes = {"BaseModel": BaseModel,
               "User": User, "Place": Place,
               "State": State, "City": City,
               "Amenity": Amenity, "Review": Review}
    
    intro = "Welcome to Airbnb console. type 'help' for more info."
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handle EOF to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class, save it, and print the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class__nm = args[0]
        if class__nm not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class__nm]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show details of a specified object."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all__objj = storage.all()
        if key in all__objj:
            print(all__objj[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete a specified object."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class__nm = args[0]
        if class__nm not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class__nm, instance_id)
        all__objj = storage.all()
        if key in all__objj:
            del all__objj[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """List all objects or objects of a specified class."""
        args = arg.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        all__objj = storage.all()
        if args:
            class__nm = args[0]
            objects = [str(obj) for key, obj in all__objj.items()
                       if key.startswith(class__nm)]
        else:
            objects = [str(obj) for obj in all__objj.values()]
        print(objects)

    def do_update(self, arg):
        """Update an attribute of a specified object."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class__nm = args[0]
        if class__nm not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr__nm = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_val = args[3]
        key = "{}.{}".format(class__nm, instance_id)
        all__objj = storage.all()
        if key in all__objj:
            obj = all__objj[key]
            try:
                attr_val = eval(attr_val)
            except (NameError, SyntaxError):
                pass
            setattr(obj, attr__nm, attr_val)
            obj.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
