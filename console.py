#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for managing HBNB data.
    """
  
    prompt = "(hbnb) "
    
    def do_quit(self):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self):
        """
        Exit the program cleanly at end of file (EOF).
        """
        return True
  
    def emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
