#!/usr/bin/python3
from models.city import City
import unittest

"""
Unittest for the city module
"""


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


if __name__ == "__main__":
    unittest.main()
