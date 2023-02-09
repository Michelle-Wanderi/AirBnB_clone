#!/usr/bin/python3
#To see it in action cd into the airbnb console directory then run python commandline.py or python3 commandline.py in your terminal 

import cmd
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    """Contains functionality of the console"""
    intro = 'Welcome to the interpreter! Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    
    def do_hello(self, line):
        """Says hello to the user"""
        print("Hello!")


    def do_create(self, line):
        """Creates a new object"""
        print("Create a new object")
        if len(line)==0:
            print("**PLease write the name of the class")
        elif line not in HBNBCommand.classes:
            print("Class does not exist")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)


    def do_update(self, line):
        """Updates attributes of an object"""
        print("Update attributes of an object")


    def do_destroy(self, line):
        """Destroys an object"""
        print("Destroy an object")
        args = parse(line)


    def do_operations(self,args):
        """Do operations on objects"""
        print("Choose operation to use on object")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        

    def do_quit(self, args):
        """Quits the interpreter"""
        print("Goodbye!")
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    