#!/usr/bin/python3
import unittest
import pycodestyle
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests the amenity class"""

    def setUp(self):
        """Set up for each test"""
        self.amenity = Amenity()

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style violations in models/amenity.py")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style violations in test_amenity.py")

    def test_checking_for_docstring_Amenity(self):
        """Checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_is_subclass_Amenity(self):
        """Test if Amenity is subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_amenity_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_update_attributes(self):
        """Test Amenity attribute updates"""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

    def test_amenity_attribute_type(self):
        """Test Amenity attribute types"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_default_values(self):
        """Test Amenity default values"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_save_method(self):
        """Test Amenity save method"""
        amenity = Amenity()
        previous_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, previous_updated_at)

    def test_amenity_to_dict_method(self):
        """Test Amenity to_dict method"""
        amenity = Amenity()
        amenity.name = "Gym"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Gym")
        self.assertEqual(amenity_dict['__class__'], "Amenity")


if __name__ == '__main__':
    unittest.main()
