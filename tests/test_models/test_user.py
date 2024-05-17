#!/usr/bin/python3
import unittest
import pycodestyle
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests the user class"""

    def setUp(self):
        """Set up for each test"""
        self.user = User()

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style violations in models/user.py")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style violations in tests/test_user.py")

    def test_checking_for_docstring_User(self):
        """Checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_is_subclass_User(self):
        """Test if User is subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_user_attributes(self):
        """Test User attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_update_attributes(self):
        """Test User attribute updates"""
        user = User()
        user.email = "example@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "example@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_attribute_type(self):
        """Test User attribute types"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_default_values(self):
        """Test User default values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_save_method(self):
        """Test User save method"""
        user = User()
        previous_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, previous_updated_at)

    def test_user_to_dict_method(self):
        """Test User to_dict method"""
        user = User()
        user.email = "example@example.com"
        user.first_name = "John"
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "example@example.com")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['__class__'], "User")


if __name__ == '__main__':
    unittest.main()
