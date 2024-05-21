#!/usr/bin/python3
""" Defining class HBNBCommand. """
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
    """
    Command interpreter for the HBNB project.
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """
        Overrides the default behavior to do nothing on empty input line.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program (Ctrl+D).

        Usage: EOF
        """
        return True

    def do_help(self, arg):
        """
        Help command to display information about available commands.

        Usage: help [command]
        """
        super().do_help(arg)

    def do_create(self, arg):
        """
        Create a new instance of a class, save it, and print the id.

        Usage: create <class_name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show details of a specified object.

        Usage: show <class_name> <instance_id>
        """
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
        all_objects = storage.all()
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete a specified object.

        Usage: destroy <class_name> <instance_id>
        """
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
        all_objects = storage.all()
        if key in all_objects:
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        List all objects or objects of a specified class.

        Usage: all [class_name]
        """
        args = arg.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        if args:
            class_name = args[0]
            objects = [str(obj) for key, obj in all_objects.items()
                       if key.startswith(class_name)]
        else:
            objects = [str(obj) for obj in all_objects.values()]
        print(objects)

    def do_update(self, arg):
        """
        Update an attribute of a specified object.

        Usage: update <class_name> <instance_id>
               <attribute_name> <attribute_value>
        """
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
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()
        if key in all_objects:
            obj = all_objects[key]
            try:
                attr_value = eval(attr_value)
            except (NameError, SyntaxError):
                pass
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
