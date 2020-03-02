#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved


import GLXCurses
import unittest


# Unittest
class TestBuildable(unittest.TestCase):

    # Test
    def test_Buildable_set_name(self):
        """Test Buildable.set_name()"""
        vseparator = GLXCurses.VSeparator()
        buildable = GLXCurses.Buildable()
        buildable.set_name(buildable=vseparator, name="Hello")
        self.assertEqual(vseparator.name, "Hello")

        # Buildable is not a GLXC.Editable
        self.assertRaises(
            TypeError,
            buildable.set_name,
            buildable=None,
            name=None
        )
        self.assertRaises(
            TypeError,
            buildable.set_name,
            buildable=str("Hello"),
            name="Hello"
        )
        # Is not a Buildable instance
        self.assertRaises(
            TypeError,
            buildable.set_name,
            buildable=GLXCurses.Application(),
            name=None
        )
        # name is not a str
        self.assertRaises(
            TypeError,
            buildable.set_name,
            buildable=vseparator,
            name=int(42)
        )

    def test_Buildable_get_name(self):
        """Test Buildable.get_name()"""
        vseparator = GLXCurses.VSeparator()
        buildable = GLXCurses.Buildable()
        buildable.set_name(buildable=vseparator, name="Hello")
        self.assertEqual(buildable.get_name(buildable=vseparator), "Hello")

        # Buildable is not a GLXC.Editable
        self.assertRaises(
            TypeError,
            buildable.get_name,
            buildable=None,
        )
        self.assertRaises(
            TypeError,
            buildable.get_name,
            buildable=str("Hello"),
        )
        # Is not a Buildable instance
        self.assertRaises(
            TypeError,
            buildable.get_name,
            buildable=GLXCurses.Application(),
        )
