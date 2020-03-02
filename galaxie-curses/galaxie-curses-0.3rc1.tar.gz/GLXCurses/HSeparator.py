#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import curses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved


class HSeparator(GLXCurses.Widget):
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

        .. py:__area_data:: position_type

            PositionType: CENTER, TOP, BOTTOM

              +---------------+-------------------------------+
              | Type          | :py:__area_data:`PositionType`       |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | CENTER                        |
              +---------------+-------------------------------+

        """
        # Load heritage
        GLXCurses.Widget.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.HSeparator'
        self.name = '{0}{1}'.format(self.__class__.__name__, self.id)

        # Make a Widget Style heritage attribute as local attribute
        if self.style.get_attribute_states():
            self.set_attribute_states(self.style.get_attribute_states())

        # Size management
        self.preferred_height = 1

        # PositionType: CENTER, TOP, BOTTOM
        self._position_type = GLXCurses.GLXC.POS_CENTER

        # Internal Widget Setting
        self._x_offset = 0
        self._y_offset = 0

    def draw_widget_in_area(self):
        """
        Call by the \
        :func:`Widget.draw() <GLXCurses.Widget.Widget.draw()>` method each time the MainLoop call a \
        :func:`Application.refresh() <GLXCurses.Application.Application.refresh()>`
        """
        self.create_or_resize()

        self.preferred_width = self._get_estimated_preferred_width()
        self.preferred_height = self._get_estimated_preferred_height()

        self._check_position_type()
        if self.height >= self.preferred_height:
            if self.width >= self.preferred_width:
                self._draw_horizontal_separator()

    def set_position_type(self, position_type):
        """
        Set the Position of the Horizontal separator

        PositionType: GLXC.POS_TOP, GLXC.POS_CENTER, GLXC.POS_BOTTOM

        :param position_type: a PositionType
        :type position_type: str
        """
        if position_type in GLXCurses.GLXC.PositionType:
            if self.get_position_type() != str(position_type).upper():
                self._position_type = str(position_type).upper()
        else:
            raise TypeError('PositionType must a valid GLXC.PositionType')

    def get_position_type(self):
        """
        Return the Position Type of the Horizontal separator

        PositionType:

         GLXC.POS_TOP

         GLXC.POS_CENTER

         GLXC.POS_BOTTOM

        :return: the position type string
        :rtype: str
        """
        return self._position_type

    # Internal
    def _check_position_type(self):
        """
        Check the PositionType of the Y axe

        PositionType:
         .glxc.POS_TOP
         .glxc.POS_CENTER
         .glxc.POS_BOTTOM
        """
        height = self.height
        preferred_height = self.preferred_height

        if self.get_position_type() == GLXCurses.GLXC.POS_CENTER:

            # Clamp height
            if height is None:
                estimated_height = 0
            elif height <= 0:
                estimated_height = 0
            elif height == 1:
                # prevent a 1/2 = float(0.5) case
                estimated_height = 0
            else:
                estimated_height = int(height / 2)

            # Clamp preferred_height
            if preferred_height is None:
                estimated_preferred_height = 0
            elif preferred_height <= 0:
                estimated_preferred_height = 0
            else:
                estimated_preferred_height = preferred_height

            # Make teh compute
            final_value = int(estimated_height - estimated_preferred_height)

            # Clamp the result to a positive
            if final_value <= 0:
                final_value = 0

            # Finally set the result
            self._set_y_offset(final_value)

        elif self.get_position_type() == GLXCurses.GLXC.POS_TOP:
            self._set_y_offset(0)

        elif self.get_position_type() == GLXCurses.GLXC.POS_BOTTOM:

            # Clamp height
            estimated_height = GLXCurses.clamp_to_zero(height)

            # Clamp preferred_height
            estimated_preferred_height = GLXCurses.clamp_to_zero(preferred_height)

            # Make the compute
            final_value = int(estimated_height - estimated_preferred_height)

            # Clamp the result to a positive
            if final_value <= 0:
                final_value = 0

            # Finally set the result
            self._set_y_offset(final_value)

    def _draw_horizontal_separator(self):
        """Draw the Horizontal Separator with PositionType"""
        if self.width >= self.preferred_width:
            if self.parent and self.parent.get_decorated():
                self.subwin.hline(
                    self._get_y_offset(),
                    1,
                    curses.ACS_HLINE,
                    self.preferred_width - 2,
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
            else:
                self.subwin.hline(
                    self._get_y_offset(),
                    self._get_x_offset(),
                    curses.ACS_HLINE,
                    self.preferred_width,
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )

    def _get_estimated_preferred_width(self):
        """
        Estimate a preferred width, by consider X Location, allowed width

        :return: a estimated preferred width
        :rtype: int
        """
        estimated_preferred_width = 0
        estimated_preferred_width += self.width
        return estimated_preferred_width

    @staticmethod
    def _get_estimated_preferred_height():
        """
        Estimate a preferred height, by consider Y Location

        :return: a estimated preferred height
        :rtype: int
        """
        estimated_preferred_height = 1
        return estimated_preferred_height

    def _set_x_offset(self, number):
        """
        Set the Horizontal Axe Separator X

        :param number: the new value
        :type number: int
        """
        if type(number) == int:
            if self._get_x_offset() != number:
                self._x_offset = number
        else:
            raise TypeError('>number< is not a int type')

    def _get_x_offset(self):
        """
        Return Horizontal Axe Separator

        :return: hseperator_x value
        :rtype: int
        """
        return self._x_offset

    def _set_y_offset(self, number):
        """
        Set the Horizontal Axe Separator

        :param number: the new value of hseperator_x
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

        :return: hseperator_y value
        :rtype: int
        """
        return self._y_offset
