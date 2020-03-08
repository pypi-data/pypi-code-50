#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import unittest
import GLXCurses


# Unittest
class TestVSeparator(unittest.TestCase):

    # Test
    def test_glxc_type(self):
        """Test if VSeparator is GLXCurses Type"""
        vline = GLXCurses.VSeparator()
        self.assertTrue(GLXCurses.glxc_type(vline))

    def test_draw_widget_in_area(self):
        """Test VSeparator.draw_widget_in_area()"""

        win = GLXCurses.Window()
        vline = GLXCurses.VSeparator()

        win.add(vline)

        GLXCurses.Application().add_window(win)
        # Main loop
        # entry.draw_widget_in_area()
        GLXCurses.Application().refresh()

    def test_set_get_justify(self):
        """Test VSeparator.set_justify() and VSeparator.get_justify()"""
        vline = GLXCurses.VSeparator()

        vline.set_justify(GLXCurses.GLXC.JUSTIFY_CENTER)
        self.assertEqual(vline.get_justify(), GLXCurses.GLXC.JUSTIFY_CENTER)

        vline.set_justify(GLXCurses.GLXC.JUSTIFY_LEFT)
        self.assertEqual(vline.get_justify(), GLXCurses.GLXC.JUSTIFY_LEFT)

        vline.set_justify(GLXCurses.GLXC.JUSTIFY_RIGHT)
        self.assertEqual(vline.get_justify(), GLXCurses.GLXC.JUSTIFY_RIGHT)

        vline.set_justify(GLXCurses.GLXC.JUSTIFY_FILL)
        self.assertEqual(vline.get_justify(), GLXCurses.GLXC.JUSTIFY_FILL)

        self.assertRaises(TypeError, vline.set_justify, 'HELLO')

    # Internal
    def test__check_justify(self):
        """Test VSeparator._check_justify()"""
        vline = GLXCurses.VSeparator()

        # glxc.JUSTIFY_CENTER -> (self.get_width() / 2) - (self.get_preferred_width() / 2)
        vline._justify = GLXCurses.GLXC.JUSTIFY_CENTER
        vline.width = 124
        vline.preferred_width = 40
        vline._check_justify()
        self.assertEqual(vline._x_offset, 42)

        vline.width = None
        vline.preferred_width = None
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = -1
        vline.preferred_width = -1
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = 0
        vline.preferred_width = -0
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = 1
        vline.preferred_width = -0
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = -1000
        vline.preferred_width = -100
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        # glxc.JUSTIFY_LEFT -> self.get_spacing()
        vline._justify = GLXCurses.GLXC.JUSTIFY_LEFT
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = None
        vline.preferred_width = None
        vline.spacing = None
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = -1
        vline.preferred_width = -1
        vline.spacing = -1
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = 0
        vline.preferred_width = 0
        vline.spacing = 0
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = -1000
        vline.preferred_width = -100
        vline.spacing = -10
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        # glxc.JUSTIFY_RIGHT -> self.get_width() - self.get_preferred_width() - self.get_spacing()
        vline._justify = GLXCurses.GLXC.JUSTIFY_RIGHT
        vline.width = 124
        vline.preferred_width = 80
        vline._check_justify()
        self.assertEqual(vline._x_offset, 44)

        vline.width = None
        vline.preferred_width = None
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = -1
        vline.preferred_width = -1
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = 0
        vline.preferred_width = -0
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

        vline.width = -1000
        vline.preferred_width = -100
        vline._check_justify()
        self.assertEqual(vline._x_offset, 0)

    def test__get_estimated_preferred_width(self):
        """Test VSeparator._get_estimated_preferred_width()"""
        vline = GLXCurses.VSeparator()
        self.assertEqual(vline._get_estimated_preferred_width(), 1)

    def test__get_estimated_preferred_height(self):
        """Test VSeparator._get_estimated_preferred_height()"""
        vline = GLXCurses.VSeparator()
        vline.y = 20
        vline.height = 20
        self.assertEqual(vline._get_estimated_preferred_height(), 40)

    def test__set__get_vseperator_x(self):
        """Test VSeparator._set_vseperator_x() and VSeparator._get_vseperator_x()"""
        vline = GLXCurses.VSeparator()
        # call set_decorated() with 0 as argument
        vline._set_x_offset(0)
        # verify we go back 0
        self.assertEqual(vline._get_x_offset(), 0)
        # call set_decorated() with 0 as argument
        vline._set_x_offset(42)
        # verify we go back 0
        self.assertEqual(vline._get_x_offset(), 42)
        # test raise TypeError
        self.assertRaises(TypeError, vline._set_x_offset, 'Galaxie')

    def test__set__get_vseperator_y(self):
        """Test VSeparator._set_vseperator_y() and VSeparator._get_vseperator_y()"""
        vline = GLXCurses.VSeparator()
        # call set_decorated() with 0 as argument
        vline._set_y_offset(0)
        # verify we go back 0
        self.assertEqual(vline._get_y_offset(), 0)
        # call set_decorated() with 0 as argument
        vline._set_y_offset(42)
        # verify we go back 0
        self.assertEqual(vline._get_y_offset(), 42)
        # test raise TypeError
        self.assertRaises(TypeError, vline._set_y_offset, 'Galaxie')
