#!/usr/bin/python3

"""
Unittests Tests for the place module
"""

from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Test Suites for the Place class"""

    @classmethod
    def setUp(self) -> None:
        """Setup resources for running tests"""
        self.place = Place()

    @classmethod
    def tearDown(self) -> None:
        """Clean up resources after running the tests"""
        del self.place

    def tests_attributes(self) -> None:
        """Test for presece of attributes"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertIsNotNone(self.place.description)
        self.assertIsNotNone(self.place.number_rooms)
        self.assertIsNotNone(self.place.number_bathrooms)
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_attributes_types(self):
        """Test the types of attributes"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_class_documentation(self):
        """Test the for class documentation"""
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(self.__class__.__doc__)

    def test_module_documentation(self):
        """Test for module documentation"""
        self.assertIsNotNone(Place.__module__.__doc__)
        self.assertIsNotNone(self.__module__.__doc__)


if __name__ == "__main__":
    unittest.main()
