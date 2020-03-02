import unittest

import GLXCurses


class TestApplicationController(unittest.TestCase):
    def test_has_default(self):
        monitor = GLXCurses.ApplicationMonitor()
        widget = GLXCurses.Widget()
        child = GLXCurses.Child()
        child.widget = widget
        self.assertIsNone(monitor.has_default)
        monitor.has_default = child
        self.assertEqual(child, monitor.has_default)
        monitor.has_default = None
        self.assertIsNone(monitor.has_default)
        monitor.has_default = widget
        self.assertEqual(widget, monitor.has_default.widget)
        monitor.has_default = None
        self.assertIsNone(monitor.has_default)

        self.assertRaises(TypeError, setattr, monitor, 'has_default', 42)

    def test_has_focus(self):
        monitor = GLXCurses.ApplicationMonitor()
        widget = GLXCurses.Widget()
        child = GLXCurses.Child()
        child.widget = widget
        self.assertIsNone(monitor.has_focus)
        monitor.has_focus = child
        self.assertEqual(child, monitor.has_focus)
        monitor.has_focus = None
        self.assertIsNone(monitor.has_focus)
        monitor.has_focus = widget
        self.assertEqual(widget, monitor.has_focus.widget)
        monitor.has_focus = None
        self.assertIsNone(monitor.has_focus)

        self.assertRaises(TypeError, setattr, monitor, 'has_focus', 42)


if __name__ == '__main__':
    unittest.main()
