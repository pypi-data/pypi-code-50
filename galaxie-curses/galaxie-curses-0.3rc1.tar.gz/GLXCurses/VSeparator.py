#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import GLXCurses
import curses


class VSeparator(GLXCurses.Widget, GLXCurses.Buildable):
    def __init__(self):
        """
        The GLXCurses.HSeparator widget is a horizontal separator, used to visibly separate the widgets within a \
        window. It displays a horizontal line.

        :Property's Details:

        .. py:__area_data:: name

            The widget can be named, which allows you to refer to them from a GLXCurses.Style

              +---------------+-------------------------------+
              | Type          | :py:__area_data:`str`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | HSeparator                    |
              +---------------+-------------------------------+

        .. py:__area_data:: Justify

            Justify: CENTER, LEFT, RIGHT

              +---------------+-------------------------------+
              | Type          | :py:__area_data:`Justify`            |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | CENTER                        |
              +---------------+-------------------------------+

        """
        # Load heritage
        GLXCurses.Widget.__init__(self)
        GLXCurses.Buildable.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.VSeparator'
        self.name = '{0}{1}'.format(self.__class__.__name__, self.id)

        # Make a Widget Style heritage attribute as local attribute
        if self.style.get_attribute_states():
            self.set_attribute_states(self.style.get_attribute_states())

        # Size management
        self.preferred_width = 1

        # Justification: LEFT, RIGHT, CENTER
        self._justify = GLXCurses.GLXC.JUSTIFY_CENTER

        # Internal Widget Setting
        self._x_offset = 0
        self._y_offset = 0

    def draw_widget_in_area(self):
        """
        Call by the \
        :func:`Widget.draw() <GLXCurses.Widget.Widget.draw()>` method each time the \
        :class:`MainLoop <GLXCurses.MainLoop.MainLoop>` call a \
        :func:`Application.refresh() <GLXCurses.Application.Application.refresh()>`
        """
        self.create_or_resize()

        if self.subwin is not None:
            self.preferred_width = self._get_estimated_preferred_width()
            self.preferred_height = self._get_estimated_preferred_height()
            self._check_justify()

            self._draw_vertical_separator()

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justify):
        """
        Set the Justify of the Vertical separator

         Justify:
            GLXC.JUSTIFY_LEFT

            GLXC.JUSTIFY_CENTER

            GLXC.JUSTIFY_RIGHT

            GLXC.JUSTIFY_FILL

        :param justify: a GLXC.Justification
        :type justify: str
        :raise TypeError: if ``justify`` is not a valide GLXC.Justification.
        """
        if str(justify).upper() not in GLXCurses.GLXC.Justification:
            raise TypeError("'justify' must be a valid GLXC.Justification")

        if self.get_justify() != str(justify).upper():
            self._justify = str(justify).upper()

    def get_justify(self):
        """
        Return the Justify of the Vertical separator

         Justify:
          - LEFT
          - CENTER
          - RIGHT

        :return: a GLXC.Justification
        :rtype: str
        """
        return self._justify

    # Internal
    def _check_justify(self):
        """Check the justification of the X axe"""
        width = self.width
        preferred_width = self.preferred_width

        if self.get_justify() == GLXCurses.GLXC.JUSTIFY_CENTER:
            # Clamp value et impose the center
            if width is None:
                estimated_width = 0
            elif width <= 0:
                estimated_width = 0
            elif width == 1:
                estimated_width = 0
            else:
                estimated_width = int(width / 2)

            # Clamp value et impose the center
            if preferred_width is None:
                estimated_preferred_width = 0
            elif preferred_width <= 0:
                estimated_preferred_width = 0
            elif preferred_width == 1:
                estimated_preferred_width = 0
            else:
                estimated_preferred_width = int(preferred_width / 2)

            # Make the compute
            final_value = int(estimated_width - estimated_preferred_width)

            # clamp the result
            if final_value <= 0:
                final_value = 0

            # Finally set the value
            self._set_x_offset(final_value)

        elif self.get_justify() == GLXCurses.GLXC.JUSTIFY_LEFT:

            # Finally set the value
            self._set_x_offset(0)

        elif self.get_justify() == GLXCurses.GLXC.JUSTIFY_RIGHT:

            # Clamp estimated_width
            estimated_width = GLXCurses.clamp_to_zero(width)

            # Clamp preferred_width
            estimated_preferred_width = GLXCurses.clamp_to_zero(preferred_width)

            # Make the compute
            final_value = int(estimated_width - estimated_preferred_width)

            # clamp the result
            if final_value <= 0:
                final_value = 0

            # Finally set the value
            self._set_x_offset(final_value)

    def _draw_vertical_separator(self):
        """Draw the Vertical Label with Justification and PositionType"""
        if self.height >= 1:
            if self.width >= 1:
                for y in range(self._get_y_offset(), self.height - 1):
                    self.subwin.insch(
                        int(self._get_y_offset() + y),
                        int(self._get_x_offset()),
                        curses.ACS_VLINE,
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )

    @staticmethod
    def _get_estimated_preferred_width():
        """
        Estimate a preferred width, by consider X Location, allowed width

        :return: a estimated preferred width
        :rtype: int
        """
        estimated_preferred_width = 1
        return estimated_preferred_width

    def _get_estimated_preferred_height(self):
        """
        Estimate a preferred height, by consider Y Location

        :return: a estimated preferred height
        :rtype: int
        """
        estimated_preferred_height = self.y
        estimated_preferred_height += self.height

        return estimated_preferred_height

    def _set_x_offset(self, number):
        """
        Set the Vertical Axe Separator

        :param number: the new value of vseperator_x
        :type number: int
        """
        if type(number) == int:
            if self._get_x_offset() != number:
                self._x_offset = number
        else:
            raise TypeError('>number< is not a int type')

    def _get_x_offset(self):
        """
        Return Vertical Axe Separator

        :return: _x_offset
        :rtype: int
        """
        return self._x_offset

    def _set_y_offset(self, number):
        """
        Set the Horizontal Axe Separator

        :param number: the new value of vseperator_x
        :type number: int
        """
        if type(number) == int:
            if self._get_y_offset() != number:
                self._y_offset = number
        else:
            raise TypeError('>number< is not a int type')

    def _get_y_offset(self):
        """
        Return Horizontal Axe Separator

        :return: vseperator_x
        :rtype: int
        """
        return self._y_offset
