from unittest import TestCase
import os

from chappie.utils.text_tools import TextTools


class TestFileTools(TestCase):
    """Test Dict Tools"""

    def setUp(self):
        """Some Initial data setup"""
        self.text_tools = TextTools()

    def tearDown(self):
        """ """

    def test_file_tools(self):
        """ """
        text = "Ñjavhb4389343 cjhla92834r*YQ*&Y#R&@ERF4  F73RT8fWx"
        clean_text = self.text_tools.clean_text(text)

        self.assertEqual(clean_text, "ñjavhb4389343cjhla92834ryqyrerf4f73rt8fwx")

