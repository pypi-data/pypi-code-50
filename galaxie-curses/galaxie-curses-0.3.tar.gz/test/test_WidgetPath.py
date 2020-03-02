#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: the Galaxie Curses Team, all rights reserved

from GLXCurses.WidgetPath import WidgetPath
from GLXCurses.WidgetPath import GLXCPathElement
from GLXCurses.Object import Object
from GLXCurses.Constants import GLXC
from yaml import dump

import unittest


# Unittest
class TestWidgetPath(unittest.TestCase):

    def test_WidgetPath_new(self):
        """Test WidgetPath.new()"""
        path = WidgetPath().new()

        # Check if it return a instance of a WidgetPath
        self.assertTrue(isinstance(path, WidgetPath))

        # Check the Path Element type
        #         path_element = dump({
        #           'type': str(''),
        #           'name': str(''),
        #           'state': str(''),
        #           'sibling_index': int(0),
        #           'regions': list(dict()),
        #           'classes': list(dict()),
        #           'siblings': WidgetPath()
        #         })
        # that is the elems[0] that because it just freshly created
        self.assertEquals(type(str()), type(path.elems[0].type))
        self.assertEquals(type(str()), type(path.elems[0].name))
        self.assertEquals(type(str()), type(path.elems[0].state))
        self.assertEquals(type(int()), type(path.elems[0].sibling_index))
        self.assertEquals(type(dict()), type(path.elems[0].regions))
        self.assertEquals(type(list()), type(path.elems[0].classes))
        self.assertEquals(type(None), type(path.elems[0].siblings))

        # check if ref_count = 1
        self.assertEqual(1, path.ref_count)

    def test_WidgetPath_element_copy(self):
        """Test WidgetPath.element_copy()"""
        path1 = WidgetPath().new()
        path2 = WidgetPath().new()
        the_thing = Object()

        test_type_value = GLXC.TYPE_CONTAINER
        test_name_value = "Container"
        test_state_value = "Hello"
        test_sibling_index_value = 1
        test_classes_value = [
            {'class1': 'my super class1', 'class2': 'my super class2'},
            {'class2': 'my super class2', 'class4': 'my super class4'},
            {'class5': 'my super class5', 'class6': 'my super class6'},
        ]

        test_regions_value = [
            {'regions1': 'my super regions1', 'regions2': 'my super regions2'},
            {'regions2': 'my super regions2', 'regions4': 'my super regions4'},
            {'regions5': 'my super regions5', 'regions6': 'my super regions6'},
        ]

        test_siblings_value = ['1', '2', '3']

        path1.elems[0].type = test_type_value
        path1.elems[0].name = test_name_value
        path1.elems[0].state = test_state_value
        path1.elems[0].sibling_index = test_sibling_index_value
        path1.elems[0].regions = test_regions_value
        path1.elems[0].classes = test_classes_value
        path1.elems[0].siblings = test_siblings_value

        path1.element_copy(path2.elems[0], path1.elems[0])

        self.assertEqual(path2.elems[0].type, test_type_value)
        self.assertEqual(path2.elems[0].name, test_name_value)
        self.assertEqual(path2.elems[0].state, test_state_value)
        self.assertEqual(path2.elems[0].sibling_index,  test_sibling_index_value)
        self.assertEqual(path2.elems[0].regions, test_regions_value)
        self.assertEqual(path2.elems[0].classes, test_classes_value)
        self.assertEqual(path2.elems[0].siblings, test_siblings_value)

        # Check Errors
        self.assertRaises(
            TypeError,
            path1.element_copy,
            dest=path2.elems[0],
            src=the_thing
        )
        self.assertRaises(
            TypeError,
            path1.element_copy,
            src=path1.elems[0],
            dest='Hello'
        )

    def test_WidgetPath_copy(self):
        """Test WidgetPath.copy()"""
        path1 = WidgetPath().new()

        the_thing = Object()

        test_type_value = GLXC.TYPE_CONTAINER
        test_name_value = "Container"
        test_state_value = "Hello"
        test_sibling_index_value = 1
        test_classes_value = [
            {'class1': 'my super class1', 'class2': 'my super class2'},
            {'class2': 'my super class2', 'class4': 'my super class4'},
            {'class5': 'my super class5', 'class6': 'my super class6'},
        ]

        test_regions_value = [
            {'regions1': 'my super regions1', 'regions2': 'my super regions2'},
            {'regions2': 'my super regions2', 'regions4': 'my super regions4'},
            {'regions5': 'my super regions5', 'regions6': 'my super regions6'},
        ]

        test_siblings_value = ['1', '2', '3']

        path1.elems[0].type = test_type_value
        path1.elems[0].name = test_name_value
        path1.elems[0].state = test_state_value
        path1.elems[0].sibling_index = test_sibling_index_value
        path1.elems[0].regions = test_regions_value
        path1.elems[0].classes = test_classes_value
        path1.elems[0].siblings = test_siblings_value

        path2 = path1.copy(path1)
        # Check return type
        self.assertTrue(isinstance(path2, WidgetPath))

        self.assertNotEqual(path1, path2)

        self.assertEqual(path1.elems[0].type, path2.elems[0].type)
        self.assertEqual(path1.elems[0].name, path2.elems[0].name)
        self.assertEqual(path1.elems[0].state, path2.elems[0].state)
        self.assertEqual(path1.elems[0].sibling_index, path2.elems[0].sibling_index)
        self.assertEqual(path1.elems[0].regions, path2.elems[0].regions)
        self.assertEqual(path1.elems[0].classes, path2.elems[0].classes)
        self.assertEqual(path1.elems[0].siblings, path2.elems[0].siblings)

        # Check Errors
        self.assertRaises(
            TypeError,
            path1.copy,
            path=the_thing,
        )

        self.assertRaises(
            TypeError,
            path1.copy,
            path=the_thing,
        )

    def test_WidgetPath_ref(self):
        """Test WidgetPath.ref()"""
        path1 = WidgetPath().new()
        the_thing = Object()

        # check the default value, suppose to be 1 after a WidgetPath().new()
        self.assertEqual(1, path1.ref_count)

        return_ref = path1.ref(path1)

        # Check return type
        self.assertTrue(isinstance(return_ref, WidgetPath))
        # check if ref_count have been increase by one.
        self.assertEqual(2, path1.ref_count)

        # Check Errors
        self.assertRaises(
            TypeError,
            path1.ref,
            path='Hello',
        )

        self.assertRaises(
            TypeError,
            path1.ref,
            path=the_thing,
        )

    def test_WidgetPath_unref(self):
        """Test WidgetPath.unref()"""
        path = WidgetPath().new()
        the_thing = Object()

        # check the default value, suppose to be 1 after a WidgetPath().new()
        self.assertEqual(1, path.ref_count)

        path.ref(path)
        self.assertEqual(2, path.ref_count)
        self.assertEqual(len(path.elems), 1)

        path.unref(path)
        self.assertEqual(1, path.ref_count)
        self.assertEqual(len(path.elems), 1)

        # Check if the reference count reaches 0
        path.unref(path)
        self.assertEqual(0, path.ref_count)
        self.assertEqual(len(path.elems), 0)

        # Check Errors
        self.assertRaises(
            TypeError,
            path.unref,
            path='Hello',
        )

        self.assertRaises(
            TypeError,
            path.unref,
            path=the_thing,
        )

    def test_WidgetPath_free(self):
        """Test WidgetPath.free()"""
        path = WidgetPath().new()
        the_thing = Object()

        # check the default value, suppose to be 1 after a WidgetPath().new()
        self.assertEqual(1, path.ref_count)

        path.ref(path)
        self.assertEqual(2, path.ref_count)
        self.assertEqual(len(path.elems), 1)

        path.free(path)
        self.assertEqual(1, path.ref_count)
        self.assertEqual(len(path.elems), 1)

        # Check if the reference count reaches 0
        path.free(path)
        self.assertEqual(0, path.ref_count)
        self.assertEqual(len(path.elems), 0)

        # Check Errors
        self.assertRaises(
            TypeError,
            path.free,
            'Hello',
        )

        self.assertRaises(
            TypeError,
            path.free,
            the_thing,
        )

    def test_WidgetPath_length(self):
        """Test WidgetPath.length()"""
        path = WidgetPath()
        the_thing = Object()

        path.append_type(path, GLXC.TYPE_CONTAINER)
        path.append_type(path, GLXC.TYPE_CONTAINER)
        path.append_type(path, GLXC.TYPE_CONTAINER)
        path.append_type(path, GLXC.TYPE_CONTAINER)

        # Check the return type
        self.assertEqual(type(int()), type(path.length(path)))
        self.assertEqual(path.length(path), 4)

        # Check Errors
        self.assertRaises(
            TypeError,
            path.length,
            'Hello',
        )

        self.assertRaises(
            TypeError,
            path.length,
            the_thing,
        )

    def test_WidgetPath_to_string(self):
        """Test WidgetPath.to_string()"""
        path = WidgetPath().new()

        the_thing = Object()

        test_type_value = GLXC.TYPE_CONTAINER
        test_name_value = "Container"
        test_state_value = "Hello"
        test_sibling_index_value = 1
        test_classes_value = [
            {'class1': 'my super class1', 'class2': 'my super class2'},
            {'class2': 'my super class2', 'class4': 'my super class4'},
            {'class5': 'my super class5', 'class6': 'my super class6'},
        ]

        test_regions_value = [
            {'regions1': 'my super regions1', 'regions2': 'my super regions2'},
            {'regions2': 'my super regions2', 'regions4': 'my super regions4'},
            {'regions5': 'my super regions5', 'regions6': 'my super regions6'},
        ]

        test_siblings_value = ['1', '2', '3']

        path.elems[0].type = test_type_value
        path.elems[0].name = test_name_value
        path.elems[0].state = test_state_value
        path.elems[0].sibling_index = test_sibling_index_value
        path.elems[0].regions = test_regions_value
        path.elems[0].classes = test_classes_value
        path.elems[0].siblings = test_siblings_value

        wanted_value = dump(path.elems)
        returned_value = path.to_string(path)

        self.assertEqual(wanted_value, returned_value)

        # Check Errors
        # Check when WidgetPath is not a GLXC.WidgetPath
        self.assertRaises(
            TypeError,
            path.to_string,
            'Hello',
        )

        self.assertRaises(
            TypeError,
            path.to_string,
            the_thing,
        )

    def test_WidgetPath_prepend_type(self):
        """Test WidgetPath.prepend_type()"""
        path = WidgetPath()
        the_thing = Object()

        path.prepend_type(path, GLXC.TYPE_BIN)
        self.assertEquals(path.elems[0].type, GLXC.TYPE_BIN)

        path.prepend_type(path, GLXC.TYPE_CONTAINER)
        self.assertEquals(path.elems[0].type, GLXC.TYPE_CONTAINER)

        path.prepend_type(path, GLXC.TYPE_BUTTON)
        self.assertEquals(path.elems[0].type, GLXC.TYPE_BUTTON)

        # Check errors
        # Check when WidgetPath is not a GLXC.WidgetPath
        self.assertRaises(
            TypeError,
            path.prepend_type,
            "Hello",
            GLXC.TYPE_BUTTON
        )
        self.assertRaises(
            TypeError,
            path.prepend_type,
            the_thing,
            GLXC.TYPE_BUTTON
        )
        # Type is not a GLXC.Type
        self.assertRaises(
            TypeError,
            path.prepend_type,
            path,
            'Hello'
        )

    def test_WidgetPath_append_type(self):
        """Test WidgetPath.append_type()"""
        path = WidgetPath()
        the_thing = Object()

        position1 = path.append_type(path, GLXC.TYPE_BIN)
        self.assertEqual(type(position1), type(int()))
        self.assertEquals(position1, 0)

        position2 = path.append_type(path, GLXC.TYPE_CONTAINER)
        self.assertEqual(type(position2), type(int()))
        self.assertEquals(position2, 1)

        position3 = path.append_type(path, GLXC.TYPE_BUTTON)
        self.assertEqual(type(position3), type(int()))
        self.assertEquals(position3, 2)

        # Check errors
        # Check when WidgetPath is not a GLXC.WidgetPath
        self.assertRaises(
            TypeError,
            path.append_type,
            "Hello",
            GLXC.TYPE_BUTTON
        )
        self.assertRaises(
            TypeError,
            path.append_type,
            the_thing,
            GLXC.TYPE_BUTTON
        )
        # Type is not a GLXC.Type
        self.assertRaises(
            TypeError,
            path.append_type,
            path,
            'Hello'
        )

    def test_WidgetPath_append_with_siblings(self):
        """Test WidgetPath.append_with_siblings()"""
        path = WidgetPath()
        siblings = WidgetPath()
        the_thing = Object()

        pathelement1 = GLXCPathElement()
        pathelement1.sibling_index = 0
        pathelement1.siblings = WidgetPath()
        pathelement1.name = 'pathelement1'

        pathelement2 = GLXCPathElement()
        pathelement2.sibling_index = 0
        pathelement2.siblings = WidgetPath()
        pathelement2.name = 'pathelement2'

        pathelement3 = GLXCPathElement()
        pathelement3.sibling_index = 0
        pathelement3.siblings = WidgetPath()
        pathelement3.name = 'pathelement3'

        pathelement2.siblings.elems.append(pathelement3)

        path.elems = list()
        path.elems.append(pathelement1)
        path.siblings = WidgetPath()

        siblings.elems = list()
        siblings.elems.append(pathelement2)
        siblings.siblings = WidgetPath()

        self.assertEqual(path.elems[0], pathelement1)
        self.assertEqual(siblings.elems[0].siblings.elems[0].name, 'pathelement3')

        # Before
        print('Before:')
        print(path.to_string(path))
        print(siblings.to_string(siblings))
        # print(siblings.to_string(siblings))

        # check the size before
        self.assertEqual(path.length(path), 1)
        self.assertEqual(siblings.length(siblings), 1)

        # During
        path.append_with_siblings(path, siblings, 1)

        # After
        print('After:')
        print(path.to_string(path))

        # check the size after
        self.assertEqual(path.length(path), 2)

        # Check if path contain pathelement2 as sibling
        self.assertEqual(path.elems[1].siblings.elems[0].name, 'pathelement2')
        # with it siblings child ?
        self.assertEqual(path.elems[1].siblings.elems[0].siblings.elems[0].name, 'pathelement3')

        # Check errors
        # Check when WidgetPath is not a GLXC.WidgetPath
        self.assertRaises(
            TypeError,
            path.append_with_siblings,
            "Hello",
            siblings,
            1
        )
        self.assertRaises(
            TypeError,
            path.append_with_siblings,
            path,
            'hello',
            1
        )
        self.assertRaises(
            TypeError,
            path.append_with_siblings,
            the_thing,
            siblings,
            1
        )
        self.assertRaises(
            TypeError,
            path.append_with_siblings,
            path,
            the_thing,
            1
        )
        self.assertRaises(
            TypeError,
            path.append_with_siblings,
            path,
            siblings,
            None
        )
        # Check value error
        self.assertRaises(
            ValueError,
            path.append_with_siblings,
            path,
            siblings,
            -1
        )

    def test_WidgetPath_iter_get_siblings(self):
        """Test WidgetPath.iter_get_siblings()"""
        siblings = WidgetPath().new()
        siblings.elems[0].name = 'My Widget Patch 2'

        path = WidgetPath()
        path.append_type(path, GLXC.TYPE_BUTTON)
        path.elems[0].name = 'My Widget Patch 1'
        path.append_with_siblings(path, siblings, len(siblings.elems))

        returned_value_1 = path.iter_get_siblings(path, 0)
        returned_value_2 = path.iter_get_siblings(path, 1)

        self.assertEqual(type(None), type(returned_value_1))
        self.assertEqual(type(WidgetPath()), type(returned_value_2))
        self.assertEqual(returned_value_2.elems[0].name, 'My Widget Patch 2')

        # print(path.to_string(path))
        # self.assertTrue(False)

        # Check errors
        # Check when WidgetPath is not a GLXC.WidgetPath
        the_thing = Object()
        self.assertRaises(
            TypeError,
            path.iter_get_siblings,
            "Hello",
            1
        )
        self.assertRaises(
            TypeError,
            path.iter_get_siblings,
            the_thing,
            1
        )
        self.assertRaises(
            TypeError,
            path.iter_get_siblings,
            path,
            'Hello'
        )
