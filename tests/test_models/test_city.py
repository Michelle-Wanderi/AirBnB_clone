#!/usr/bin/python3
"""
Unittest for the city module
"""

from models.city import City
import unittest


class TestCityModel(unittest.TestCase):
    """
    Test Suites for the City class
    """
    def setUp(self):
        """setup resources to be used in the tests"""
        self.city = City()

    def tearDown(self):
        """Tear down resources setup during tests"""
        del self.city

    def test_attributes_city(self):
        """Afirm that the object has expected attrs"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_attributes_types(self):
        """Afirm that the types of the objects are strings"""
        self.assertTrue(isinstance(self.city.name, str))
        self.assertTrue(isinstance(self.city.state_id, str))

    def test_str_method(self):
        """Test the __str__ method of the object"""
        self.assertIn("[City]", self.city.__str__())

    def test_to_dict_method(self):
        """Test the to_dict method of the parent class"""
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertEqual(city_dict["__class__"], "City")

    def test_class_documentation(self):
        """Test documentation for the 'City' class"""
        self.assertIsNotNone(City.__doc__)

    def test_module_documentation(self):
        """Test documentation for the 'city' module"""
        self.assertIsNotNone(City.__module__.__doc__)

    def test_self_docuentation(self):
        """Test documentation for this class/module"""
        self.assertIsNotNone(self.__class__.__doc__)
        self.assertIsNotNone(self.__module__.__doc__)


if __name__ == "__main__":
    unittest.main()
