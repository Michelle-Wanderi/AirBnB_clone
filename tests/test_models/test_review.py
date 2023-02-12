#!/usr/bin/python3
"""
Unit test for the review module
"""

from models.review import Review
import unittest


class TestReviewModel(unittest.TestCase):
    """Test suites for the Review class"""

    @classmethod
    def setUp(self):
        """Setup resources to be used in the tests"""
        self.review = Review()

    @classmethod
    def tearDown(self):
        """Tear down resources after running the tests"""
        del self.review

    def test_attributes_review(self):
        """Test for the presence of all attributes"""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))

    def test_type_attributes(self):
        """Test for the types of attributes"""
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)

    def test_class_documentation(self):
        """Test 'Review' class Documentation"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsInstance(Review.__doc__, str)

    def test_module_documentation(self):
        """Test documentation for the 'review' module"""
        self.assertIsNotNone(Review.__module__.__doc__)

    def test_self_docuentation(self):
        """Test documentation for this class/module"""
        self.assertIsNotNone(self.__class__.__doc__)
        self.assertIsInstance(self.__module__.__doc__, str)


if __name__ == "__main__":
    unittest.main()
