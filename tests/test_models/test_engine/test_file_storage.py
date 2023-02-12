#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest

"""
Test Suites for the file_storage module
FileStorage class and the methods
"""


class TestFileStorage(unittest.TestCase):
    """Unittests for the FileStorage class"""

    def setUp(self):
        """
        Set up resources to be used in the tests
        i) If 'file.json' exists, rename it to 'tempfile'
        ii) Initialize objects
        """
        if os.path.isfile('file.json'):
            os.rename('file.json', 'tempfile')
        self.storage = FileStorage()
        self.base = BaseModel()

    def tearDown(self):
        """
        Tear down resources associated with tests
        i) Rename 'tempfile' back to 'file.json'
        ii) Delete the objects created during the tests
        """
        if os.path.isfile('tempfile'):
            os.rename('tempfile', 'file.json')
        del self.storage
        del self.base

    def test_attributes(self):
        """Test the attributes of objects"""
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "__class__"))
        self.assertEqual(self.base.__class__.__name__, "BaseModel")
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))

    def test_all_method(self):
        """Test the all method"""
        all_objs_dict = self.storage.all()
        base_id = "BaseModel." + self.base.id
        self.assertIsInstance(all_objs_dict, dict)
        self.assertIn(base_id, all_objs_dict)

    def test_reload_method(self):
        """
        Test the reload method
        i) Create a temporaty BaseModel object
        ii) Call save on the object
        iii) call reload on the storge object and verify that the new
        temporaty object exists in the storage object
        iv) Delete temporary object
        """
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))
        temp_base = BaseModel()
        temp_base.save()
        temp_base_id = "BaseModel." + temp_base.id
        self.assertIn(temp_base_id, self.storage.all())
        del temp_base


if __name__ == "__main__":
    unittest.main()
