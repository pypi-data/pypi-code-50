#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

# Inspired by: https://developer.gnome.org/gtk3/stable/gtk3-GtkWidgetPath.html
# Inspired by: https://gitlab.gnome.org/GNOME/gtk/blob/master/gtk/gtkwidgetpath.c
# Inspired by: https://github.com/linuxmint/gtk/blob/master/gtk/gtkwidgetpath.c

from GLXCurses.Utils import new_id
from GLXCurses.Utils import glxc_type
from GLXCurses.Utils import clamp_to_zero
from GLXCurses.Constants import GLXC
from yaml import dump


class WidgetPath(object):
    def __init__(self):
        """
        Widget path abstraction
        """
        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.WidgetPath'

        # Unique ID it permit to individually identify a widget by example for get_focus get_default
        self.id = new_id()
        self.name = '{0}{1}'.format(self.__class__.__name__, self.id)

        # Public Property
        # First element contains the described widget
        self.elems = list()
        self.ref_count = 1

    @staticmethod
    def new():
        """
        Returns an empty widget path.

        :return: A newly created, empty WidgetPath
        :rtype: WidgetPath
        """
        path = WidgetPath()
        path.elems = list()
        path.elems.append(GLXCPathElement())
        path.ref_count = 1
        path.sibling_index = 0
        path.siblings = WidgetPath()

        return path

    @staticmethod
    def element_copy(dest, src):
        """
        Copy elements from a GLXCPathElement to a other GLXCPathElement

        :param dest: GLXCPathElement where copy elements
        :type dest: GLXCPathElement
        :param src: GLXCPathElement from where copy elements
        :type src: GLXCPathElement
        :raise TypeError: if ``dest`` is not a instance of GLXCPathElement.
        :raise TypeError: if ``src`` is not a instance of GLXCPathElement.
        """

        if not isinstance(dest, GLXCPathElement):
            raise TypeError("'dest' must be an instance of GLXCPathElement")

        if not isinstance(src, GLXCPathElement):
            raise TypeError("'src' must be an instance of GLXCPathElement")

        dest.type = src.type
        dest.name = src.name
        dest.state = src.state

        if bool(src.siblings):
            dest.siblings = src.siblings
        dest.sibling_index = src.sibling_index

        if bool(src.regions):
            dest.regions = src.regions
            # dest.regions = list()
            # for region in src.regions:
            #     for key, value in region:
            #         dest.regions.append({key, value})

        if bool(src.classes):
            dest.classes = src.classes
            # dest.classes = list()
            # for the_class in src.classes:
            #     for key, value in the_class:
            #         dest.classes.append({key, value})

    @staticmethod
    def copy(path):
        """
        Returns a copy of ``path``

        :param path: WidgetPath to copy
        :type path: WidgetPath
        :return: A newly created, with elements copy from path
        :rtype: WidgetPath
        :raise TypeError: if ``path`` is not a instance of WidgetPath.
        """
        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of WidgetPath")

        new_path = WidgetPath().new()
        new_path.elems = path.elems

        return new_path

    @staticmethod
    def ref(path):
        """
        Increments the reference count on ``path``.

        :param path: a WidgetPath where increment reference count
        :type path: WidgetPath
        :return: path itself.
        :rtype: WidgetPath
        :raise TypeError: if ``path`` is not a GLXCurses thing.
        :raise TypeError: if ``path`` is not a instance of WidgetPath.
        """
        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        path.ref_count += 1

        return path

    @staticmethod
    def unref(path):
        """
        Decrements the reference count on @path, freeing the structure if the reference count reaches 0.

        :param path: a WidgetPath where decrement reference count
        :type path: WidgetPath
        :raise TypeError: if ``path`` is not a GLXCurses thing.
        :raise TypeError: if ``path`` is not a instance of WidgetPath.
        """
        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        path.ref_count -= 1
        path.ref_count = clamp_to_zero(path.ref_count)

        if path.ref_count > 0:
            return
        else:
            path.elems = list()

    def free(self, path):
        """
        Decrements the reference count on @path, freeing the structure if the reference count reaches 0.

        :param path: a WidgetPath where decrement reference count
        :type path: WidgetPath
        :raise TypeError: if ``path`` is not a GLXCurses thing.
        :raise TypeError: if ``path`` is not a instance of WidgetPath.
        """
        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        self.unref(path)

    @staticmethod
    def length(path):
        """
        Returns the number of #GtkWidget #GTypes between the represented widget and its topmost container.

        :param path: a WidgetPath where decrement reference count
        :type path: WidgetPath
        :return: the number of elements in the path
        :rtype: int
        :raise TypeError: if ``path`` is not a GLXCurses thing.
        :raise TypeError: if ``path`` is not a instance of WidgetPath.
        """
        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        return len(path.elems)

    @staticmethod
    def to_string(path):
        """
        Dumps the widget path into a string representation. CSS is not use on GLXCurses, then the style use is YAML.
        The dump is done by use yaml.dump(path.elems).


        :param path: a WidgetPath where decrement reference count
        :type path: WidgetPath
        :return: A new string describing ``path`` in pure YAML Style.
        :rtype: str
        :raise TypeError: if ``path`` is not a GLXCurses thing.
        :raise TypeError: if ``path`` is not a instance of WidgetPath.
        """
        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        return dump(path.elems)

    @staticmethod
    def prepend_type(path, widget_type):
        """
        Prepends a widget type to the widget hierarchy represented by ``path``.

        :param path: a WidgetPath or None for self
        :type path: WidgetPath or None
        :param widget_type: widget type to append
        :type widget_type: str
        :raise TypeError: if ``widget_type`` is not a GLXC.Type type or None.
        :raise TypeError: if ``path`` is not a valid GLXCurses type.
        :raise TypeError: if ``path`` is not a instance of GLXCurses.WidgetPath.
        """
        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        if widget_type not in GLXC.Type:
            raise TypeError("'widget_type' must be an valid of GLXCurses.Type")

        # We make the job
        path_element = GLXCPathElement()
        path_element.type = widget_type
        path.elems.insert(0, path_element)

    @staticmethod
    def append_type(path, widget_type):
        """
        Appends a widget type to the widget hierarchy represented by ``path``.

        :param path: a WidgetPath or None for self
        :type path: WidgetPath or None
        :param widget_type: widget type to append
        :type widget_type: str
        :return: the position where the element was inserted
        :rtype: int
        :raise TypeError: if ``widget_type`` is not a GLXC.Type type or None.
        :raise TypeError: if ``path`` is not a valid GLXCurses type.
        :raise TypeError: if ``path`` is not a instance of GLXCurses.WidgetPath.
        """
        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        if widget_type not in GLXC.Type:
            raise TypeError("'widget_type' must be an valid of GLXCurses.Type")

        # We make the job
        path_element = GLXCPathElement()
        path_element.type = widget_type
        path.elems.append(path_element)

        return len(path.elems) - 1

    @staticmethod
    def append_with_siblings(path, siblings, sibling_index):
        """
        Appends a widget type with all its siblings to the widget hierarchy represented by path .
        Using this function instead of WidgetPath.append_type() will allow the YAML theming to use sibling matches
        in selectors and apply :nth-child() pseudo classes.
        In turn, it requires a lot more care in widget implementations as widgets
        need to make sure to call GLXCurses.Widget.reset_style() on all involved widgets when the ``siblings``
        path changes.

        :param path: the widget path to append to
        :type path: WidgetPath
        :param siblings: a widget path describing a list of siblings. \
        This path may not contain any siblings itself and it must not be modified afterwards.
        :type siblings: WidgetPath
        :param sibling_index: index into siblings for where the added element is positioned.
        :type sibling_index: int
        :return: the position where the element was inserted.
        :rtype: int
        :raise TypeError: if ``path`` is not a valid GLXCurses type.
        :raise TypeError: if ``path`` is not a instance of GLXCurses.WidgetPath.
        :raise TypeError: if ``siblings`` is not a valid GLXCurses type.
        :raise TypeError: if ``siblings`` is not a instance of GLXCurses.WidgetPath.
        :raise TypeError: if ``sibling_index`` is not a int.
        """
        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        if not glxc_type(siblings):
            raise TypeError("'siblings' must be a GLXCurses type")

        if not isinstance(siblings, WidgetPath):
            raise TypeError("'siblings' must be an instance of GLXCurses.WidgetPath")

        if type(sibling_index) != int:
            raise TypeError("'sibling_index' must be a int type")

        if sibling_index < siblings.length(siblings):
            raise ValueError("'sibling_index' must be superior to siblings.length(siblings)")

        # We make the job
        new = GLXCPathElement()
        sibling_index = clamp_to_zero(sibling_index - 1)
        path.element_copy(new, siblings.elems[sibling_index])

        new.siblings = WidgetPath()
        new.siblings.elems.append(siblings.elems[sibling_index])

        new.siblings.ref(siblings)

        new.sibling_index = sibling_index

        path.elems.append(new)

        return len(path.elems) - 1

    @staticmethod
    def iter_get_siblings(path, pos):
        """
        Returns the list of siblings for the element at ``pos``.
        If the element was not added with siblings, None is returned.

        :return: None or the list of siblings for the element at ``pos``.
        :rtype: None or list
        :raise TypeError: if ``path`` is not a valid GLXCurses type.
        :raise TypeError: if ``path`` is not a instance of GLXCurses.WidgetPath.
        :raise TypeError: if ``pos`` is not a int.
        """

        # Try to exit as soon of possible
        if not glxc_type(path):
            raise TypeError("'path' must be a GLXCurses type")

        if not isinstance(path, WidgetPath):
            raise TypeError("'path' must be an instance of GLXCurses.WidgetPath")

        if type(pos) != int:
            raise TypeError("'pos' must be a int type")

        # We make the job
        if pos < 0 or pos >= len(path.elems):
            pos = len(path.elems) - 1

        elem = path.elems[pos]

        return elem.siblings


class GLXCPathElement(object):
    # struct GtkPathElement
    # {
    #   GType type;
    #   GQuark name;
    #   GtkStateFlags state;
    #   guint sibling_index;
    #   GHashTable *regions;
    #   GArray *classes;
    #   GtkWidgetPath *siblings;
    # };
    type = str()
    name = str()
    state = str()
    sibling_index = int()
    regions = dict()
    classes = list(dict())
    siblings = None
