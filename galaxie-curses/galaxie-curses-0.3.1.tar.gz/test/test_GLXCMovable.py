import unittest
import GLXCurses


class TestGLXCMovable(unittest.TestCase):
    def test_x_offset(self):
        movable = GLXCurses.GLXCMovable()
        self.assertEqual(0, movable.x_offset)
        movable.x_offset = 42
        self.assertEqual(42, movable.x_offset)
        movable.x_offset = None
        self.assertEqual(0, movable.x_offset)

        self.assertRaises(TypeError, setattr, movable, 'x_offset', 'Hello.42')

    def test_y_offset(self):
        movable = GLXCurses.GLXCMovable()
        self.assertEqual(0, movable.y_offset)
        movable.y_offset = 24
        self.assertEqual(24, movable.y_offset)
        movable.y_offset = None
        self.assertEqual(0, movable.y_offset)

        self.assertRaises(TypeError, setattr, movable, 'y_offset', 'Hello.42')


if __name__ == '__main__':
    unittest.main()
