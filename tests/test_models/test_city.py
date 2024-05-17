#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel
import pycodestyle


class TestCity(unittest.TestCase):
    """Tests the city class"""

    def setUp(self):
        """Set up for each test"""
        self.city = City()

    def test_pep8_conformance(self):
        """Test that models/city.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        pep8style.options.max_line_length = 120
        result = pep8style.check_files(['models/city.py'])
        error_message = "Found PEP8 style violations:\n{}".format(
            '\n'.join(result.messages))
        self.assertEqual(result.total_errors, 0, error_message)

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings)")

    def test_city_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_is_subclass_City(self):
        """test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_city_update_attributes(self):
        """Test City attribute updates"""
        city = City()
        city.state_id = "NY"
        city.name = "New York"
        self.assertEqual(city.state_id, "NY")
        self.assertEqual(city.name, "New York")

    def test_checking_for_docstring_City(self):
        """checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_city_to_dict_method(self):
        """Test City to_dict method"""
        city = City(state_id="NV", name="Las Vegas")
        city_dict = city.to_dict()
        self.assertEqual(city_dict['state_id'], "NV")
        self.assertEqual(city_dict['name'], "Las Vegas")
        self.assertEqual(city_dict['__class__'], "City")


if __name__ == '__main__':
    unittest.main()
