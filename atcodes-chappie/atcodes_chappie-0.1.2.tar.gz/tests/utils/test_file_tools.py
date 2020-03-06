from unittest import TestCase
import os

from chappie.utils.file_tools import FileTools


class TestFileTools(TestCase):
    """Test Dict Tools"""

    def setUp(self):
        """Some Initial data setup"""
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_tools = FileTools(path + "/resources/test.json")

    def tearDown(self):
        """ """

    def test_file_tools(self):
        """ """
        filename = self.file_tools.generate_unique_filename()

        self.assertTrue(filename, str)
        self.assertTrue(filename[-4:]=="json")
        self.assertFalse(filename=="test.json")

        data = self.file_tools.process_json_file()
        self.assertIsInstance(data, list)
        self.assertTrue(data[0]["data"]=="test")

