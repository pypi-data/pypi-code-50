#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import unittest
from GLXCurses.Label import Label
from GLXCurses import GLXC


class TestLabel(unittest.TestCase):
    def test_Label_get_justify(self):
        """Test Label.get_justify()"""
        label = Label()
        self.assertEqual(GLXC.JUSTIFY_LEFT, label.get_justify())

        label.justify = GLXC.JUSTIFY_RIGHT
        self.assertEqual(GLXC.JUSTIFY_RIGHT, label.get_justify())

    def test_Label_set_justify(self):
        """Test Label.set_justify()"""
        label = Label()

        self.assertEqual(GLXC.JUSTIFY_LEFT, label.justify)

        for jutify in GLXC.Justification:
            label.set_justify(jutify)
            self.assertEqual(jutify, label.justify)

        self.assertRaises(TypeError, label.set_justify, 'Hello')

    def test_Label_get_line_wrap(self):
        """Test Label.get_line_wrap()"""
        label = Label()
        self.assertEqual(False, label.get_line_wrap())

        label.wrap = True
        self.assertEqual(True, label.get_line_wrap())

    def test_Label_set_line_wrap(self):
        """Test Label.set_line_wrape()"""
        label = Label()
        self.assertEqual(False, label.wrap)

        label.set_line_wrap(True)
        self.assertEqual(True, label.wrap)

        self.assertRaises(TypeError, label.set_line_wrap, 'Hello')

    def test_Label_get_width_chars(self):
        """Test Label.get_width_chars()"""
        label = Label()
        self.assertEqual(-1, label.get_width_chars())

        label.width_chars = 42
        self.assertEqual(42, label.get_width_chars())

    def test_Label_set_width_chars(self):
        """Test Label.set_width_chars()"""
        label = Label()
        self.assertEqual(-1, label.width_chars)

        label.set_width_chars(42)
        self.assertEqual(42, label.width_chars)

        self.assertRaises(TypeError, label.set_width_chars, 'Hello')


if __name__ == '__main__':
    unittest.main()
