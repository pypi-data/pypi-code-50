import unittest
from GLXCurses.Child import Child
from GLXCurses.ChildProperty import ChildProperty
from GLXCurses.Widget import Widget


class TestChild(unittest.TestCase):
    def test_widget(self):
        child = Child()
        widget = Widget()
        self.assertIsNone(child.widget)
        child.widget = widget
        self.assertEqual(widget, child.widget)
        child.widget = None
        self.assertIsNone(child.widget)

        self.assertRaises(TypeError, setattr, child, 'widget', 42)

    def test_name(self):
        child = Child()
        self.assertIsNone(child.name)
        child.name = 'Hello.42'
        self.assertEqual('Hello.42', child.name)
        child.name = None
        self.assertIsNone(child.name)

        self.assertRaises(TypeError, setattr, child, 'name', 42)

    def test_type(self):
        child = Child()
        self.assertIsNone(child.type)
        child.type = 'GLXCurses.Container'
        self.assertEqual('GLXCurses.Container', child.type)
        child.type = None
        self.assertIsNone(child.type)

        self.assertRaises(TypeError, setattr, child, 'type', 42)
        self.assertRaises(ValueError, setattr, child, 'type', 'Hello.42')

    def test_id(self):
        child = Child()
        self.assertIsNone(child.id)
        child.id = 'Hello.42'
        self.assertEqual('Hello.42', child.id)
        child.id = None
        self.assertIsNone(child.id)

        self.assertRaises(TypeError, setattr, child, 'id', 42)

    def test_properties(self):
        child = Child()
        properties = ChildProperty()
        self.assertEqual(type(child.properties), ChildProperty)
        child.properties = properties
        self.assertEqual(properties, child.properties)

        child.properties.padding = 1
        self.assertEqual(1, child.properties.padding)

        child.properties = None
        self.assertIsNone(child.properties)

        self.assertRaises(TypeError, setattr, child, 'properties', 42)


if __name__ == '__main__':
    unittest.main()
