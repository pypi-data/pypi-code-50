#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import GLXCurses


class ApplicationMonitor(object):
    def __init__(self):
        self.widget_it_have_default = {
            'widget': None,
            'type': None,
            'id': None
        }
        self.widget_it_have_focus = {
            'widget': None,
            'type': None,
            'id': None
        }
        self.widget_it_have_tooltip = {
            'widget': None,
            'type': None,
            'id': None
        }

        self.__has_default = None
        self.__has_focus = None

    @property
    def has_default(self):
        return self.__has_default

    @has_default.setter
    def has_default(self, child=None):
        if child is not None and isinstance(child, GLXCurses.Widget):
            child_it_has_default = GLXCurses.Child()
            child_it_has_default.name = child.name
            child_it_has_default.id = child.id
            child_it_has_default.widget = child
            child = child_it_has_default
        if child is not None and not isinstance(child, GLXCurses.Child):
            raise TypeError('"child" must be a GLXCurses.Child instance or None')
        if self.has_default != child:
            self.__has_default = child

    @property
    def has_focus(self):
        return self.__has_focus

    @has_focus.setter
    def has_focus(self, child=None):
        if child is not None and isinstance(child, GLXCurses.Widget):
            child_it_has_focus = GLXCurses.Child()
            child_it_has_focus.name = child.name
            child_it_has_focus.id = child.id
            child_it_has_focus.widget = child
            child = child_it_has_focus
        if child is not None and not isinstance(child, GLXCurses.Child):
            raise TypeError('"child" must be a GLXCurses.Child instance or None')
        if self.has_focus != child:
            self.__has_focus = child

    def get_tooltip(self):
        """
        Return the unique id of the widget it have been set by \
        :func:`Application.set_tooltip() <GLXCurses.Application.Application.set_tooltip()>`

        .. seealso:: \
         :func:`Application.set_tooltip() <GLXCurses.Application.Application.set_tooltip()>`

         :func:`Widget.id <GLXCurses.Widget.Widget.id>`

        :return: a unique id generate by uuid module
        :rtype: long or None
        """
        return self.widget_it_have_tooltip

    def set_tooltip(self, widget=None):
        """
        Determines if the widget have to display a tooltip

        "Not implemented yet"

        .. seealso:: \
        :func:`Application.get_tooltip() <GLXCurses.Application.Application.get_tooltip()>`

        :param widget: a Widget
        :type widget: GLXCurses.Widget or None
        """
        if isinstance(widget, GLXCurses.Widget):
            info = {
                'widget': widget,
                'type': widget.glxc_type,
                'id': widget.id
            }
            if self.widget_it_have_tooltip != info:
                self.widget_it_have_tooltip = info
        else:
            info = {
                'widget': None,
                'type': None,
                'id': None
            }
            if self.widget_it_have_tooltip != info:
                self.widget_it_have_tooltip = info
