#!/usr/bin/python3
"""
Test Suites for the amenity module
"""

from models.amenity import Amenity
import unittest


class TestAmenityModel(unittest.TestCase):
    """
    Test Cases for the Amenity model
    """

    @classmethod
    def setUp(self):
        """setup resources to be used in the test"""
        self.amenity = Amenity()

    @classmethod
    def tearDown(self):
        """Tear down the resources after running the tests"""
        del self.amenity

    def test_attributes(self):
        """Test for attributes of the objects"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attribute_type(self):
        """Assert that the attribute is of the right type"""
        self.assertIsInstance(self.amenity.name, str)

    def test_str_method(self):
        """Test the __str__ method on the object"""
        self.assertIsNotNone(self.amenity.__str__())
        self.assertIn("[Amenity]", self.amenity.__str__())

    def test_to_dict_method(self):
        """Test the to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_class_documentation(self):
        """Test for the 'Amenity' class documentation"""
        self.assertTrue(isinstance(Amenity.__doc__, str))

    def test_module_documentation(self) -> None:
        """Test documentation for the 'amenity' module"""
        self.assertIsNotNone(Amenity.__module__.__doc__)

    def test_self_docuentation(self):
        """Test documentation for this class"""
        self.assertIsNotNone(self.__class__.__doc__)


if __name__ == "__main__":
    unittest.main()
