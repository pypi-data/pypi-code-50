#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import GLXCurses
import curses


class MenuBar(GLXCurses.Widget):
    def __init__(self):
        # Load heritage
        GLXCurses.Widget.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.MenuBar'
        self.name = '{0}{1}'.format(self.__class__.__name__, self.id)

        # Make a Style heritage attribute
        if self.style.get_attribute_states():
            self.set_attribute_states(self.style.get_attribute_states())

        # Internal Widget Setting
        self.app_info_label = None

    def draw(self):
        """
        White the menubar to the stdscr, the location is imposed to top left corner
        """
        self.create_or_resize()

        if self.subwin is not None:
            self._check_sizes()
            self._draw_background()

            if self.app_info_label:
                text = GLXCurses.resize_text(self.app_info_label, self.width, '~')
                try:
                    self.subwin.addstr(
                        0,
                        self.width - 1 - len(text),
                        text,
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('dark', 'STATE_NORMAL'),
                            background=self.style.get_color_text('light', 'STATE_NORMAL')
                        )
                    )

                except curses.error:
                    pass

    def _draw_background(self):
        try:
            self.subwin.addstr(
                0,
                0,
                ' ' * (self.width - 1),
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_PRELIGHT')
                )
            )
            self.subwin.insstr(
                0,
                self.width - 1,
                ' ',
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_PRELIGHT')
                )
            )
        except curses.error:
            pass

    def _check_sizes(self):
        self.preferred_height = 1
        self.preferred_width = self.width
