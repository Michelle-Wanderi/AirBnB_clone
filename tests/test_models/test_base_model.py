#!/usr/bin/python3
"""
Tests Suites for the base model
"""

import models as md
import os
import json
import unittest


class TestBaseModel(unittest.TestCase):
    """Unit test class for the BaseModel class Objects"""

    def setUp(self):
        """Instantiate objects to be used in the test"""
        self.base1 = md.base_model.BaseModel()
        self.base2 = md.base_model.BaseModel()

    def tearDown(self):
        """Delete the objects created during the tests"""
        del self.base1
        del self.base2

    def test_unique_id(self):
        """Test to ascertain that no two objects have the same ID"""
        self.assertNotEqual(self.base1.id, self.base2.id)

    def test_kwargs_init(self):
        """Test Kwargs initialization"""
        kwargs = {
             "__class__": "BaseModel",
             "created_at": "2023-02-10T19:52:36.252305",
             "id": "83b3c8a8-b72b-1337-9d80-c52b2e090f04",
             "updated_at": "2022-02-11T19:52:36.252312"
            }
        new_base = md.base_model.BaseModel(**kwargs)
        self.assertEqual(new_base.created_at.isoformat(), kwargs['created_at'])
        self.assertEqual(new_base.id, kwargs['id'])
        self.assertEqual(new_base.updated_at.isoformat(), kwargs['updated_at'])
        self.assertEqual(new_base.__class__.__name__, kwargs["__class__"])

    def test_str_method(self):
        """Test the __str__ method of the BaseModel class"""
        base1_string = self.base1.__str__()
        self.assertTrue(type(base1_string), str)
        self.assertIsNotNone(base1_string)
        self.assertIn("id", base1_string)
        self.assertIn("created_at", base1_string)
        self.assertIn("updated_at", base1_string)
        self.assertIn("[BaseModel]", base1_string)

    def test_to_dict_method(self):
        """Test return value of the the to_dict method of BaseModel class"""
        test_dictionary = {k: v for k, v in self.base1.__dict__.items()}
        test_dictionary["created_at"] = self.base1.created_at.isoformat()
        test_dictionary["updated_at"] = self.base1.updated_at.isoformat()
        test_dictionary["__class__"] = self.base1.__class__.__name__
        self.assertEqual(test_dictionary, self.base1.to_dict())


class TestBaseModelSave(unittest.TestCase):
    """Test the save and reload methods of the BaseModel class"""

    def setUp(self):
        """Create the resources needed to run the unittest
        i) If a file  'file.json' exists, rename it, so its content is not
        interefered with by the tests
        ii) Create Objects of the BaseModel class
        """
        if os.path.isfile("file.json"):
            os.rename("file.json", "tempfile")
        self.base_1 = md.base_model.BaseModel()
        self.base_2 = md.base_model.BaseModel()

    def tearDown(self):
        """Tear down the resources setup during the tests, after running them
        i) Delete the 'file.json' that was created
        ii) If 'file.json' was renamed to 'tmpfile' is the setup,
        Rename it back to 'file.json'
        iii) Delete the objects created during setUp
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("tempfile"):
            os.rename("tempfile", "file.json")
        del self.base_1
        del self.base_2

    def test_update_at(self):
        """Test for the update_at attribute on calling the save method"""
        time_a = self.base_1.updated_at
        self.base_1.save()
        self.assertNotEqual(time_a, self.base_1.updated_at)
        self.assertLess(time_a, self.base_1.updated_at)

    def test_object_saved(self):
        """Test to affirm an object is saved on calling the save method"""
        self.base_2.save()
        if os.path.isfile("file.json"):
            with open("file.json", "r", encoding="UTF-8") as jsonfile:
                json_attributes = json.load(jsonfile)
            base_2_id = "BaseModel." + self.base_2.id
            value = json_attributes[base_2_id]
            self.assertEqual(value, self.base_2.to_dict())

        else:
            pass


class TestDocumentation(unittest.TestCase):
    """Documentation Tests"""

    @classmethod
    def setUp(self):
        """Setup objects"""
        self.new_base = md.base_model.BaseModel()

    @classmethod
    def tearDown(self):
        """Tear down resources"""
        del self.new_base

    def test_class_documentation(self):
        """Test class documentation"""
        self.assertIsNotNone(md.base_model.BaseModel.__doc__)

    def test_module_documentation(self):
        """Test documentation for the 'base_model' module"""
        module = self.new_base.__module__
        self.assertIsNotNone(module.__doc__)

    def test_self_docuentation(self):
        """Tests for this documentation for classes in this module"""
        self.assertIsNotNone(self.__class__.__doc__)
        self.assertIsNotNone(TestBaseModelSave.__doc__)
        self.assertIsNotNone(TestBaseModel.__doc__)


if __name__ == "__main__":
    unittest.main()
