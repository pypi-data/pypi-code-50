#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

import GLXCurses
import curses
import logging


class CheckButton(GLXCurses.Widget):
    def __init__(self):
        # Load heritage
        GLXCurses.Widget.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.CheckButton'
        self.name = '{0}{1}'.format(self.__class__.__name__, self.id)

        # Make a Widget Style heritage attribute as local attribute
        if self.style.get_attribute_states():
            self.set_attribute_states(self.style.get_attribute_states())

        # Internal Widget Setting
        self.text = None
        self._x_offset = 0
        self._y_offset = 0

        # Interface
        self.interface_unactivated = '[ ] '
        self.interface_active = '[x] '
        self.interface = self.interface_unactivated

        # Size management
        self._update_preferred_sizes()

        # Justification: LEFT, RIGHT, CENTER
        self._justify = GLXCurses.GLXC.JUSTIFY_CENTER

        # PositionType: CENTER, TOP, BOTTOM
        self._position_type = GLXCurses.GLXC.POS_CENTER

        # Sensitive
        self.can_default = True
        self.can_focus = True
        self.set_sensitive(True)
        self.states_list = None

        # States
        self.curses_mouse_states = {
            GLXCurses.GLXC.BUTTON1_PRESSED: 'BUTTON1_PRESS',
            GLXCurses.GLXC.BUTTON1_RELEASED: 'BUTTON1_RELEASED',
            GLXCurses.GLXC.BUTTON1_CLICKED: 'BUTTON1_CLICKED',
            GLXCurses.GLXC.BUTTON1_DOUBLE_CLICKED: 'BUTTON1_DOUBLE_CLICKED',
            GLXCurses.GLXC.BUTTON1_TRIPLE_CLICKED: 'BUTTON1_TRIPLE_CLICKED',

            GLXCurses.GLXC.BUTTON2_PRESSED: 'BUTTON2_PRESSED',
            GLXCurses.GLXC.BUTTON2_RELEASED: 'BUTTON2_RELEASED',
            GLXCurses.GLXC.BUTTON2_CLICKED: 'BUTTON2_CLICKED',
            GLXCurses.GLXC.BUTTON2_DOUBLE_CLICKED: 'BUTTON2_DOUBLE_CLICKED',
            GLXCurses.GLXC.BUTTON2_TRIPLE_CLICKED: 'BUTTON2_TRIPLE_CLICKED',

            GLXCurses.GLXC.BUTTON3_PRESSED: 'BUTTON3_PRESSED',
            GLXCurses.GLXC.BUTTON3_RELEASED: 'BUTTON3_RELEASED',
            GLXCurses.GLXC.BUTTON3_CLICKED: 'BUTTON3_CLICKED',
            GLXCurses.GLXC.BUTTON3_DOUBLE_CLICKED: 'BUTTON3_DOUBLE_CLICKED',
            GLXCurses.GLXC.BUTTON3_TRIPLE_CLICKED: 'BUTTON3_TRIPLE_CLICKED',

            GLXCurses.GLXC.BUTTON4_PRESSED: 'BUTTON4_PRESSED',
            GLXCurses.GLXC.BUTTON4_RELEASED: 'BUTTON4_RELEASED',
            GLXCurses.GLXC.BUTTON4_CLICKED: 'BUTTON4_CLICKED',
            GLXCurses.GLXC.BUTTON4_DOUBLE_CLICKED: 'BUTTON4_DOUBLE_CLICKED',
            GLXCurses.GLXC.BUTTON4_TRIPLE_CLICKED: 'BUTTON4_TRIPLE_CLICKED',

            GLXCurses.GLXC.BUTTON_SHIFT: 'BUTTON_SHIFT',
            GLXCurses.GLXC.BUTTON_CTRL: 'BUTTON_CTRL',
            GLXCurses.GLXC.BUTTON_ALT: 'BUTTON_ALT'
        }

        # Subscription
        self.connect('MOUSE_EVENT', CheckButton._handle_mouse_event)
        # Keyboard
        self.connect('CURSES', CheckButton._handle_key_event)

    def draw_widget_in_area(self):
        self.create_or_resize()

        if self.subwin is not None:
            # Many Thing's
            # Check if the text can be display
            text_have_necessary_width = (self.preferred_width >= 1)
            text_have_necessary_height = (self.preferred_height >= 1)
            if not text_have_necessary_height or not text_have_necessary_width:
                return

            if self.get_text():

                # Check if the text can be display
                text_have_necessary_width = (self.preferred_width >= 1)
                text_have_necessary_height = (self.preferred_height >= 1)
                if text_have_necessary_width and text_have_necessary_height:
                    self._draw_button()

    def set_active(self, boolean):
        self.state['ACTIVE'] = bool(boolean)
        self._check_active()

    def get_active(self):
        self._check_active()
        return self.state['ACTIVE']

    # Internal curses_subwin functions
    def set_text(self, text):
        self.text = text
        self._update_preferred_sizes()

    def get_text(self):
        return self.text

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justify):
        """
        Set the Justify of the Vertical separator

         Justify:
          - LEFT
          - CENTER
          - RIGHT

        :param justify: a Justify
        :type justify: str
        """
        if justify in [GLXCurses.GLXC.JUSTIFY_LEFT, GLXCurses.GLXC.JUSTIFY_CENTER, GLXCurses.GLXC.JUSTIFY_RIGHT]:
            if self.get_justify() != str(justify).upper():
                self._justify = str(justify).upper()
                # When the justify is set update preferred sizes store in Widget class
                self._update_preferred_sizes()
        else:
            raise TypeError('PositionType must be LEFT or CENTER or RIGHT')

    def get_justify(self):
        """
        Return the Justify of the CheckButton

         Justify:
          - LEFT
          - CENTER
          - RIGHT

        :return: str
        """
        return self._justify

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        """
        Set the Position type

        PositionType:
         .GLXCurses.GLXC.POS_TOP
         .GLXCurses.GLXC.POS_CENTER
         .GLXCurses.GLXC.POS_BOTTOM

        :param position_type: a PositionType
        :type position_type: str
        """
        if position_type in [GLXCurses.GLXC.POS_TOP, GLXCurses.GLXC.POS_CENTER, GLXCurses.GLXC.POS_BOTTOM]:
            if self.get_position_type() != str(position_type).upper():
                self._position_type = str(position_type).upper()
                # When the position type is set update preferred sizes store in Widget class
                self._update_preferred_sizes()
        else:
            raise TypeError('PositionType must be CENTER or TOP or BOTTOM')

    def get_position_type(self):
        """
        Return the Position Type

        PositionType:
         .GLXCurses.GLXC.POS_TOP
         .GLXCurses.GLXC.POS_CENTER
         .GLXCurses.GLXC.POS_BOTTOM

        :return: str
        """
        return self._position_type

    # Internal
    def _draw_button(self):
        self._check_active()
        self._update_preferred_sizes()
        self._check_justify()
        self._check_position_type()
        self._check_selected()

        if not self.get_sensitive():
            self._draw_the_good_button(
                color=self.style.get_color_pair(
                    foreground=self.style.get_color_text('bg', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                )
            )
        elif self.state['PRELIGHT']:
            self._draw_the_good_button(
                color=self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_PRELIGHT')
                )
            )
        elif self.state['NORMAL']:
            self._draw_the_good_button(
                color=self.style.get_color_pair(
                    foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                )
            )

    def _draw_the_good_button(self, color):
        try:
            # Interface management
            self.subwin.addstr(
                self._y_offset,
                self._x_offset,
                self.interface,
                color
            )
        except curses.error:
            pass

        try:
            # Draw the Horizontal Button with Justification and PositionType
            message_to_display = GLXCurses.resize_text(self.get_text(), self.width - 1 - len(self.interface), '~')
            self.subwin.addstr(
                self._y_offset,
                self._x_offset + len(self.interface),
                message_to_display,
                color
            )
        except curses.error:
            pass

    def _handle_mouse_event(self, event_signal, event_args):
        if self.get_sensitive():
            # Read the mouse event information's
            (mouse_event_id, x, y, z, event) = event_args
            # Be sure we select really the Button
            y -= self.y
            x -= self.x

            x_pos_start = (self._get_x_offset()) + len(self.interface) + len(self.get_text()) - 1
            x_pos_stop = (self._get_x_offset())
            y_pos_start = self._get_y_offset()
            y_pos_stop = self._get_y_offset() - self.preferred_height + 1

            that_for_me = (y_pos_start >= y >= y_pos_stop and x_pos_start >= x >= x_pos_stop)

            if that_for_me:
                self._grab_focus()
                self._check_selected()
                self._check_active()

                # BUTTON1
                if event == curses.BUTTON1_PRESSED:
                    pass

                elif event == curses.BUTTON1_RELEASED:
                    self.set_active(not self.get_active())

                if event == curses.BUTTON1_CLICKED:
                    self.set_active(not self.get_active())

                if event == curses.BUTTON1_DOUBLE_CLICKED:
                    pass

                if event == curses.BUTTON1_TRIPLE_CLICKED:
                    pass

                if event == 524288 or event == 134217728:
                    self.set_active(not self.get_active())

                # Create a Dict with everything
                instance = {
                    'class': self.__class__.__name__,
                    'label': self.get_text(),
                    'id': self.id
                }
                # EVENT EMIT
                self.emit(self.curses_mouse_states[event], instance)

        else:
            if self.debug:
                logging.debug('{0} -> id:{1}, object:{2}, is not sensitive'.format(
                    self.__class__.__name__,
                    self.id,
                    self
                ))

    def _handle_key_event(self, event_signal, *event_args):
        # Check if we have to care about keyboard event
        if self.get_sensitive() and \
                isinstance(GLXCurses.Application().has_focus, GLXCurses.Child) and \
                GLXCurses.Application().has_focus.id == self.id:
            # setting
            key = event_args[0]

            # Touch Escape
            if key == GLXCurses.GLXC.KEY_ESC:
                GLXCurses.Application().has_focus = None

                self._check_selected()

            if key == ord(" "):
                self._check_active()
                self.set_active(not self.get_active())

    def _check_active(self):
        if self.state['ACTIVE']:
            self.interface = self.interface_active
        else:
            self.interface = self.interface_unactivated

    def _grab_focus(self):
        """
        Internal method, for Select the contents of the Entry it take focus.

        See: grab_focus_without_selecting ()
        """
        if isinstance(GLXCurses.Application().has_focus, GLXCurses.Child) and \
                GLXCurses.Application().has_focus.id != self.id:
            GLXCurses.Application().has_focus = self

    def _check_selected(self):
        if self.can_focus:
            if isinstance(GLXCurses.Application().has_focus, GLXCurses.Child) and \
                    GLXCurses.Application().has_focus.id == self.id:
                self.is_focus = True
                self.has_focus = True
                self._set_state_prelight(True)
                self._update_preferred_sizes()
            else:
                self.is_focus = False
                self.has_focus = False
                self._set_state_prelight(False)
                self._update_preferred_sizes()
        else:
            pass

    def _set_state_prelight(self, value):
        """
        Internal function for set the state prelight, use for prelight the button during a click by example.

        :param value: True for enable, False for disable
        :type value: bool
        :raise TypeError: if ``value`` parameter is not a :py:__area_data:`bool`
        """
        # We exit as soon of possible
        if not isinstance(value, bool):
            raise TypeError("'value' argument must be a bool type")

        if self._get_state_prelight() != value:
            self.state['PRELIGHT'] = value

    def _get_state_prelight(self):
        """
        Get the prelight value as set by
        :func:`Button._set_state_prelight() <GLXCurses.Button.Button._set_state_prelight()>`

        :return: True for enable, False for disable
        :rtype: bool
        """
        return self.state['PRELIGHT']

    def _check_justify(self):
        """Check the justification of the X axe"""
        width = self.width - 1
        preferred_width = self.preferred_width

        self._set_x_offset(0)
        if self.get_justify() == GLXCurses.GLXC.JUSTIFY_CENTER:
            # Clamp value and impose the center
            if width is None:
                estimated_width = 0
            elif width <= 0:
                estimated_width = 0
            elif width == 1:
                estimated_width = 0
            else:
                estimated_width = int(width / 2)

            # Clamp value and impose the center
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
            self._x_offset = final_value

    def _check_position_type(self):
        # PositionType: CENTER, TOP, BOTTOM
        height = self.height - 1
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
            elif preferred_height == 1:
                # prevent a 1/2 = float(0.5) case
                estimated_preferred_height = 0
            else:
                estimated_preferred_height = int(preferred_height / 2)

            # Make teh compute
            final_value = int(estimated_height - estimated_preferred_height)

            # Clamp the result to a positive
            if final_value <= 0:
                final_value = 0

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

            # Clamp height
            estimated_height = GLXCurses.clamp_to_zero(height)

            # Clamp preferred_height
            estimated_preferred_height = GLXCurses.clamp_to_zero(preferred_height)

            # Make the compute
            final_value = int(estimated_height - estimated_preferred_height)

            # Clamp the result to a positive
            if final_value <= 0:
                final_value = 0

            self._set_y_offset(final_value)

    def _update_preferred_sizes(self):
        self.preferred_width = self._get_estimated_preferred_width()
        self.preferred_height = self._get_estimated_preferred_height()

    def _get_estimated_preferred_width(self):
        """
        Estimate a preferred width, by consider X Location, allowed width

        :return: a estimated preferred width
        :rtype: int
        """
        if self.get_text():
            estimated_preferred_width = 0
            estimated_preferred_width += len(self.get_text())
            estimated_preferred_width += len(self.interface)
        else:
            estimated_preferred_width = 0
            estimated_preferred_width += len(self.interface)

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

    def _set_x_offset(self, value=None):
        """
        Set _x

        :param value: A value to set to _x attribute
        :type value: int or None
        :raise TypeError: when value is not int or None
        """
        if type(value) is None or type(value) == int:
            self._x_offset = value
        else:
            raise TypeError('>value< must be a int or None type')

    def _get_x_offset(self):
        """
        Return the x space add to text for justify computation

        :return: _label_x attribute
        """
        return self._x_offset

    def _set_y_offset(self, value=None):
        """
        Set _y

        :param value: A value to set to _y attribute
        :type value: int or None
        :raise TypeError: when value is not int or None
        """
        if type(value) is None or type(value) == int:
            self._y_offset = value
        else:
            raise TypeError('>y< must be a int or None type')

    def _get_y_offset(self):
        """
        Return the _y space add to text for position computation

        :return: y attribute
        """
        return self._y_offset

    # Unimplemented
    def _enter(self):
        pass

    def _leave(self):
        pass

    @staticmethod
    def _key_pressed(char):
        if char > 255:
            return 0  # skip control-characters
        # if chr(char).upper() == self.LabelButton[self.Underline]:
        #     return 1
        else:
            return 0
