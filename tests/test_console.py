#!/usr/bin/python3
"""
Unittest for console command interpreter
"""
import unittest
import os
import json
import console
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from io import StringIO
from unittest.mock import patch



"""Test command interpreter outputs"""
def test_emptyline(self):
        """Test no user input"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

def test_create(self):
        """Test cmd output: create"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create User")  # not used
            self.typing.onecmd("create User")  # just need to create instances
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.all()")
            self.assertEqual("[[User]",
                             fake_output.getvalue()[:7])
