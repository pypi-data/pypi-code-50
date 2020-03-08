#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import unittest
from GLXCurses import Button
from GLXCurses.Utils import glxc_type


# Unittest
class TestButton(unittest.TestCase):

    # Test
    def test_glxc_type(self):
        """Test Entry type"""
        button = Button()
        self.assertTrue(glxc_type(button))

    def test_get_preferred_width(self):
        button = Button()
        button.set_text('Hello.42')
        self.assertEqual(12, button.preferred_width)



