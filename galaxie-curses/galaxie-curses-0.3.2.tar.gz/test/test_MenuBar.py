import unittest
import GLXCurses


class TestMenuBar(unittest.TestCase):
    def test_info_label(self):
        menubar = GLXCurses.MenuBar()
        self.assertIsNone(menubar.info_label)
        menubar.info_label = 'Hello.42'
        self.assertEqual('Hello.42', menubar.info_label)
        menubar.info_label = None
        self.assertIsNone(menubar.info_label)

        self.assertRaises(TypeError, setattr, menubar, 'info_label', 42)

    def test__update_position(self):
        menubar = GLXCurses.MenuBar()
        menu1 = GLXCurses.Menu()
        menu2 = GLXCurses.Menu()
        menu1.title = 'Hello.1'
        menu2.title = 'Hello.2'
        menubar._upgrade_position()

        self.assertEqual([], menubar.list_machin)
        menubar.pack_start(menu1)
        menubar.pack_start(menu1)
        menubar._upgrade_position()
        self.assertEqual([{'start': 2, 'stop': 13}, {'start': 14, 'stop': 25}], menubar.list_machin)


if __name__ == '__main__':
    unittest.main()
