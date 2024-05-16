import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestConsole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        """Resets the storage before each test"""
        storage.all().clear()

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        self.assertTrue(self.console.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        self.assertTrue(self.console.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.console.onecmd("")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        self.console.onecmd("create")
        self.assertIn("** class name missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        self.console.onecmd("create MyModel")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(obj_id) == 36)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        self.console.onecmd("show")
        self.assertIn("** class name missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        self.console.onecmd("show MyModel")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        self.console.onecmd("show BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_no_instance_found(self, mock_stdout):
        self.console.onecmd("show BaseModel 1234")
        self.assertIn("** no instance found **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn("BaseModel", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        self.console.onecmd("destroy")
        self.assertIn("** class name missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_invalid_class(self, mock_stdout):
        self.console.onecmd("destroy MyModel")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_id(self, mock_stdout):
        self.console.onecmd("destroy BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_no_instance_found(self, mock_stdout):
        self.console.onecmd("destroy BaseModel 1234")
        self.assertIn("** no instance found **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"destroy BaseModel {obj_id}")
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn("** no instance found **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_invalid_class(self, mock_stdout):
        self.console.onecmd("all MyModel")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create User")
        self.console.onecmd("create Place")
        self.console.onecmd("all")
        self.assertIn("BaseModel", mock_stdout.getvalue())
        self.assertIn("User", mock_stdout.getvalue())
        self.assertIn("Place", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_class(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create User")
        self.console.onecmd("all BaseModel")
        self.assertIn("BaseModel", mock_stdout.getvalue())
        self.assertNotIn("User", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        self.console.onecmd("update")
        self.assertIn("** class name missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_invalid_class(self, mock_stdout):
        self.console.onecmd("update MyModel")
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_id(self, mock_stdout):
        self.console.onecmd("update BaseModel")
        self.assertIn("** instance id missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_attribute_name(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"update BaseModel {obj_id}")
        self.assertIn("** attribute name missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_value(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"update BaseModel {obj_id} name")
        self.assertIn("** value missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_no_instance_found(self, mock_stdout):
        self.console.onecmd("update BaseModel 1234 name 'test'")
        self.assertIn("** no instance found **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.console.onecmd(f"update BaseModel {obj_id} name 'test'")
        self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn("test", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()