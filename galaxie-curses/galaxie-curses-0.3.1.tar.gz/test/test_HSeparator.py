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
        GLXCurses.Application().refresh()

    def test_set_get_position_type(self):
        """Test HSeparator.set_position_type() and HSeparator.get_position_type()"""
        hline = GLXCurses.HSeparator()

        hline.set_position_type('CENTER')
        self.assertEqual(hline.get_position_type(), GLXCurses.GLXC.POS_CENTER)

        hline.set_position_type('TOP')
        self.assertEqual(hline.get_position_type(), GLXCurses.GLXC.POS_TOP)

        hline.set_position_type('BOTTOM')
        self.assertEqual(hline.get_position_type(), GLXCurses.GLXC.POS_BOTTOM)

        hline.set_position_type(GLXCurses.GLXC.POS_CENTER)
        self.assertEqual(hline.get_position_type(), 'CENTER')

        hline.set_position_type(GLXCurses.GLXC.POS_TOP)
        self.assertEqual(hline.get_position_type(), 'TOP')

        hline.set_position_type(GLXCurses.GLXC.POS_BOTTOM)
        self.assertEqual(hline.get_position_type(), 'BOTTOM')

        self.assertRaises(TypeError, hline.set_position_type, 'HELLO')

    # Internal
    def test__check_position_type(self):
        """Test VSeparator._check_position_type()"""
        hline = GLXCurses.HSeparator()

        # glxc.POS_CENTER -> (self.get_height() / 2) - self.get_preferred_height()
        hline._position_type = GLXCurses.GLXC.POS_CENTER
        hline.height = 124
        hline.preferred_height = 20
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 42)

        hline.height = None
        hline.preferred_height = None
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = -1
        hline.preferred_height = -1
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = 0
        hline.preferred_height = -0
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = 1
        hline.preferred_height = -0
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = -1000
        hline.preferred_height = -100
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        # glxc.POS_TOP -> self._set_hseperator_y(0)
        hline._position_type = GLXCurses.GLXC.POS_TOP
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = None
        hline.preferred_height = None
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = -1
        hline.preferred_height = -1
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = 0
        hline.preferred_height = -0
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = -1000
        hline.preferred_height = -100
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        # glxc.POS_BOTTOM -> self.get_height() - self.get_preferred_height()
        hline._position_type = GLXCurses.GLXC.POS_BOTTOM
        hline.height = 62
        hline.preferred_height = 20
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 42)

        hline.height = None
        hline.preferred_height = None
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = -1
        hline.preferred_height = -1
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = 0
        hline.preferred_height = -0
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

        hline.height = -1000
        hline.preferred_height = -100
        hline._check_position_type()
        self.assertEqual(hline._y_offset, 0)

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

    def test_set_get_hseperator_x(self):
        """Test HSeparator._set_hseperator_x() and HSeparator._get_hseperator_x()"""
        hline = GLXCurses.HSeparator()
        # call set_decorated() with 0 as argument
        hline._set_x_offset(0)
        # verify we go back 0
        self.assertEqual(hline._get_x_offset(), 0)
        # call set_decorated() with 0 as argument
        hline._set_x_offset(42)
        # verify we go back 0
        self.assertEqual(hline._get_x_offset(), 42)
        # test raise TypeError
        self.assertRaises(TypeError, hline._set_x_offset, 'Galaxie')

    def test_set_get_hseperator_y(self):
        """Test HSeparator._set_hseperator_y() and HSeparator._get_hseperator_y()"""
        hline = GLXCurses.HSeparator()
        # call set_decorated() with 0 as argument
        hline._set_y_offset(0)
        # verify we go back 0
        self.assertEqual(hline._get_y_offset(), 0)
        # call set_decorated() with 0 as argument
        hline._set_y_offset(42)
        # verify we go back 0
        self.assertEqual(hline._get_y_offset(), 42)
        # test raise TypeError
        self.assertRaises(TypeError, hline._set_y_offset, 'Galaxie')
