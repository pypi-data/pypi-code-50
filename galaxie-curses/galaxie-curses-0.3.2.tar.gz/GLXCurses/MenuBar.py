#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import GLXCurses
import logging
from curses import error as curses_error
from curses import A_BOLD
from curses import A_NORMAL


class MenuBar(GLXCurses.Box, GLXCurses.Dividable):
    def __init__(self):
        # Load heritage
        GLXCurses.Box.__init__(self)
        GLXCurses.Dividable.__init__(self)

        self.glxc_type = 'GLXCurses.{0}'.format(self.__class__.__name__)
        self.name = '{0}{1}'.format(self.__class__.__name__, self.id)

        # Internal Widget Setting
        self.can_focus = True
        self.can_default = True
        self.can_prelight = True

        self.__info_label = None
        self.info_label = None
        self.spacing = 2
        self.list_machin = []

        # Cab be remove
        self.debug = True


        # Subscription
        # Mouse
        self.connect('MOUSE_EVENT', MenuBar._handle_mouse_event)
        # Keyboard
        self.connect('CURSES', MenuBar._handle_key_event)

    @property
    def info_label(self):
        return self.__info_label

    @info_label.setter
    def info_label(self, text=None):
        if text is not None and type(text) != str:
            raise TypeError('"text" must be a str type or None')
        if self.info_label != text:
            self.__info_label = text

    def draw_widget_in_area(self):
        """
        White the menubar to the stdscr, the location is imposed to top left corner
        """
        self.create_or_resize()
        self._check_selected()
        self._update_sizes()
        self._update_preferred_sizes()
        if self.subwin:
            if self.debug:
                logging.debug('Draw {0}'.format(self))
                logging.debug(
                    "In Area -> x: {0}, y: {1}, width: {2}, height:{3}".format(
                        self.x,
                        self.y,
                        self.width,
                        self.height
                    )
                )
            self._draw_background()
            self._draw_menu_bar()
            self._draw_info_label()

    def _update_preferred_sizes(self):
        self.preferred_height = self.height
        self.preferred_width = self.width

    def _update_sizes(self):
        self.start = self.x
        self.stop = self.width - 1
        self.num = len(self.children)
        self.round_type = GLXCurses.GLXC.ROUND_DOWN

        self._upgrade_position()

    def _upgrade_position(self):
        mc_menu_start = 1
        mc_menu_scpacing = 5
        pos = mc_menu_start
        for child in self.children:
            if child.widget.title is not None:
                self.list_machin.append({'start': pos + 1, 'stop': pos + len(child.widget.title) + mc_menu_scpacing})
                pos += len(child.widget.title) + mc_menu_scpacing

    def _check_selected(self):
        if self.can_default:
            if GLXCurses.Application().has_default:
                if GLXCurses.Application().has_default.id == self.id:
                    self.has_default = True
                else:
                    self.has_default = False
        if self.can_focus:
            if GLXCurses.Application().has_focus:
                if GLXCurses.Application().has_focus.id == self.id:
                    self.has_focus = True
                else:
                    self.has_focus = False
        if self.can_prelight:
            if GLXCurses.Application().has_prelight:
                if GLXCurses.Application().has_prelight.id == self.id:
                    self.has_prelight = True
                else:
                    self.has_prelight = False

    def _grab_focus(self):
        """
        Internal method, for Select the contents of the Entry it take focus.

        See: grab_focus_without_selecting ()
        """
        if self.can_focus:
            GLXCurses.Application().has_focus = self
        if self.can_default:
            GLXCurses.Application().has_default = self
        if self.can_prelight:
            GLXCurses.Application().has_prelight = self

        self._check_selected()

    def _draw_info_label(self):
        if self.info_label:
            text = GLXCurses.resize_text(self.info_label, self.width, '~')
            for x_inc in range(0, len(text)):
                try:
                    self.subwin.addstr(
                        0,
                        self.width - len(text) + x_inc,
                        text[x_inc],
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('dark', 'STATE_NORMAL'),
                            background=self.style.get_color_text('light', 'STATE_NORMAL')
                        ) | A_BOLD
                    )
                except curses_error:
                    pass

    def _draw_background(self):
        for y_inc in range(0, self.height):
            for x_inc in range(0, self.width):
                try:
                    self.subwin.delch(y_inc, x_inc)
                    self.subwin.insstr(
                        y_inc,
                        x_inc,
                        ' ',
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('dark', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_PRELIGHT')
                        )
                    )
                except curses_error:
                    pass

    def _draw_menu_bar(self):
        if self.children:
            self.start = self.x
            self.stop = self.width
            self.num = len(self.children)
            self.round_type = GLXCurses.GLXC.ROUND_DOWN
            if self.can_focus and self.has_focus:
                color_shortcut = self.style.get_color_pair(
                    foreground='YELLOW',
                    background='CYAN'
                )
                color_base = self.style.get_color_pair(
                    foreground='GRAY',
                    background='CYAN'
                )

            else:
                color_shortcut = self.style.get_color_pair(
                    foreground='BLACK',
                    background='CYAN'
                )
                color_base = self.style.get_color_pair(
                    foreground='BLACK',
                    background='CYAN'
                )

            count = 0
            shortcut_to_display = False
            for child in self.children:
                if child.widget.title is not None:
                    for x_inc in range(0, len(child.widget.title)):
                        if child.widget.title[x_inc] == '_':
                            shortcut_to_display = True
                            continue
                        if shortcut_to_display:
                            try:
                                self.subwin.addstr(
                                    0,
                                    self.list_machin[count]['start'] + x_inc,
                                    child.widget.title[x_inc],
                                    color_shortcut
                                )
                            except curses_error:
                                pass
                            shortcut_to_display = False
                        else:
                            try:
                                self.subwin.addstr(
                                    0,
                                    self.list_machin[count]['start'] + x_inc,
                                    child.widget.title[x_inc],
                                    color_base
                                )
                            except curses_error:
                                pass
                    count += 1

    def _handle_mouse_event(self, event_signal, event_args):
        if self.sensitive:
            (mouse_event_id, x, y, z, event) = event_args
            # Be sure we select really the Button
            y -= self.y
            x -= self.x
            if 0 <= y <= self.height - 1:
                if 0 <= x <= self.preferred_width - 1:
                    # We are sure about the ToolBar have been clicked
                    self._grab_focus()

    def _handle_key_event(self, event_signal, *event_args):
        # Check if we have to care about keyboard event
        if self.has_focus:
            # setting
            key = event_args[0]
            # Touch Escape
            if key == GLXCurses.GLXC.KEY_ESC:
                GLXCurses.Application().has_focus = None
                GLXCurses.Application().has_default = None
                GLXCurses.Application().has_prelight = None
                self.has_focus = False
                self.has_prelight = False
                self.has_default = False

