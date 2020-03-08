#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import unittest
import GLXCurses


# Unittest
class TestHSeparator(unittest.TestCase):
    # Test
    def test_glxc_type(self):
        """Test if VSeparator is GLXCurses Type"""
        hline = GLXCurses.HSeparator()
        self.assertTrue(GLXCurses.glxc_type(hline))

    def test_draw_widget_in_area(self):
        """Test VSeparator.draw_widget_in_area()"""

        win = GLXCurses.Window()
        hline = GLXCurses.HSeparator()

        win.add(hline)

        GLXCurses.Application().add_window(win)
        # Main loop
        # entry.draw_widget_in_area()
        for position in GLXCurses.GLXC.PositionType:
            hline.position_type = position
            GLXCurses.Application().refresh()


    def test_position_type(self):
        hline = GLXCurses.HSeparator()

        hline.position_type = 'CENTER'
        for position in GLXCurses.GLXC.PositionType:
            hline.position_type = position
            self.assertEqual(hline.position_type, position)

        self.assertRaises(TypeError, setattr, hline, 'position_type', 'HELLO')

    # Internal
    def test__check_position_type(self):
        """Test VSeparator._check_position_type()"""
        hline = GLXCurses.HSeparator()

        # glxc.POS_CENTER -> (self.get_height() / 2) - self.get_preferred_height()
        hline.__position_type = GLXCurses.GLXC.POS_CENTER
        hline.height = 124
        hline.preferred_height = 20
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 42)

        hline.height = None
        hline.preferred_height = None
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = -1
        hline.preferred_height = -1
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = 0
        hline.preferred_height = -0
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = 1
        hline.preferred_height = -0
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = -1000
        hline.preferred_height = -100
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        # glxc.POS_TOP -> self._set_hseperator_y(0)
        hline.__position_type = GLXCurses.GLXC.POS_TOP
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = None
        hline.preferred_height = None
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = -1
        hline.preferred_height = -1
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = 0
        hline.preferred_height = -0
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = -1000
        hline.preferred_height = -100
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        # glxc.POS_BOTTOM -> self.get_height() - self.get_preferred_height()
        hline.__position_type = GLXCurses.GLXC.POS_BOTTOM
        hline.height = 62
        hline.preferred_height = 20
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 11)

        hline.height = None
        hline.preferred_height = None
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = -1
        hline.preferred_height = -1
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = 0
        hline.preferred_height = -0
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

        hline.height = -1000
        hline.preferred_height = -100
        hline._check_position_type()
        self.assertEqual(hline.y_offset, 0)

    def test__get_estimated_preferred_width(self):
        """Test VSeparator._get_estimated_preferred_width()"""
        hline = GLXCurses.HSeparator()
        hline.x = 20
        hline.width = 20
        self.assertEqual(hline._get_estimated_preferred_width(), 20)

    def test__get_estimated_preferred_height(self):
        """Test VSeparator._get_estimated_preferred_height()"""
        hline = GLXCurses.HSeparator()
        self.assertEqual(hline._get_estimated_preferred_height(), 1)


