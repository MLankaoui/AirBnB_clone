#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class extends cmd.Cmd to create
    a command-line interface for a program.

    Attributes:
        prompt (str): The command prompt displayed to the user.

    Methods:
        __init__: Initializes the command-line interface.
        do_help: Provides help information about available commands.
        do_quit: Quits the program.
        do_EOF: Handles End-of-File condition.
        do_: Handles an empty line input.
    """

    def __init__(self):
        """
        Initializes the HBNBCommand instance.
        Sets the prompt for the command-line interface.
        """
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '
        self.file_storage = FileStorage()
        self.file_storage.reload()


    def do_quit(self, args):
        """Quits the program"""
        return True

    def do_EOF(self, args):
        """Handles End-of-File condition (Ctrl+D).
        Exits the program gracefully."""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        self.file_storage.new(new_instance)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        try:
            with open("file.json", "r") as file:
                instances = json.load(file)
                key = "{}.{}".format(class_name, instance_id)
                if key in instances:
                    instance = instances[key]
                    # Convert created_at and updated_at to datetime objects
                    instance["created_at"] = datetime.datetime.strptime(instance["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    instance["updated_at"] = datetime.datetime.strptime(instance["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    # Remove __class__ key
                    del instance['__class__']
                    formatted_instance = "[{}] ({}) {}".format(
                        class_name, instance_id, instance)
                    print(formatted_instance)
                else:
                    print("** no instance found **")
        except FileNotFoundError:
            print("** no instance found **")




    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        try:
            with open("file.json", "r") as file:
                instances = json.load(file)
                key = "{}.{}".format(class_name, instance_id)
                if key in instances:
                    del instances[key]
                    with open("file.json", "w") as outfile:
                        json.dump(instances, outfile)
                else:
                    print("** no instance found **")
        except FileNotFoundError:
            print("** no instance found **")

    def do_all(self, arg):
        args = arg.split()
        if args and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        try:
            with open("file.json", "r") as file:
                instances = json.load(file)
                if args:
                    class_name = args[0]
                    filtered_instances = {
                        k: v for k, v in instances.items() if k.split(".")[0] == class_name
                    }
                    formatted_instances = []
                    for key, instance in filtered_instances.items():
                        attributes = ", ".join(["'{}': {}".format(k, repr(v)) for k, v in instance.items() if k != "__class__"])
                        formatted_instance = "[{}] ({}) ({})".format(
                            instance["__class__"], instance["id"],
                            attributes
                        )
                        formatted_instances.append(formatted_instance)
                    print("\n".join(formatted_instances))
                else:
                    formatted_instances = []
                    for key, instance in instances.items():
                        attributes = ", ".join(["'{}': {}".format(k, repr(v)) for k, v in instance.items() if k != "__class__"])
                        formatted_instance = "[{}] ({}) ({})".format(
                            instance["__class__"], instance["id"],
                            attributes
                        )
                        formatted_instances.append(formatted_instance)
                    print("\n\n".join(formatted_instances))
        except FileNotFoundError:
            print("[]")


    def do_update(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            print("** value missing **")
            return

        try:
            with open("file.json", "r") as file:
                instances = json.load(file)
                key = "{}.{}".format(class_name, instance_id)
                if key in instances:
                    instance = instances[key]
                    instance[attribute_name] = attribute_value
                    with open("file.json", "w") as outfile:
                        json.dump(instances, outfile)
                else:
                    print("** no instance found **")
        except FileNotFoundError:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
