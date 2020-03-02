#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import unittest
from GLXCurses import Application

################################################################################
# IT TEST IS REQUIRE FORE CLOSE THE GLXCURSES APPLICATION AFTER UNITTEST TESTS #
################################################################################


# Unittest
class TestZZZ(unittest.TestCase):
    def setUp(self):
        """Get Application Singleton"""
        # Before the test start
        self.application = Application()


    def test_GLXCurses_final_refresh(self):
        """GLXCurses Final refresh"""
        # entry.draw_widget_in_area()
        self.application.refresh()
        self.application.screen.close()
