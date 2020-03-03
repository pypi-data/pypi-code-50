#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

"""
Created on 4 avr. 2015

@author: Tuuux
"""

import curses
import os
from operator import itemgetter
import time
import logging

import GLXCurses


class CreateHistoryBox(object):

    def __init__(self, model=None, y=None, x=None, label=None):

        self.parent = model.stdscr
        self.y_parent, self.x_parent = self.parent.getbegyx()
        self.y_max_parent, self.x_max_parent = self.parent.getmaxyx()
        self.y = y
        self.x = x
        self.label = str(label)
        self.label = str(" " + label + " ")
        self.Width = len(str(label))

        # Look for history window size it depend of the history list
        if len(model.history_dir_list) + 2 < self.y_max_parent:
            history_y = len(model.history_dir_list) + 2

        else:
            history_y = self.y_max_parent - 1

        if len(model.history_dir_list) > 0:
            history_x = len(max(model.history_dir_list, key=len)) + 2
            if history_x > self.x_max_parent - 1:
                history_x = self.x_max_parent
        else:
            history_x = len(self.label) + 2

        history_box = self.parent.subwin(
            history_y,
            history_x,
            2,
            0
        )

        # Inside the history menu
        history_box.bkgdset(
            ord(' '),
            model.style.get_color_pair(
                foreground=model.style.get_color_text('dark', 'STATE_NORMAL'),
                background=model.style.get_color_text('base', 'STATE_NORMAL')
            )
        )
        history_box.bkgd(
            ord(' '),
            model.style.get_color_pair(
                foreground=model.style.get_color_text('dark', 'STATE_NORMAL'),
                background=model.style.get_color_text('base', 'STATE_NORMAL')
            )
        )

        history_box_num_lines, history_box_num_cols = history_box.getmaxyx()
        max_cols_to_display = history_box_num_cols - 2
        max_lines_to_display = 1

        for I in range(0, history_box_num_lines - 2):
            history_box.addstr(I + 1,
                               1,
                               str(" " * int(history_box_num_cols - 2)),
                               model.style.get_color_pair(
                                   foreground=model.style.get_color_text('dark', 'STATE_NORMAL'),
                                   background=model.style.get_color_text('base', 'STATE_NORMAL')
                               )
                               )
            max_lines_to_display += 1
        model.history_menu_can_be_display = max_lines_to_display

        for I in range(0 + model.history_menu_item_list_scroll, model.history_menu_can_be_display):
            if I < len(model.history_dir_list):

                if model.history_menu_selected_item == I:
                    model.history_menu_selected_item_value = model.history_dir_list[I]
                    if len(str(model.history_dir_list[I])) >= max_cols_to_display:
                        history_box.addstr(
                            I + 1,
                            1,
                            str(model.history_dir_list[I][:max_cols_to_display]),
                            model.style.get_color_pair(
                                foreground='BLUE',
                                background=model.style.get_color_text('bg', 'STATE_SELECTED')
                            )
                        )
                    else:
                        history_box.addstr(
                            I + 1,
                            1,
                            str(model.history_dir_list[I]),
                            model.style.get_color_pair(
                                foreground='BLUE',
                                background=model.style.get_color_text('bg', 'STATE_SELECTED')
                            )
                        )
                        history_box.addstr(
                            I + 1,
                            len(str(model.history_dir_list[I])) + 1,
                            str(" " * int(
                                history_box_num_cols - 2 - len(str(model.history_dir_list[I])))),
                            model.style.get_color_pair(
                                foreground='BLUE',
                                background=model.style.get_color_text('bg', 'STATE_SELECTED')
                            )
                        )
                else:
                    if len(str(model.history_dir_list[I])) >= max_cols_to_display:
                        history_box.addstr(
                            I + 1,
                            1,
                            str(model.history_dir_list[I][:max_cols_to_display]),
                            model.style.get_color_pair(
                                foreground=model.style.get_color_text('dark', 'STATE_NORMAL'),
                                background=model.style.get_color_text('base', 'STATE_NORMAL')
                            )
                        )
                    else:
                        history_box.addstr(
                            I + 1,
                            1,
                            str(model.history_dir_list[I]),
                            model.style.get_color_pair(
                                foreground=model.style.get_color_text('dark', 'STATE_NORMAL'),
                                background=model.style.get_color_text('base', 'STATE_NORMAL')
                            )
                        )

        history_box.box()
        # Title
        history_box.addstr(
            0,
            (int(history_box_num_cols / 2)) - int((len(self.label) / 2)),
            self.label,
            model.style.get_color_pair(
                foreground='BLUE',
                background=model.style.get_color_text('base', 'STATE_NORMAL')
            )
        )

    def mouse_clicked(self, mouse_event):
        (event_id, x, y, z, event) = mouse_event
        if self.y_parent <= y <= self.y_parent + 1:
            if self.x + self.x_parent <= x < self.x + self.x_parent + self.Width:
                return 1
        else:
            return 0


class FileSelect(GLXCurses.Widget):
    def __init__(self):
        # Load heritage
        GLXCurses.Widget.__init__(self)

        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.FileSelect'
        self.name = '{0}{1}'.format(self.__class__.__name__, self.id)

        # Make a Widget Style heritage attribute as local attribute
        if self.style.get_attribute_states():
            self.set_attribute_states(self.style.get_attribute_states())

        # Variables:
        self.dir_name = None
        self.sort_by_name = None
        self.sort_name_order = None
        self.sort_by_size = None
        self.sort_size_order = None
        self.sort_by_mtime = None
        self.sort_mtime_order = None
        self.item_list = None
        self.item_info_list = None
        self.item_it_can_be_display = None
        self.item_scroll_pos = None
        self.selected_item_pos = None
        self.selected_item_info_list = None
        self.app_file_extensions = None

        # Object use for clickable Text
        self.name_text_object = None
        self.size_text_object = None
        self.mtime_text_object = None

        self.display_history_menu = 0
        self.display_history_text = 'History'
        self.history_dir_list_object = None
        self.history_dir_list_prev_object = None
        self.history_dir_list_next_object = None
        self.history_dir_list = list()
        self.history_menu_selected_item = 0
        self.history_menu_selected_item_value = "."
        self.history_menu_item_list_scroll = 0
        self.history_menu_can_be_display = 0
        self.history_menu_item_number = 0

        # Scroll

        # Set thing for the first time, yes like a boss ...
        self.set_sort_by_name(True)
        self.set_sort_name_order(True)
        self.set_sort_by_size(False)
        self.set_sort_size_order(True)
        self.set_sort_by_mtime(False)
        self.set_sort_mtime_order(True)

        self._set_item_it_can_be_display(0)
        self._set_item_scroll_pos(0)
        self._set_selected_item_pos(0)
        self._set_selected_item_info_list(list())

        # Size management
        self.border_len = 2

        # Mouse speed
        self.time_last_scroll_up = time.time()
        self.time_last_scroll_down = time.time()

        # States
        self.curses_mouse_states = {
            curses.BUTTON1_PRESSED: 'BUTTON1_PRESS',
            curses.BUTTON1_RELEASED: 'BUTTON1_RELEASED',
            curses.BUTTON1_CLICKED: 'BUTTON1_CLICKED',
            curses.BUTTON1_DOUBLE_CLICKED: 'BUTTON1_DOUBLE_CLICKED',
            curses.BUTTON1_TRIPLE_CLICKED: 'BUTTON1_TRIPLE_CLICKED',

            curses.BUTTON2_PRESSED: 'BUTTON2_PRESSED',
            curses.BUTTON2_RELEASED: 'BUTTON2_RELEASED',
            curses.BUTTON2_CLICKED: 'BUTTON2_CLICKED',
            curses.BUTTON2_DOUBLE_CLICKED: 'BUTTON2_DOUBLE_CLICKED',
            curses.BUTTON2_TRIPLE_CLICKED: 'BUTTON2_TRIPLE_CLICKED',

            curses.BUTTON3_PRESSED: 'BUTTON3_PRESSED',
            curses.BUTTON3_RELEASED: 'BUTTON3_RELEASED',
            curses.BUTTON3_CLICKED: 'BUTTON3_CLICKED',
            curses.BUTTON3_DOUBLE_CLICKED: 'BUTTON3_DOUBLE_CLICKED',
            curses.BUTTON3_TRIPLE_CLICKED: 'BUTTON3_TRIPLE_CLICKED',

            # curses.BUTTON4_PRESSED: 'BUTTON4_PRESSED',
            # curses.BUTTON4_RELEASED: 'BUTTON4_RELEASED',
            # curses.BUTTON4_CLICKED: 'BUTTON4_CLICKED',
            # curses.BUTTON4_DOUBLE_CLICKED: 'BUTTON4_DOUBLE_CLICKED',
            # curses.BUTTON4_TRIPLE_CLICKED: 'BUTTON4_TRIPLE_CLICKED',

            curses.REPORT_MOUSE_POSITION: 'MOUSE_WHEEL_DOWN',
            curses.BUTTON4_PRESSED: 'MOUSE_WHEEL_UP',

            curses.BUTTON_SHIFT: 'BUTTON_SHIFT',
            curses.BUTTON_CTRL: 'BUTTON_CTRL',
            curses.BUTTON_ALT: 'BUTTON_ALT'
        }

        # self.model = model
        self.rep_sup_text = "UP--DIR"
        self.name_text = "Name"
        self.size_text = "Size"
        self.mtime_text = "Modify time"
        self.sort_name_letter = self.name_text[0].lower()
        self.sort_size_letter = self.size_text[0].lower()
        self.sort_mtime_letter = self.mtime_text[0].lower()
        self.history_button_text_prev = '<'
        self.history_button_text_list = '.[^]'
        self.history_button_text_next = '<'

        self._update_directory_list()

        # Sensitive
        self.can_default = True
        self.can_focus = True
        self.sensitive = True
        self.states_list = None
        self._focus_without_selecting = False

        # Subscription
        # Mouse
        self.connect('MOUSE_EVENT', FileSelect._handle_mouse_event)
        # Keyboard
        self.connect('CURSES', FileSelect._handle_key_event)

    def _update_directory_list(self):
        # We consider to be on the local directory
        self._set_item_list(os.listdir(os.getcwd()))
        self._get_item_list().sort()

        # Prepare the super list with all information's to display
        self._set_item_info_list()
        for item in self._get_item_list():
            self._get_item_info_list().append(self._get_item_info(item))

        # Prepare list by sort
        # Sort by name
        if self.get_sort_by_name():
            list_file = list()
            list_dir = list()
            if self.get_sort_name_order():
                for tmp in self._get_item_list():
                    if os.path.isfile(tmp):
                        list_file.append(tmp)
                    else:
                        list_dir.append(tmp)
                list_file.sort()
                list_dir.sort()
            else:
                for tmp in reversed(self._get_item_list()):
                    if os.path.isfile(tmp):
                        list_file.append(tmp)
                    else:
                        list_dir.append(tmp)
            self._set_item_list(list_dir + list_file)

        # # Sort by size
        elif self.get_sort_by_size():
            self._get_item_info_list().sort(key=itemgetter(4))
            tmp_file = list()
            if self.get_sort_size_order():
                for tmp in self._get_item_info_list():
                    tmp_file.append(tmp[0])
            else:
                for tmp in reversed(self._get_item_info_list()):
                    tmp_file.append(tmp[0])

            self._set_item_list(tmp_file)

        # # Sort by Time
        elif self.get_sort_by_mtime():
            self.item_info_list.sort(key=itemgetter(5))
            tmp_file = list()
            if self.get_sort_mtime_order() == 0:
                for tmp in self._get_item_info_list():
                    tmp_file.append(tmp[0])
            else:
                for tmp in reversed(self._get_item_info_list()):
                    tmp_file.append(tmp[0])

            self._set_item_list(tmp_file)

        # At end insert .. for permit to back to the parent directory
        self._get_item_list().insert(0, '..')

    def set_app_file_extensions(self, file_extensions=None):
        """
        A tuple of file extension to colorize, it's consider as file type you searching for.

        The FileChooser will colorize they file's, in orange.

        Note the function automatically deal with case sensitive.

        Example: .mkv -> ('.mkv','.Mkv','MKV')

        :param file_extensions: a tuple of file extension to colorize or None for disable the colorize.
        :type file_extensions: tuple or None
        :raise TypeError: when ``file_extensions`` argument is not a tuple type or None
        """
        if file_extensions is None:
            if self.get_app_file_extensions() is not None:
                self.app_file_extensions = None
                return

        # Exit as soon of possible
        if type(file_extensions) != tuple:
            raise TypeError("'file_extensions' must be a tuple type")

        # Create a Tuple with Upper Lower and Title extension
        # Example: .mkv -> ('.mkv','.Mkv','MKV')
        file_extensions_temp = list()
        # Lower -> .mkv
        for I in list(file_extensions):
            file_extensions_temp.append(I.lower())
        # Title -> Mkv
        for I in list(file_extensions):
            file_extensions_temp.append(I.title())
        # Upper -> .MKV
        for I in list(file_extensions):
            file_extensions_temp.append(I.upper())
        video_file_extensions = tuple(file_extensions_temp)

        if self.get_app_file_extensions() != video_file_extensions:
            self.app_file_extensions = video_file_extensions

    def get_app_file_extensions(self):
        """
        Return the list of file extension to colorize.

        See . Filechooser.set_app_file_extensions() for more details.

        :return: a tuple of file extension to colorize or None if disable.
        :rtype: tuple or None
        """
        return self.app_file_extensions

    def set_sort_by_name(self, boolean=True):
        """
        Set the sort_by_name attribute . It use for display files and directory sorted by name.

        :param boolean: True for enable, False for disable
        :type boolean: bool
        :raise TypeError: when ``boolean`` argument is not a bool type
        """
        # Exit as soon of possible
        if type(boolean) != bool:
            raise TypeError("'boolean' must be a bool type")

        # just in case we make the job
        if self.get_sort_by_name() != boolean:
            self.sort_by_name = boolean

    def get_sort_by_name(self):
        """
        Return sort_by_name attribute.

        :return: True if enable, False if disable
        :rtype: bool
        """
        return self.sort_by_name

    def set_sort_name_order(self, boolean=True):
        """
        Set the sort_name_order attribute . It use for display files and directory sorted by name in order.

        Order are:
            True for A to Z
            False for Z to A

        :param boolean: True for A to Z, False for Z to A
        :type boolean: bool
        :raise TypeError: when ``boolean`` argument is not a bool type
        """
        # Exit as soon of possible
        if type(boolean) != bool:
            raise TypeError("'boolean' must be a bool type")

        # just in case we make the job
        if self.get_sort_name_order() != boolean:
            self.sort_name_order = boolean

    def get_sort_name_order(self):
        """
        Return sort_name_order attribute.

        :return: True if ordering A to Z, False if ordering Z to A
        :rtype: bool
        """
        return self.sort_name_order

    def set_sort_by_size(self, boolean=False):
        """
        Set the sort_by_size attribute . It use for display files and directory sorted by size.

        :param boolean: True for enable, False for disable
        :type boolean: bool
        :raise TypeError: when ``boolean`` argument is not a bool type
        """
        # Exit as soon of possible
        if type(boolean) != bool:
            raise TypeError("'boolean' must be a bool type")

        # just in case we make the job
        if self.get_sort_by_size() != boolean:
            self.sort_by_size = boolean

    def get_sort_by_size(self):
        """
        Return sort_by_size attribute.

        :return: True if enable, False if disable
        :rtype: bool
        """
        return self.sort_by_size

    def set_sort_size_order(self, boolean=True):
        """
        Set the sort_size_order attribute . It use for display files and directory sorted by size in order.

        Order are:
            True: Min to Max
            False: Max to Min

        :param boolean: True if ordering Min to Max, False if ordering Max to Min.
        :type boolean: bool
        :raise TypeError: when ``boolean`` argument is not a bool type
        """
        # Exit as soon of possible
        if type(boolean) != bool:
            raise TypeError("'boolean' must be a bool type")

        # just in case we make the job
        if self.get_sort_size_order() != boolean:
            self.sort_size_order = boolean

    def get_sort_size_order(self):
        """
        Return sort_by_size attribute. as set by set_sort_size_order()

        :return: True if enable, False if disable
        :rtype: bool
        """
        return self.sort_size_order

    def set_sort_by_mtime(self, boolean=False):
        """
        Set the sort_by_mtime attribute . It use for display files and directory sorted by mtime.

        :param boolean: True for enable, False for disable
        :type boolean: bool
        :raise TypeError: when ``boolean`` argument is not a bool type
        """
        # Exit as soon of possible
        if type(boolean) != bool:
            raise TypeError("'boolean' must be a bool type")

        # just in case we make the job
        if self.get_sort_by_mtime() != boolean:
            self.sort_by_mtime = boolean

    def get_sort_by_mtime(self):
        """
        Return sort_by_mtime attribute.

        :return: True if enable, False if disable
        :rtype: bool
        """
        return self.sort_by_mtime

    def set_sort_mtime_order(self, boolean=True):
        """
        Set the sort_size_order attribute . It use for display files and directory sorted by mtime in order.

        Order are:
            True: Now to Ago
            False: Ago to Now

        :param boolean: True if ordering Now to Ago, False if ordering Ago to Now.
        :type boolean: bool
        :raise TypeError: when ``boolean`` argument is not a bool type
        """
        # Exit as soon of possible
        if type(boolean) != bool:
            raise TypeError("'boolean' must be a bool type")

        # just in case we make the job
        if self.get_sort_mtime_order() != boolean:
            self.sort_mtime_order = boolean

    def get_sort_mtime_order(self):
        """
        Return sort_mtime_order attribute. as set by set_sort_mtime_order()

        :return: True if ordering Now to Ago, False if ordering Ago to Now.
        :rtype: bool
        """
        return self.sort_mtime_order

    def draw_widget_in_area(self):
        self.create_or_resize()

        #  May be it have no parent or that the first init, then test if subwin creation have work
        if self.subwin:

            # self._draw_background()
            self._update_preferred_sizes()
            self._update_directory_list()

            self._check_selected()

            if self.get_decorated():
                self._draw_box()

        self._draw_filechooser()

    def _draw_background(self):
        pass
        # self.subwin.bkgd(
        #     ord(' '),
        #     self.style.get_color_pair(
        #         foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
        #         background=self.style.get_color_text('bg', 'STATE_NORMAL')
        #     )
        #
        # )
        # self.subwin.bkgdset(
        #     ord(' '),
        #     self.style.get_color_pair(
        #         foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
        #         background=self.style.get_color_text('bg', 'STATE_NORMAL')
        #     )
        #
        # )
        #
        # for line in range(self.get_y(), self.height - 1):
        #     for char in range(self.get_x(), self.width - 1):
        #         self.subwin.addch(
        #             line,
        #             char,
        #             ' ',
        #             self.style.get_color_pair(
        #                 foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
        #                 background=self.style.get_color_text('bg', 'STATE_NORMAL')
        #             )
        #
        #         )

    def _draw_filechooser(self):

        # Apply the Background color and border
        if self.subwin is not None:
            self._draw_background()
            # if self.get_decorated():
            #     self.subwin.box()

        # History Line
        # History arrow for navigate inside history directory list
        self._draw_history_hline()
        self._draw_history_prev()
        self._draw_history_actual_path()
        self._draw_history_button()
        self._draw_history_next()

        # Titles Column
        self._draw_column_title_sorted_order()

        # Create 3 clickable elements for "Name", "Size", "Modify Time"
        self._draw_column_title_name()
        self._draw_column_title_size()
        self._draw_column_title_mtime()

        # Create 2 Vertical Lines for create columns for Name, Size and Modify Time
        self._draw_column_vline_mtime()
        self._draw_column_vline_size()

        # FOR qui occupe toute la fenetre avec des listes de fichiers
        count = 0

        for line_number in range(self._get_y_pos_items(), self.preferred_height - 2):

            if count < len(self._get_item_list()):

                # Force the selected high color line to stay on the aviable box size
                if self._get_selected_item_pos() + 1 > self._get_item_it_can_be_display():
                    self._set_selected_item_pos(self._get_selected_item_pos() - 1)

                try:
                    # We know how is the selected line
                    file_info_list = self._get_item_info(
                        os.path.join(
                            os.getcwd(),
                            self._get_item_list()[count + self._get_item_scroll_pos()],
                        )
                    )
                    # Draw normal line
                    self._draw_line_normal(line_number, file_info_list)

                    # Draw the selected Line
                    # That is the selected line enjoy, cher !!!!
                    if self._get_selected_item_pos() == count:
                        self._set_selected_item_info_list(file_info_list)
                        self._draw_line_selected(line_number, file_info_list)
                        self._draw_information_text(file_info_list[1])
                except IndexError:
                    continue

            count += 1

        # Information part
        self._draw_information_hline()

        # If the item value is '..' it use Directory setting
        # if self.get_is_focus():
        #     self._draw_information_text(file_info_list)

        # Disk Usage
        self._draw_information_disk_usage()

        # Test if the history widget should be display
        if self.display_history_menu:
            self.history_dialog_box = CreateHistoryBox(
                model=self,
                y=0,
                x=self._get_x_pos_history_list_label(),
                label=self.display_history_text,
            )

    def _draw_line_normal(self, line_number, file_info_list):
        # Special case of item_name_text text size , it have to be resize
        try:
            name_to_display = GLXCurses.resize_text(
                str(file_info_list[6]) + str(file_info_list[0]),
                self._get_name_collumn_width()
            )

            self.subwin.addstr(
                line_number,
                self._get_x_pos_line_start(),
                name_to_display,
                self.style.get_color_pair(
                    foreground=file_info_list[7],
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                ) | file_info_list[8]
            )
            size_to_display = GLXCurses.resize_text(
                str(file_info_list[2]),
                self._get_size_collumn_width()
            )
            self.subwin.addstr(
                line_number,
                (self._get_mtime_collumn_width() - len(
                    str(file_info_list[2]))),
                size_to_display,
                self.style.get_color_pair(
                    foreground=file_info_list[7],
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                ) | file_info_list[8]
            )
            self.subwin.addstr(
                line_number,
                self._get_mtime_collumn_width() + 1,
                str(file_info_list[3]),
                self.style.get_color_pair(
                    foreground=file_info_list[7],
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                ) | file_info_list[8]
            )
        except curses.error:
            pass

    def _draw_line_selected(self, line_number, file_info_list):
        try:
            # Paint the entire line with a hight light color
            self.subwin.addstr(
                line_number,
                self._get_x_pos_line_start(),
                str(" " * int(self._get_x_pos_line_stop() - self._get_x_pos_line_start())),
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_SELECTED'),
                    background=self.style.get_color_text('bg', 'STATE_SELECTED')
                )
            )

            # If that a file add a special character
            # Special case of item_name_text text size , it have to be resize
            name_to_display = GLXCurses.resize_text(
                str(file_info_list[6]) + str(file_info_list[0]),
                self._get_name_collumn_width()
            )
            self.subwin.addstr(
                line_number,
                self._get_x_pos_line_start(),
                name_to_display,
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_SELECTED'),
                    background=self.style.get_color_text('bg', 'STATE_SELECTED')
                )
            )
            self.subwin.vline(
                line_number,
                self._get_mtime_collumn_width() - self._get_size_collumn_width(),
                curses.ACS_VLINE,
                1,
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_SELECTED'),
                    background=self.style.get_color_text('bg', 'STATE_SELECTED')
                )
            )
            # Draw the Size
            self.subwin.addstr(
                line_number,
                (self._get_mtime_collumn_width() - len(
                    str(file_info_list[2]))),
                str(file_info_list[2]),
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_SELECTED'),
                    background=self.style.get_color_text('bg', 'STATE_SELECTED')
                )
            )
            # Draw the Date
            self.subwin.addstr(
                line_number,
                self._get_mtime_collumn_width() + 1,
                str(file_info_list[3]),
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_SELECTED'),
                    background=self.style.get_color_text('bg', 'STATE_SELECTED')
                )
            )
            # Draw the 2 vertical lines with high light color
            self.subwin.vline(
                line_number,
                self._get_mtime_collumn_width(),
                curses.ACS_VLINE,
                1,
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('dark', 'STATE_SELECTED'),
                    background=self.style.get_color_text('bg', 'STATE_SELECTED')
                )
            )

        except curses.error:
            pass

    def _draw_information_hline(self):
        try:
            if self.get_decorated():
                for x_inc in range(self._get_x_pos_line_start(), self._get_x_pos_line_stop() + 2):
                    self.subwin.addch(
                        self.preferred_height - 3,
                        x_inc,
                        curses.ACS_HLINE,
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )
            else:
                for x_inc in range(self._get_x_pos_line_start(), self.preferred_width):
                    self.subwin.addch(
                        self.preferred_height - 3,
                        x_inc,
                        curses.ACS_HLINE,
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )

        except curses.error:
            pass

    def _draw_information_text(self, text):
        try:
            self.subwin.addstr(
                self.preferred_height - 2,
                self._get_x_pos_line_start(),
                GLXCurses.resize_text(text, self.preferred_width - 2),
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                )
            )
        except curses.error:
            pass

    def _draw_information_disk_usage(self):
        # Add Disk usage
        try:
            disk_space_line = GLXCurses.disk_usage(os.getcwd())
            if self.get_decorated():
                self.subwin.addstr(
                    self.preferred_height - 1,
                    self.preferred_width - int(self.border_len / 2) - len(disk_space_line),
                    disk_space_line,
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
            else:
                self.subwin.addstr(
                    self.preferred_height - 1,
                    self.preferred_width - len(disk_space_line),
                    disk_space_line,
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
        except curses.error:
            pass

    def _draw_history_hline(self):
        try:
            if self.is_focus:
                # self.subwin.hline(
                #     self._get_y_pos_history(),
                #     self._get_x_pos_line_start(),
                #     curses.ACS_HLINE,
                #     self._get_x_pos_line_stop(),
                #     self.style.get_color_pair(
                #         foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                #         background=self.style.get_color_text('bg', 'STATE_NORMAL')
                #     )
                # )
                for x_inc in range(self._get_x_pos_line_start(), self._get_x_pos_line_stop()):
                    self.subwin.addch(
                        self._get_y_pos_history(),
                        x_inc,
                        curses.ACS_HLINE,
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        ) | curses.A_NORMAL
                    )

            else:
                for x_inc in range(self._get_x_pos_line_start(), self._get_x_pos_line_stop()):
                    self.subwin.addch(
                        self._get_y_pos_history(),
                        x_inc,
                        curses.ACS_HLINE,
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        ) | curses.A_DIM
                    )
                # self.subwin.hline(
                #     self._get_y_pos_history(),
                #     self._get_x_pos_line_start(),
                #     curses.ACS_HLINE,
                #     self._get_x_pos_line_stop(),
                #     self.style.get_color_pair(
                #         foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                #         background=self.style.get_color_text('bg', 'STATE_NORMAL')
                #     ) | curses.A_DIM
                # )

        except curses.error:
            pass

    def _draw_history_prev(self):
        # History arrow for navigate inside history directory list
        try:
            if self.is_focus:
                self.subwin.addstr(
                    self._get_y_pos_history(),
                    self._get_x_pos_history_prev_label(),
                    "<",
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
            else:
                self.subwin.addstr(
                    self._get_y_pos_history(),
                    self._get_x_pos_history_prev_label(),
                    "<",
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    ) | curses.A_DIM
                )
        except curses.error:
            pass

    def _draw_history_actual_path(self):
        # Path Management
        try:
            spacing = 2
            internal_spacing = 2
            prepend_text = '...'

            label_dir = os.getcwd()
            label_dir = label_dir.replace(os.path.expanduser("~"), "~")
            ce_que_je_retire = self._get_x_pos_history_actual_path_allowed_size()
            ce_que_je_retire -= self._get_x_pos_history_actual_path()
            ce_que_je_retire -= spacing

            if internal_spacing >= 2:
                space_to_add = ' ' * int(internal_spacing / 2)
                label_dir = space_to_add + label_dir + space_to_add

            label_dir = label_dir[-ce_que_je_retire:]

            if ce_que_je_retire > 1:
                self.subwin.addstr(
                    self._get_y_pos_history(),
                    self._get_x_pos_history_actual_path(),
                    str(label_dir),
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('dark', 'STATE_NORMAL'),
                        background=self.style.get_color_text('base', 'STATE_NORMAL')
                    )
                )
                if ce_que_je_retire <= len(label_dir):
                    self.subwin.addstr(
                        self._get_y_pos_history(),
                        self._get_x_pos_history_actual_path(),
                        prepend_text,
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('dark', 'STATE_NORMAL'),
                            background=self.style.get_color_text('base', 'STATE_NORMAL')
                        )
                    )
        except curses.error:
            pass

    def _draw_history_button(self):
        # History button for display the history dialog window
        try:
            if self.is_focus:
                self.subwin.addstr(
                    self._get_y_pos_history(),
                    self._get_x_pos_history_list_label(),
                    ".[^]",
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
            else:
                self.subwin.addstr(
                    self._get_y_pos_history(),
                    self._get_x_pos_history_list_label(),
                    ".[^]",
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    ) | curses.A_DIM
                )
        except curses.error:
            pass

    def _draw_history_next(self):
        # History next arrow for navigate inside history directory list
        try:
            if self.is_focus:
                self.subwin.addstr(
                    self._get_y_pos_history(),
                    self._get_x_pos_history_next_label(),
                    ">",
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
            else:
                self.subwin.addstr(
                    self._get_y_pos_history(),
                    self._get_x_pos_history_next_label(),
                    ">",
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    ) | curses.A_DIM
                )
        except curses.error:
            pass

    def _draw_column_vline_size(self):
        try:
            for y_inc in range(self._get_y_pos_titles(), self.preferred_height - 2):
                self.subwin.delch(
                    y_inc,
                    self.preferred_height - 2
                )
                self.subwin.insch(
                    y_inc,
                    self._get_mtime_collumn_width() - self._get_size_collumn_width(),
                    curses.ACS_VLINE,
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )

            # self.subwin.vline(
            #     self._get_y_pos_titles(),
            #     self._get_mtime_collumn_width() - self._get_size_collumn_width(),
            #     curses.ACS_VLINE,
            #     self.preferred_height - 3,
            #     self.style.get_color_pair(
            #         foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
            #         background=self.style.get_color_text('bg', 'STATE_NORMAL')
            #     )
            # )
        except curses.error:
            pass

    def _draw_column_vline_mtime(self):
        try:
            for y_inc in range(self._get_y_pos_titles(), self.preferred_height - 2):
                self.subwin.delch(
                    y_inc,
                    self.preferred_height - 2
                )
                self.subwin.insch(
                    y_inc,
                    self._get_mtime_collumn_width(),
                    curses.ACS_VLINE,
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('base', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
            # self.subwin.vline(
            #     self._get_y_pos_titles(),
            #     self._get_mtime_collumn_width(),
            #     curses.ACS_VLINE,
            #     self.preferred_height - 3,
            #     self.style.get_color_pair(
            #         foreground=self.style.get_color_text('text', 'STATE_NORMAL'),
            #         background=self.style.get_color_text('bg', 'STATE_NORMAL')
            #     )
            # )
        except curses.error:
            pass

    def _draw_column_title_mtime(self):
        try:
            self.subwin.addstr(
                self._get_y_pos_titles(),
                self._get_x_pos_title_mtime(),
                self.mtime_text,
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                )
            )
        except curses.error:
            pass

    def _draw_column_title_size(self):
        try:
            self.subwin.addstr(
                self._get_y_pos_titles(),
                self._get_x_pos_title_size(),
                self.size_text,
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                )
            )
        except curses.error:
            pass

    def _draw_column_title_name(self):
        try:
            self.subwin.addstr(
                self._get_y_pos_titles(),
                self._get_x_pos_title_name(),
                self.name_text,
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                )
            )
        except curses.error:
            pass
        except TypeError:
            self.subwin.addstr(
                self._get_y_pos_titles(),
                self._get_x_pos_title_name(),
                self.name_text,
                self.style.get_color_pair(
                    foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                    background=self.style.get_color_text('bg', 'STATE_NORMAL')
                )
            )

    def _draw_column_title_sorted_order(self):
        # Verify which short type is selected and display ('n) (,n) ('s) (,s) ('m) (,m)
        try:
            # Check if it have to display ('n) (,n)
            if self.get_sort_by_name():
                if self.get_sort_name_order():
                    self.subwin.addstr(
                        self._get_y_pos_titles(),
                        self._get_x_pos_line_start(),
                        "'",
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )
                else:
                    self.subwin.addstr(
                        self._get_y_pos_titles(),
                        self._get_x_pos_line_start(),
                        ",",
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )
                self.subwin.addstr(
                    self._get_y_pos_titles(),
                    self._get_x_pos_line_start() + 1,
                    str(self.sort_name_letter),
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
            # Check if it have to display ('s) (,s)
            elif self.get_sort_by_size():
                if self.get_sort_size_order():
                    self.subwin.addstr(
                        self._get_y_pos_titles(),
                        self._get_x_pos_line_start(),
                        "'",
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )
                else:
                    self.subwin.addstr(
                        self._get_y_pos_titles(),
                        self._get_x_pos_line_start(),
                        ",",
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )
                self.subwin.addstr(
                    self._get_y_pos_titles(),
                    self._get_x_pos_line_start() + 1,
                    str(self.sort_size_letter),
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
            # Check if it have to display ('m) (,m)
            elif self.get_sort_by_mtime():
                if self.get_sort_mtime_order():
                    self.subwin.addstr(
                        self._get_y_pos_titles(),
                        self._get_x_pos_line_start(),
                        ",",
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )

                else:
                    self.subwin.addstr(
                        self._get_y_pos_titles(),
                        self._get_x_pos_line_start(),
                        "'",
                        self.style.get_color_pair(
                            foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                            background=self.style.get_color_text('bg', 'STATE_NORMAL')
                        )
                    )

                self.subwin.addstr(
                    self._get_y_pos_titles(),
                    self._get_x_pos_line_start() + 1,
                    str(self.sort_mtime_letter),
                    self.style.get_color_pair(
                        foreground=self.style.get_color_text('mid', 'STATE_NORMAL'),
                        background=self.style.get_color_text('bg', 'STATE_NORMAL')
                    )
                )
        except curses.error:
            pass

    def _set_item_list(self, file_list=None):
        """
        Set the files list, internally use for list directory.

        Note that item_list=None will reset the list

        :param file_list: a file list
        :type file_list: list
        :raise TypeError: when ``item_list`` argument is not a list or None
        """
        # Reset the list in case that None
        if file_list is None:
            file_list = list()

        # Exit as soon of possible
        if type(file_list) != list:
            raise TypeError("'item_list' must be a list type")

        # just in case it make teh job
        if self._get_item_list() != file_list:
            self.item_list = file_list

    def _get_item_list(self):
        """
        Set the files list.

        Note tha can't be None, that because _set_file_list() set a empty list.

        :return: the file list, internally use for list directory
        :rtype: list
        """
        return self.item_list

    def _set_item_info_list(self, list_item_info=None):
        """
        Set a item info list, internally use for store information about each item in a directory.

        Note that item_info_list=None will reset the list

        :param list_item_info: a file list
        :type list_item_info: list
        :raise TypeError: when ``item_info_list`` argument is not a list or None
        """
        # Reset the list in case that None
        if list_item_info is None:
            list_item_info = list()

        # Exit as soon of possible
        if type(list_item_info) != list:
            raise TypeError("'item_info_list' must be a list type")

        # just in case it make teh job
        if self._get_item_info_list() != list_item_info:
            self.item_info_list = list_item_info

    def _get_item_info_list(self):
        """
        Set the files list.

        Note tha can't be None, that because _set_file_list() set a empty list.

        :return: the file list, internally use for list directory
        :rtype: list
        """
        return self.item_info_list

    def _set_item_it_can_be_display(self, value=0):
        """
        Get the number of item it can be display

        :param value: the number of item it can be display
        :type value: int
        :raise TypeError: when ``value`` argument is not a int
        """
        # Exit as soon of possible
        if type(value) != int:
            raise TypeError("'value' must be a int type")

        # just in case it make teh job
        if self._get_item_it_can_be_display() != value:
            self.item_it_can_be_display = value

    def _get_item_it_can_be_display(self):
        """
        Get the number of item it can be display, as set by _set_item_it_can_be_display().

        :return: The number of item it can be display
        :rtype: int
        """
        return self.item_it_can_be_display

    def _set_item_scroll_pos(self, value=None):
        """
        Position on the scroll list. value=None for reset to 0.

        Default 0

        :param value: the position
        :type value: int or None
        :raise TypeError: when ``value`` argument is not a int or None
        """
        if value is None:
            value = 0

        # Exit as soon of possible
        if type(value) != int:
            raise TypeError("'value' must be a int type")

        # just in case it make teh job
        if self._get_item_scroll_pos() != value:
            self.item_scroll_pos = value

    def _get_item_scroll_pos(self):
        """
        Get the number of item it can be display, as set by _set_item_it_can_be_display().

        :return: The Position on the scroll list
        :rtype: int
        """
        return self.item_scroll_pos

    def _get_item_info(self, file_path):
        """
        Return information list about a file pass as argument

        Index position and description:
            0 - Name to Display
            1 - Full Path
            2 - Size to Display
            3 - Time to Display
            4 - Size value used by the shorted process
            5 - Mtime value used by the shorted process
            6 - Small symbol
            7 - Color
            8 - Color_add

        :param file_path: a filename path
        :type file_path: str
        :return: a list with information's
        :raise TypeError: when ``file_path`` argument is not a :py:__area_data:`string`
        :raise IOError: when ``file_path`` does not exist
        """
        # Exit as soon of possible
        if type(file_path) != str:
            raise TypeError("'file_path' must be a str type")

        # if not os.path.exists(os.path.realpath(file_path)):
        #     raise FileNotFoundError("'%s' do not exist" % file_path)

        # 0 Name to Display
        if os.path.islink(file_path):
            name_to_display = os.path.basename(file_path) + ' -> ' + os.readlink(file_path)
        else:
            name_to_display = os.path.basename(file_path)

        # 1 Full Path
        full_path = os.path.abspath(file_path)

        # 2 Size to Display
        if os.path.basename(file_path) == "..":
            size_to_display = "UP--DIR"
        elif os.path.islink(file_path):
            st = os.lstat(file_path)
            size = GLXCurses.sizeof(st.st_size)
            size_to_display = size
        else:
            if os.path.isfile(file_path):
                st = os.lstat(file_path)
                size = GLXCurses.sizeof(st.st_size)
                size_to_display = size
            else:
                try:
                    x = os.statvfs(file_path)
                    size_to_display = x.f_bsize
                except OSError:
                    size_to_display = "ERROR"

        # 3 Time to Display
        try:
            st = os.lstat(file_path)
            time_to_display = time.strftime("%d/%m/%Y  %H:%M", time.localtime(st.st_mtime))
        except OSError:
            time_to_display = 'ERROR'

        # 4 Size value used by the shorted process
        try:
            st = os.lstat(file_path)
            size_value_to_order = st.st_size
        except OSError:
            size_value_to_order = 'ERROR'

        # 5 Mtime value used by the shorted process
        try:
            st = os.lstat(file_path)
            mtime_value_to_order = st.st_mtime
        except OSError:
            mtime_value_to_order = "ERROR"

        # 6 - Small symbol
        # 7 - Color
        # 8 - Color_add
        small_symbol = ' '
        color = 'GRAY'
        color_add = curses.A_NORMAL
        if os.path.islink(file_path):
            if not os.path.exists(file_path):
                small_symbol = '!'
                color = 'RED'
                color_add = curses.A_BOLD
                if self.get_app_file_extensions() is not None:
                    if file_path.endswith(self.get_app_file_extensions()):
                        color = 'RED'
                        color_add = curses.A_BOLD
                    else:
                        color = 'GRAY'
                        color_add = curses.A_BOLD | curses.A_DIM
            else:
                small_symbol = '@'
                if self.get_app_file_extensions() is not None:
                    if file_path.endswith(self.get_app_file_extensions()):
                        color_add = curses.A_NORMAL
                    else:
                        color_add = curses.A_DIM
        elif os.path.isfile(file_path):
            if os.access(file_path, os.X_OK):
                small_symbol = '*'
                color = 'GREEN'
                color_add = curses.A_BOLD
                if self.get_app_file_extensions() is not None:
                    if file_path.endswith(self.get_app_file_extensions()):
                        color = 'GREEN'
                        color_add = curses.A_BOLD
                    else:
                        color = 'GRAY'
                        color_add = curses.A_BOLD | curses.A_DIM
            else:
                small_symbol = ' '
                if self.get_app_file_extensions() is not None:
                    if file_path.endswith(self.get_app_file_extensions()):
                        color_add = curses.A_NORMAL
                    else:
                        color_add = curses.A_DIM

        elif os.path.isdir(file_path):
            small_symbol = os.path.sep
            color = 'WHITE'
            color_add = curses.A_NORMAL

        # Yes it return something, it's a live !
        file_info_list = list()
        file_info_list.append(name_to_display)
        file_info_list.append(full_path)
        file_info_list.append(size_to_display)
        file_info_list.append(time_to_display)
        file_info_list.append(size_value_to_order)
        file_info_list.append(mtime_value_to_order)
        file_info_list.append(small_symbol)
        file_info_list.append(color)
        file_info_list.append(color_add)
        return file_info_list

    def _set_selected_item_pos(self, value=None):
        """
        Position of the selected item in parallel of the scroll list.

        value=None for reset to 0.

        Default: 0

        :param value: the position
        :type value: int or None
        :raise TypeError: when ``value`` argument is not a int or None
        """
        if value is None:
            value = 0

        # Exit as soon of possible
        if type(value) != int:
            raise TypeError("'value' must be a int type")

        # just in case it make teh job
        if self._get_selected_item_pos() != value:
            self.selected_item_pos = value

    def _get_selected_item_pos(self):
        """
        Position of the selected item.

        :return: The Position on the scroll list
        :rtype: int
        """
        return self.selected_item_pos

    def _set_selected_item_info_list(self, file_info_list=None):
        """
        Set the files list, internally use for list directory.

        The file_info_list information's store position:
            item_name_text in position [0]
            item_path_sys in position [1])
            item_size_text in position [2]
            item_time_text in position [3]

        :param file_info_list: a file list
        :type file_info_list: list
        :raise TypeError: when ``file_info_list`` argument is not a list or None
        """
        # Reset the list in case that None
        if file_info_list is None:
            file_info_list = list()

        # Exit as soon of possible
        if type(file_info_list) != list:
            raise TypeError("'file_info_list' must be a list type")

        # just in case it make teh job
        if self._get_selected_item_info_list() != file_info_list:
            self.selected_item_info_list = file_info_list

    def _get_selected_item_info_list(self):
        """
        Get the selected file information's list.

        The file_info_list information's store position:
            item_name_text in position [0]
            item_path_sys in position [1])
            item_size_text in position [2]
            item_time_text in position [3]

        :return: information's about selected item.
        :rtype: list
        """
        return self.selected_item_info_list

    def _update_preferred_sizes(self):
        self.preferred_width = self._get_estimated_preferred_width()
        self.preferred_height = self._get_estimated_preferred_height()

        # it_can_be_display
        # what is 5 or 4 ????
        self._set_item_it_can_be_display(self.preferred_height - 5)

    def _get_estimated_preferred_width(self):
        """
        Estimate a preferred width, by consider X Location, allowed width (No need on FileChooser)

        :return: a estimated preferred width
        :rtype: int
        """
        return self.width

    def _get_estimated_preferred_height(self):
        """
        Estimate a preferred height, by consider Y Location (No need on FileChooser)

        :return: a estimated preferred height
        :rtype: int
        """
        return self.height

    def _check_selected(self):
        if self.can_focus:
            if isinstance(GLXCurses.Application().has_focus, GLXCurses.GLXCChildElement):
                if GLXCurses.Application().has_focus.id == self.id:
                    self.is_focus = True
                    self._update_preferred_sizes()

            else:
                self.is_focus = False
                self._update_preferred_sizes()

        else:
            pass

    def _grab_focus(self):
        """
        Internal method, for Select the contents of the Entry it take focus.

        See: grab_focus_without_selecting ()
        """
        if isinstance(GLXCurses.Application().has_focus, GLXCurses.GLXCChildElement):
            if GLXCurses.Application().has_focus.id != self.id:
                GLXCurses.Application().has_focus = self

    def _scroll_up(self):
        if not self._get_selected_item_pos() == 0:
            self._set_selected_item_pos(self._get_selected_item_pos() - 1)
        else:
            if not self._get_item_scroll_pos() == 0:
                self._set_item_scroll_pos(self._get_item_scroll_pos() - 1)

    def _scroll_down(self):
        if not (self._get_item_it_can_be_display() - 1) == self._get_selected_item_pos():
            if not self.selected_item_pos == len(self._get_item_list()) - 1:
                self._set_selected_item_pos(self._get_selected_item_pos() + 1)
        else:
            a = self._get_item_scroll_pos() + (self._get_item_it_can_be_display() - 1) + 1
            if a < len(self._get_item_list()) <= len(self._get_item_list()):
                self._set_item_scroll_pos(self._get_item_scroll_pos() + 1)

    def _history_scroll_up(self):
        if not self.history_menu_selected_item == 0:
            self.history_menu_selected_item -= 1
        else:
            if not self.history_menu_item_list_scroll == 0:
                self.history_menu_item_list_scroll -= 1

    def _history_scroll_down(self):
        if not self.history_menu_can_be_display == self.history_menu_selected_item \
                and not self.history_menu_selected_item + 1 == len(self.history_dir_list) \
                and not len(self.history_dir_list) == 0:
            self.history_menu_selected_item += 1
        else:
            if self.history_menu_item_list_scroll + self.history_menu_can_be_display < self.history_menu_item_number + 1:
                self.history_menu_item_list_scroll += 1

    def _handle_key_event(self, event_signal, *event_args):
        # Check if we have to care about keyboard event
        if self.sensitive and \
                isinstance(GLXCurses.Application().has_focus, GLXCurses.GLXCChildElement) and \
                GLXCurses.Application().has_focus.id == self.id:
            # setting
            key = event_args[0]

            if not self.display_history_menu == 1:
                # Touch Escape
                if key == GLXCurses.GLXC.KEY_ESC:
                    GLXCurses.Application().has_focus = None
                    self.is_focus = False
                    self.has_focus = False
                    self._check_selected()

                if key == curses.KEY_UP:
                    logging.debug(str(time.time() - self.time_last_scroll_up))
                    if time.time() - self.time_last_scroll_up > 0.10:
                        self._scroll_up()
                    elif 0.06 >= time.time() - self.time_last_scroll_up > 0.0:
                        self._scroll_up()
                        self._scroll_up()

                    self.time_last_scroll_up = time.time()

                if key == curses.KEY_DOWN:
                    logging.debug(str(time.time() - self.time_last_scroll_down))
                    if time.time() - self.time_last_scroll_down > 0.06:
                        self._scroll_down()
                    elif 0.06 >= time.time() - self.time_last_scroll_down > 0.0:
                        self._scroll_down()
                        self._scroll_down()

                    self.time_last_scroll_down = time.time()

                if key == curses.KEY_HOME:
                    self._set_selected_item_pos(0)
                    self._set_item_scroll_pos(0)

                # END Touch
                if key == curses.KEY_END:
                    # Scroll to down like curses.KEY_DOWN via a loop it have the len of item in directory,
                    for line_number in range(0, len(self._get_item_list())):
                        self._scroll_down()

                if key == curses.KEY_NPAGE:
                    for line_number in range(0, self._get_item_it_can_be_display() - 1):
                        self._scroll_down()

                if key == curses.KEY_PPAGE:
                    for line_number in range(0, self._get_item_it_can_be_display() - 1):
                        self._scroll_up()

                if key == ord("n"):
                    self.set_sort_by_name(True)
                    self.set_sort_by_size(False)
                    self.set_sort_by_mtime(False)
                    self.set_sort_name_order(not self.get_sort_name_order())

                if key == ord("s"):
                    self.set_sort_by_name(False)
                    self.set_sort_by_size(True)
                    self.set_sort_by_mtime(False)
                    self.set_sort_size_order(not self.get_sort_size_order())

                if key == ord("t"):
                    self.set_sort_by_name(False)
                    self.set_sort_by_size(False)
                    self.set_sort_by_mtime(True)
                    self.set_sort_mtime_order(not self.get_sort_mtime_order())

                if key == ord("h"):
                    self.display_history_menu = not self.display_history_menu

                if key == curses.KEY_ENTER or key == ord("\n"):

                    # We gat the line go do something
                    if os.path.isdir(self._get_selected_item_info_list()[1]):
                        os.chdir(os.path.join(os.getcwd(), self._get_selected_item_info_list()[1]))

                        self._set_selected_item_pos(0)
                        self._set_item_scroll_pos(0)

                        found = 0
                        for item in self.history_dir_list:
                            if item == os.getcwd():
                                found = 1
                        if not found == 1:
                            self.history_dir_list.append(os.getcwd())

                    else:
                        pass

            # When history i display enable special shortcut
            elif self.display_history_menu == 1:
                if key == GLXCurses.GLXC.KEY_ESC:
                    # Escape was pressed
                    self.display_history_menu = not self.display_history_menu

                elif key == curses.KEY_UP:
                    self._history_scroll_up()

                elif key == curses.KEY_DOWN:
                    self._history_scroll_down()

                elif key == curses.KEY_ENTER or key == ord("\n"):
                    self.display_history_menu = not self.display_history_menu
                    if os.path.isdir(self.history_menu_selected_item_value):
                        os.chdir(self.history_menu_selected_item_value)
                        # self.window_source_pwd = os.getcwd()
                        self.selected_item = 0
                        self.item_list_scroll = 0

                elif key == ord("h"):
                    self.display_history_menu = not self.display_history_menu

            # Create a Dict with everything
            instance = {
                'class': self.__class__.__name__,
                'id': self.id,
                'event_signal': event_signal
            }
            # EVENT EMIT
            # Application().emit(self.curses_mouse_states[event], instance)
            self.emit(str(key), instance)

    def _handle_mouse_event(self, event_signal, event_args):
        if self.sensitive:
            (mouse_event_id, x, y, z, event) = event_args

            # Be sure we select really the Button
            y -= self.y
            x -= self.x
            that_for_me = (0 <= y <= self.preferred_height - 1 and 0 <= x <= self.preferred_width - 1)

            if that_for_me:

                self._grab_focus()
                # self._check_selected()
                # We are sure about the FileChooser have been clicked
                # self.states_list = '; '.join(state_string for state, state_string
                #                              in self.curses_mouse_states.viewitems()
                #                              if event & state)

                # First line Prev / Next / History
                if y == 0:
                    if self._get_x_pos_history_prev_label() <= x <= self._get_x_pos_history_prev_label():
                        # logging.debug('x:' + str(x) + " y:" + str(y))
                        if not self.history_menu_selected_item == 0:
                            self.history_menu_selected_item -= 1

                        if os.path.isdir(
                                self.history_dir_list[self.history_menu_selected_item]):
                            os.chdir(
                                self.history_dir_list[self.history_menu_selected_item])

                            self.selected_item_pos = 0
                            self.item_scroll_pos = 0

                    if self._get_x_pos_history_list_label() <= x <= self._get_x_pos_history_list_label() - 1 + len(
                            self.history_button_text_list):
                        self.display_history_menu = not self.display_history_menu

                    if self._get_x_pos_history_next_label() <= x <= self._get_x_pos_history_next_label():
                        if len(self.history_dir_list) > self.history_menu_selected_item + 1:
                            self.history_menu_selected_item += 1
                            if os.path.isdir(
                                    self.history_dir_list[self.history_menu_selected_item]):
                                os.chdir(
                                    self.history_dir_list[self.history_menu_selected_item])

                                self.selected_item_pos = 0
                                self.item_scroll_pos = 0
                # Titles
                if y == self._get_y_pos_titles():
                    x_pos_name_start = self._get_x_pos_title_name() - self.x - 1
                    if x_pos_name_start <= x <= self._get_x_pos_title_name() + len(self.name_text) - 1:
                        self.set_sort_by_name(True)
                        self.set_sort_by_size(False)
                        self.set_sort_by_mtime(False)
                        self.set_sort_name_order(not self.get_sort_name_order())
                    if self._get_x_pos_title_size() <= x <= self._get_x_pos_title_size() + len(self.size_text) - 1:
                        self.set_sort_by_name(False)
                        self.set_sort_by_size(True)
                        self.set_sort_by_mtime(False)
                        self.set_sort_size_order(not self.get_sort_size_order())
                    if self._get_x_pos_title_mtime() <= x <= self._get_x_pos_title_mtime() + len(
                            self.mtime_text) - 1:
                        self.set_sort_by_name(False)
                        self.set_sort_by_size(True)
                        self.set_sort_by_mtime(False)
                        self.set_sort_size_order(not self.get_sort_size_order())

                # Mouse weel
                if self._get_y_pos_titles() + 1 <= y <= self.preferred_height - 3 \
                        and event != 524288 and event != 134217728 and event != curses.BUTTON4_PRESSED:
                    clicked_line = y - self._get_y_pos_titles() - 1
                    if 0 <= x <= self.preferred_width - 1:

                        if event == curses.BUTTON1_DOUBLE_CLICKED:
                            # Selected the line
                            if clicked_line <= len(self._get_item_list()):
                                value = clicked_line
                            else:
                                value = len(self._get_item_list()) - 1

                            self._set_selected_item_pos(value)
                            self._set_item_scroll_pos(value)
                            # self._get_item_info(
                            #     self.item_list[self._get_item_scroll_pos()],
                            # )
                            self._set_selected_item_info_list(self._get_item_info(
                                self.item_list[self._get_item_scroll_pos()],
                            )
                            )
                            # We got the line and do something
                            if os.path.isdir(self._get_selected_item_info_list()[1]):
                                os.chdir(os.path.join(os.getcwd(), self._get_selected_item_info_list()[0]))

                                self._set_selected_item_pos(0)
                                self._set_item_scroll_pos(0)

                                # Update history List
                                found = 0
                                for item in self.history_dir_list:
                                    if item == os.getcwd():
                                        found = 1
                                if not found == 1:
                                    self.history_dir_list.append(os.getcwd())

                            else:
                                pass

                        if event == curses.BUTTON1_CLICKED or event == curses.BUTTON1_PRESSED:
                            if clicked_line <= len(self._get_item_list()):
                                self._set_selected_item_pos(clicked_line)
                            else:
                                # Scroll to down like curses.KEY_DOWN via a loop
                                # it have the len of item in directory,
                                for line_number in range(0, len(self._get_item_list())):
                                    self._scroll_down()

                if event == 524288 or event == 65536:
                    if not self.display_history_menu == 1:
                        if not self.display_history_menu == 1:
                            # logging.debug(str(time.time() - self.time_last_scroll_up))
                            if time.time() - self.time_last_scroll_up > 0.10:
                                self._scroll_up()
                            elif 0.10 >= time.time() - self.time_last_scroll_up > 0.05:
                                self._scroll_up()
                                self._scroll_up()
                            elif 0.05 >= time.time() - self.time_last_scroll_up > 0.025:
                                self._scroll_up()
                                self._scroll_up()
                                self._scroll_up()
                                self._scroll_up()
                            elif 0.025 >= time.time() - self.time_last_scroll_up > 0.0:
                                self._scroll_up()
                                self._scroll_up()
                                self._scroll_up()
                                self._scroll_up()
                                self._scroll_up()
                                self._scroll_up()
                                self._scroll_up()
                                self._scroll_up()

                            self.time_last_scroll_up = time.time()
                    else:
                        self._history_scroll_up()

                if event == 134217728 or event == 2097152:
                    if not self.display_history_menu == 1:
                        # logging.debug(str(time.time() - self.time_last_scroll_down))
                        if time.time() - self.time_last_scroll_down > 0.10:
                            self._scroll_down()
                        elif 0.10 >= time.time() - self.time_last_scroll_down > 0.05:
                            self._scroll_down()
                            self._scroll_down()
                        elif 0.05 >= time.time() - self.time_last_scroll_down > 0.025:
                            self._scroll_down()
                            self._scroll_down()
                            self._scroll_down()
                            self._scroll_down()
                        elif 0.025 >= time.time() - self.time_last_scroll_down > 0.0:
                            self._scroll_down()
                            self._scroll_down()
                            self._scroll_down()
                            self._scroll_down()
                            self._scroll_down()
                            self._scroll_down()
                            self._scroll_down()
                            self._scroll_down()

                        self.time_last_scroll_down = time.time()
                    else:
                        self._history_scroll_down()

                # INTERNAL METHOD
                if event == curses.BUTTON1_PRESSED:
                    pass

                elif event == curses.BUTTON1_RELEASED:
                    pass

                if event == curses.BUTTON1_CLICKED:
                    pass

                if event == curses.BUTTON1_DOUBLE_CLICKED:
                    pass

                if event == curses.BUTTON1_TRIPLE_CLICKED:
                    pass

                # BUTTON2
                if event == curses.BUTTON2_PRESSED:
                    pass

                elif event == curses.BUTTON2_RELEASED:
                    pass

                if event == curses.BUTTON2_CLICKED:
                    pass

                if event == curses.BUTTON2_DOUBLE_CLICKED:
                    pass

                if event == curses.BUTTON2_TRIPLE_CLICKED:
                    pass

                # BUTTON3
                if event == curses.BUTTON3_PRESSED:
                    pass

                elif event == curses.BUTTON3_RELEASED:
                    pass

                if event == curses.BUTTON3_CLICKED:
                    pass

                if event == curses.BUTTON3_DOUBLE_CLICKED:
                    pass

                if event == curses.BUTTON3_TRIPLE_CLICKED:
                    pass

                # BUTTON4
                if event == curses.BUTTON4_PRESSED:
                    pass

                elif event == curses.BUTTON4_RELEASED:
                    pass

                if event == curses.BUTTON4_CLICKED:
                    pass

                if event == curses.BUTTON4_DOUBLE_CLICKED:
                    pass

                if event == curses.BUTTON4_TRIPLE_CLICKED:
                    pass

                if event == curses.BUTTON_SHIFT | curses.BUTTON1_CLICKED:
                    pass
                if event == curses.BUTTON_CTRL:
                    pass
                if event == curses.BUTTON_ALT:
                    pass

                # Create a Dict with everything
                instance = {
                    'class': self.__class__.__name__,
                    'id': self.id,
                    'event_signal': event_signal
                }
                # EVENT EMIT
                # Application().emit(self.curses_mouse_states[event], instance)
                self.emit(self.curses_mouse_states[event], instance)
            else:
                # The widget is not selected
                self.is_focus = False
                self.has_focus = False
                self._check_selected()
        else:
            if self.debug:
                logging.debug('{0} -> id:{1}, object:{2}, is not sensitive'.format(
                    self.__class__.__name__,
                    self.id,
                    self
                ))

    def _get_x_pos_history_next_label(self):
        if self.get_decorated():
            return int(self.preferred_width - 1 - int(self.border_len / 2))
        else:
            return int(self.preferred_width - 1)

    def _get_x_pos_history_list_label(self):
        return int(self._get_x_pos_history_next_label() - len(self.history_button_text_list))

    def _get_x_pos_history_prev_label(self):
        if self.get_decorated():
            return int(0 + int(self.border_len / 2))
        else:
            return int(0)

    def _get_x_pos_history_actual_path(self):
        return int(self._get_x_pos_history_prev_label() + len(self.history_button_text_prev) + 1)

    def _get_x_pos_history_actual_path_allowed_size(self):
        return int(self._get_x_pos_history_next_label() - self._get_x_pos_history_actual_path())

    def _get_x_pos_title_mtime(self):
        return int((self._get_mtime_collumn_width() + 1) + (
                (len(str(self.mtime_text)) - 1) / 2) - 4)

    def _get_x_pos_title_size(self):
        return int(((self._get_mtime_collumn_width() - self._get_size_collumn_width()) + 1) + (
                (len(self.size_text) - 1) / 2))

    def _get_x_pos_title_name(self):
        return int(((self._get_mtime_collumn_width() - self._get_size_collumn_width()) / 2) - (
                len(self.name_text) / 2) + 1)

    def _get_x_pos_line_start(self):
        if self.get_decorated():
            return int(0 + int(self.border_len / 2))
        else:
            return int(0)

    def _get_x_pos_line_stop(self):
        if self.get_decorated():
            return int(self.preferred_width - 1 - int(self.border_len / 2) - 1)
        else:
            return int(self.preferred_width - 1 - 1)

    def _get_y_pos_history(self):
        return int(0)

    def _get_y_pos_titles(self):
        return int(self._get_y_pos_history() + 1)

    def _get_y_pos_items(self):
        return int(self._get_y_pos_titles() + 1)

    def _get_name_collumn_width(self):
        if self.get_decorated():
            name_collumn_width = self.preferred_width
            name_collumn_width -= 16
            name_collumn_width -= self._get_size_collumn_width()
            name_collumn_width -= 2
            name_collumn_width -= self.border_len
        else:
            name_collumn_width = self.preferred_width
            name_collumn_width -= 16
            name_collumn_width -= self._get_size_collumn_width()
            name_collumn_width -= 2
        return int(name_collumn_width)

    def _get_mtime_collumn_width(self):
        if self.get_decorated():
            mtime_collumn_width = self.preferred_width - 1 - int(self.border_len / 2)
            mtime_collumn_width -= len(time.strftime("%d/%m/%Y  %H:%M", time.localtime(time.time())))
        else:
            mtime_collumn_width = self.preferred_width - 1
            mtime_collumn_width -= len(time.strftime("%d/%m/%Y  %H:%M", time.localtime(time.time())))
        return int(mtime_collumn_width)

    @staticmethod
    def _get_size_collumn_width():
        size_collumn_width = 8
        return int(size_collumn_width)
