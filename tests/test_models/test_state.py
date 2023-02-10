#!/usr/bin/python3
from models.state import State
import unittest

"""
Unit tests for the State module
"""


class TestState(unittest.TestCase):
    """Test Suites for the State Class"""

    def setUp(self):
        """Set up objects to be used in the test"""
        self.state = State()

    def tearDown(self):
        """Tear down resources setup during the tests"""
        del self.state

    def test_attributes_state(self):
        """Test attributes for the object"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_attributes_type(self):
        """Afirm attribute types for the object"""
        self.assertIsInstance(self.state.name, str)

    def test_to_dict_method(self):
        """Testing to_dict on the child class"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")

    def test_str_method(self):
        """Test __str__ method of the object"""
        self.assertIn("[State]", str(self.state))


if __name__ == "__main__":
    unittest.main()
