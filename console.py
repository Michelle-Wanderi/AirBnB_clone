#To see it in action cd into the airbnb directory then run python commandline.py or python3 commandline.py in your terminal 


#!/usr/bin/python3

import cmd
import sys


class Interpreter(cmd.Cmd):
    """Contains functionality of the console"""
    intro = 'Welcome to the interpreter! Type help or ? to list commands.\n'
    prompt = '(hbnb interpreter) '
    
    def do_hello(self, args):
        """Says hello to the user"""
        print("Hello!")


    def do_create(self, args):
        """Creates a new object"""
        print("Create a new object")

    def do_update(self, args):
        """Updates attributes of an object"""
        print("Update attributes of an object")


    def do_destroy(self, args):
        """Destroys an object"""
        print("Destroy an object")

    def do_operations(self,args):
        """Do operations on objects"""
        print("Choose operation to use on object")

    def do_quit(self, args):
        """Quits the interpreter"""
        print("Goodbye!")
        return True
    

if __name__ == '__main__':
    Interpreter().cmdloop()

    