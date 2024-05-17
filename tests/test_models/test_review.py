#!/usr/bin/python3
import unittest
import pycodestyle
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests the review class"""

    def setUp(self):
        """Set up for each test"""
        self.review = Review()

    def test_pep8_conformance_review(self):
        """Test that models/review.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style violations in models/review.py")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style violations in test_review.py")

    def test_checking_for_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_is_subclass_Review(self):
        """test if Review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_review_attributes(self):
        """test review attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_update_attributes(self):
        """test review attributes update"""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Nice place!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Nice place!")

    def test_review_attribute_type(self):
        """test review type attribute"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_review_default_values(self):
        """test review default values"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_save_method(self):
        """test review save method"""
        review = Review()
        previous_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, previous_updated_at)

    def test_review_to_dict_method(self):
        """test review to_dict method"""
        review = Review()
        review.text = "Great experience!"
        review_dict = review.to_dict()
        self.assertEqual(review_dict['text'], "Great experience!")
        self.assertEqual(review_dict['__class__'], "Review")


if __name__ == '__main__':
    unittest.main()
