#!/usr/bin/python3
import unittest
import pycodestyle
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests the state class"""

    def setUp(self):
        """Set up for each test"""
        self.state = State()

    def test_pep8_conformance_state(self):
        """Test that models/state.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style violations in models/state.py")

    def test_pep8_conformance_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style violations in test_state.py")

    def test_checking_for_docstring_State(self):
        """checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_is_subclass_State(self):
        """test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_state_update_attributes(self):
        """test state attributes update"""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_attribute_type(self):
        """test state type attributes"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_default_values(self):
        """test state default values"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_save_method(self):
        """test state save"""
        state = State()
        previous_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, previous_updated_at)

    def test_state_to_dict_method(self):
        """test state to_dict"""
        state = State()
        state.name = "Nevada"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "Nevada")
        self.assertEqual(state_dict['__class__'], "State")


if __name__ == '__main__':
    unittest.main()
