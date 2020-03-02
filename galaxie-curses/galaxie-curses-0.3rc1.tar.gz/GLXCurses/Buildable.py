#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

# Inspired by: https://developer.gnome.org/gtk3/stable/GtkBuildable.html

import GLXCurses


class Buildable(object):
    def __init__(self):
        self.is_buildable = True
        self.name = self.__class__.__name__

    def set_name(self, buildable=None, name=None):
        """
        Sets the name of the ``buildable`` object.

        :param buildable: a GLXC.Buildable
        :type buildable: GLXC.Buildable or None
        :param name: name to set, None set name to the Class name
        :type name: str or none
        :raise TypeError: if ``name`` is not a a str or None type.
        :raise TypeError: if ``buildable`` is not a valid GLXCurses type.
        :raise TypeError: if ``buildable`` is not a instance of GLXCurses.Buildable.
        """
        if buildable is None:
            buildable = self

        if name is None:
            self.name = self.__class__.__name__

        # Try to exit as soon of possible
        if not GLXCurses.glxc_type(buildable):
            raise TypeError("'buildable' must be a GLXCurses type")
        if not isinstance(buildable, Buildable):
            raise TypeError("'buildable' must be an instance of GLXCurses.Buildable")
        # check new_text
        if type(name) != str:
            raise TypeError("'name' must be an str type or None")

        # make the job
        if self.get_name(buildable=buildable) != name:
            buildable.name = name

    def get_name(self, buildable=None):
        """
        Gets the name of the ``buildable`` object.

        :param buildable: a GLXC.Buildable
        :type buildable: GLXC.Buildable or None
        :return: the name set with GLXC.Buildable.set_name()
        :raise TypeError: if ``buildable`` is not a valid GLXCurses type.
        :raise TypeError: if ``buildable`` is not a instance of GLXCurses.Buildable.
        """
        if buildable is None:
            buildable = self

        # Try to exit as soon of possible
        if not GLXCurses.glxc_type(buildable):
            raise TypeError("'buildable' must be a GLXCurses type")
        if not isinstance(buildable, Buildable):
            raise TypeError("'buildable' must be an instance of GLXCurses.Buildable")

        # make the job
        return buildable.name
