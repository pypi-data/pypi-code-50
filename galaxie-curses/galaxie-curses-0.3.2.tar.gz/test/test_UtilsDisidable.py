import unittest
import GLXCurses


class TestDividable(unittest.TestCase):
    def test_start(self):
        dividable = GLXCurses.Dividable()
        self.assertIsNone(dividable.start)
        dividable.start = 42
        self.assertEqual(42, dividable.start)
        dividable.start = None
        self.assertIsNone(dividable.start)

        self.assertRaises(TypeError, setattr, dividable, 'start', 'Hello.42')

    def test_stop(self):
        dividable = GLXCurses.Dividable()
        self.assertIsNone(dividable.stop)
        dividable.stop = 42
        self.assertEqual(42, dividable.stop)
        dividable.stop = None
        self.assertIsNone(dividable.stop)

        self.assertRaises(TypeError, setattr, dividable, 'stop', 'Hello.42')

    def test_num(self):
        dividable = GLXCurses.Dividable()
        self.assertIsNone(dividable.num)
        dividable.num = 42
        self.assertEqual(42, dividable.num)
        dividable.num = None
        self.assertIsNone(dividable.num)

        self.assertRaises(TypeError, setattr, dividable, 'num', 'Hello.42')

    def test_round_type(self):
        dividable = GLXCurses.Dividable()
        self.assertIsNone(dividable.round_type)
        dividable.num = None
        for round_type in [GLXCurses.GLXC.ROUND_UP,
                           GLXCurses.GLXC.ROUND_DOWN,
                           GLXCurses.GLXC.ROUND_HALF_UP,
                           GLXCurses.GLXC.ROUND_HALF_DOWN]:
            dividable.round_type = round_type
            self.assertEqual(round_type, dividable.round_type)
        dividable.round_type = None
        self.assertIsNone(dividable.round_type)

        self.assertRaises(TypeError, setattr, dividable, 'round_type', ['Hello.42', 'Hello.24'])
        self.assertRaises(ValueError, setattr, dividable, 'round_type', 'Hello.42')

    def test_linspace(self):
        dividable = GLXCurses.Dividable()
        dividable.start = 0
        dividable.stop = 99
        dividable.num = 3
        dividable.round_type = GLXCurses.GLXC.ROUND_HALF_DOWN
        self.assertEqual(
            {'0': (0, 32), '1': (33, 65), '2': (66, 99)},
            dividable.split_positions
        )
        dividable.start = 0
        dividable.stop = 99
        dividable.num = 5
        dividable.round_type = GLXCurses.GLXC.ROUND_HALF_DOWN
        self.assertEqual(
            {'0': (0, 19), '1': (20, 39), '2': (40, 59), '3': (60, 79), '4': (80, 99)},
            dividable.split_positions
        )


if __name__ == '__main__':
    unittest.main()
