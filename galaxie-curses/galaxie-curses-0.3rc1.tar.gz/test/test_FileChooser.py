import unittest
import os
import GLXCurses


class MyTestCase(unittest.TestCase):
    def test_FileChooser_draw_widget_in_area(self):
        # win = Window()
        # filechooser = GLXCurses.FileSelect()
        #
        # application.add_window(win)
        # win.add(filechooser)
        # # Main loop
        # #filechooser.draw_widget_in_area()
        # application.refresh()
        pass

    def test_FileChooser_set_sort_by_name(self):
        """Test FileChooser.set_sort_by_name()"""

        filechooser = GLXCurses.FileSelect()

        self.assertEqual(True, filechooser.sort_by_name)

        filechooser.set_sort_by_name(False)
        self.assertEqual(False, filechooser.sort_by_name)

        self.assertRaises(TypeError, filechooser.set_sort_by_name, 42)

    def test_FileChooser_get_sort_by_name(self):
        """Test FileChooser.get_sort_by_name()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(True, filechooser.get_sort_by_name())

        filechooser.sort_by_name = False
        self.assertEqual(False, filechooser.get_sort_by_name())

    def test_FileChooser_set_sort_name_order(self):
        """Test FileChooser.set_sort_name_order()"""

        filechooser = GLXCurses.FileSelect()

        self.assertEqual(True, filechooser.sort_name_order)

        filechooser.set_sort_name_order(False)
        self.assertEqual(False, filechooser.sort_name_order)

        self.assertRaises(TypeError, filechooser.set_sort_name_order, 42)

    def test_FileChooser_get_sort_name_order(self):
        """Test FileChooser.get_sort_name_order()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(True, filechooser.get_sort_name_order())

        filechooser.sort_name_order = False
        self.assertEqual(False, filechooser.get_sort_name_order())

    def test_FileChooser_set_sort_by_size(self):
        """Test FileChooser.set_sort_by_name()"""

        filechooser = GLXCurses.FileSelect()

        self.assertEqual(False, filechooser.sort_by_size)

        filechooser.set_sort_by_size(True)
        self.assertEqual(True, filechooser.sort_by_size)

        self.assertRaises(TypeError, filechooser.set_sort_by_size, 42)

    def test_FileChooser_get_sort_by_size(self):
        """Test FileChooser.get_sort_by_size()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(False, filechooser.get_sort_by_size())

        filechooser.sort_by_size = True
        self.assertEqual(True, filechooser.get_sort_by_size())

    def test_FileChooser_set_sort_size_order(self):
        """Test VuMeter.set_sort_size_order()"""

        filechooser = GLXCurses.FileSelect()

        self.assertEqual(True, filechooser.sort_size_order)

        filechooser.set_sort_size_order(False)
        self.assertEqual(False, filechooser.sort_size_order)

        self.assertRaises(TypeError, filechooser.set_sort_size_order, 42)

    def test_FileChooser_get_sort_size_order(self):
        """Test VuMeter.get_sort_size_order()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(True, filechooser.get_sort_size_order())

        filechooser.sort_size_order = False
        self.assertEqual(False, filechooser.get_sort_size_order())

    def test_FileChooser_set_sort_by_mtime(self):
        """Test FileChooser.set_sort_by_mtime()"""

        filechooser = GLXCurses.FileSelect()

        self.assertEqual(False, filechooser.sort_by_mtime)

        filechooser.set_sort_by_mtime(True)
        self.assertEqual(True, filechooser.sort_by_mtime)

        self.assertRaises(TypeError, filechooser.set_sort_by_mtime, 42)

    def test_FileChooser_get_sort_by_mtime(self):
        """Test FileChooser.get_sort_by_mtime()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(False, filechooser.get_sort_by_mtime())

        filechooser.sort_by_mtime = True
        self.assertEqual(True, filechooser.get_sort_by_mtime())

    def test_FileChooser_set_sort_mtime_order(self):
        """Test VuMeter.set_sort_mtime_order()"""

        filechooser = GLXCurses.FileSelect()

        self.assertEqual(True, filechooser.sort_mtime_order)

        filechooser.set_sort_mtime_order(False)
        self.assertEqual(False, filechooser.sort_mtime_order)

        self.assertRaises(TypeError, filechooser.set_sort_mtime_order, 42)

    def test_FileChooser_get_sort_mtime_order(self):
        """Test VuMeter.get_sort_mtime_order()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(True, filechooser.get_sort_mtime_order())

        filechooser.sort_mtime_order = False
        self.assertEqual(False, filechooser.get_sort_mtime_order())

    def test_FileChooser__set_file_list(self):
        """Test FileChooser._set_file_list()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(list, type(filechooser.item_list))

        file_list = os.listdir(os.path.curdir)
        file_list.sort()
        filechooser._set_item_list(file_list)

        self.assertEqual(file_list, filechooser.item_list)

        self.assertRaises(TypeError, filechooser._set_item_list, 42)

    def test_FileChooser__get_file_list(self):
        """Test FileChooser._get_file_list()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(list, type(filechooser._get_item_list()))

        filechooser.item_list = os.listdir(os.path.curdir)
        filechooser.item_list.sort()

        self.assertEqual(filechooser.item_list, filechooser._get_item_list())

    def test_FileChooser__set_list_item_info(self):
        """Test FileChooser._set_list_item_info()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(list, type(filechooser.item_info_list))

        filechooser._set_item_info_list(['Hello', 42])

        self.assertEqual(['Hello', 42], filechooser.item_info_list)

        self.assertRaises(TypeError, filechooser._set_item_info_list, 42)

    def test_FileChooser__get_list_item_info(self):
        """Test FileChooser._get_list_item_info()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(list, type(filechooser._get_item_info_list()))

        filechooser.item_info_list = ['Hello', 42]

        self.assertEqual(filechooser.item_info_list, filechooser._get_item_info_list())

    def test_FileChooser__set_item_it_can_be_display(self):
        """Test FileChooser._set_item_it_can_be_display()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(0, filechooser.item_it_can_be_display)

        filechooser._set_item_it_can_be_display(42)

        self.assertEqual(42, filechooser.item_it_can_be_display)

        self.assertRaises(TypeError, filechooser._set_item_it_can_be_display, '42')

    def test_FileChooser__get_item_it_can_be_display(self):
        """Test FileChooser._get_item_it_can_be_display()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(0, filechooser._get_item_it_can_be_display())

        filechooser.item_it_can_be_display = 42

        self.assertEqual(42, filechooser._get_item_it_can_be_display())

    def test_FileChooser__set_item_list_scroll(self):
        """Test FileChooser._set_item_list_scroll()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(0, filechooser.item_scroll_pos)

        filechooser._set_item_scroll_pos(42)

        self.assertEqual(42, filechooser.item_scroll_pos)

        self.assertRaises(TypeError, filechooser._set_item_scroll_pos, '42')

    def test_FileChooser__get_item_list_scroll(self):
        """Test FileChooser._get_item_list_scroll()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(0, filechooser._get_item_scroll_pos())

        filechooser.item_scroll_pos = 42

        self.assertEqual(42, filechooser._get_item_scroll_pos())

    def test_FileChooser__set_selected_item(self):
        """Test FileChooser._set_selected_item()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(0, filechooser.selected_item_pos)

        filechooser._set_selected_item_pos(42)

        self.assertEqual(42, filechooser.selected_item_pos)

        self.assertRaises(TypeError, filechooser._set_selected_item_pos, '42')

    def test_FileChooser__get_selected_item(self):
        """Test FileChooser._get_selected_item()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(0, filechooser._get_selected_item_pos())

        filechooser.selected_item_pos = 42

        self.assertEqual(42, filechooser._get_selected_item_pos())

    def test_FileChooser__set_selected_item_list_value(self):
        """Test FileChooser._set_selected_item_list_value()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(list, type(filechooser.selected_item_info_list))

        file_list = os.listdir(os.path.curdir)
        file_list.sort()
        filechooser._set_selected_item_info_list(file_list)

        self.assertEqual(file_list, filechooser.selected_item_info_list)

        self.assertRaises(TypeError, filechooser._set_selected_item_info_list, 42)

    def test_FileChooser__get_selected_item_list_value(self):
        """Test FileChooser._get_selected_item_list_value()"""
        filechooser = GLXCurses.FileSelect()

        self.assertEqual(list, type(filechooser._get_selected_item_info_list()))

        filechooser.selected_item_info_list = os.listdir(os.path.curdir)
        filechooser.selected_item_info_list.sort()

        self.assertEqual(filechooser.selected_item_info_list, filechooser._get_selected_item_info_list())

    # def test_utils_get_file_info_list(self):
    #     """Test Utils get_file_info_list"""
    # filechooser = GLXCurses.FileSelect()
    # # ['.', '.', 4096, '29/01/2019  01:52', 4096, 1548723122.4803152]
    # self.assertEqual(list, type(filechooser.get_file_info_list('.')))
    # self.assertEqual(9, len(filechooser.get_file_info_list('.')))
    # self.assertEqual(str, type(filechooser.get_file_info_list('.')[0]))
    # self.assertEqual(str, type(filechooser.get_file_info_list('.')[1]))
    # self.assertEqual(int, type(filechooser.get_file_info_list('.')[2]))
    # self.assertEqual(str, type(filechooser.get_file_info_list('.')[3]))
    # self.assertEqual(int, type(filechooser.get_file_info_list('.')[4]))
    # self.assertEqual(float, type(filechooser.get_file_info_list('.')[5]))
    #
    # self.assertEqual("UP--DIR", filechooser.get_file_info_list('..')[2])
    #
    # #self.assertRaises(FileNotFoundError, filechooser.get_file_info_list, '42')
    # self.assertRaises(TypeError, filechooser.get_file_info_list, None)


if __name__ == '__main__':
    unittest.main()
