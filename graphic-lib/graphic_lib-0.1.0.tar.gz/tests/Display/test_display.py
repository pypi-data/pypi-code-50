import unittest
import unittest.mock

from graphic_lib.Display import Display, FIRST_PIXEL_POSITION
from operator import __getitem__


class Model:
    pass


class MockFrameBuffer:
    def __init__(self, *args):
        pass

    def __getitem__(self, item):
        pass


class FakeView:
    def __init__(self, *args):
        pass


class TestDisplay(unittest.TestCase):

    @unittest.mock.patch(f'{__name__}.MockFrameBuffer.__getitem__')
    def test_top_left(self, mock):
        sut = Display([3, 3, 3], FIRST_PIXEL_POSITION.TOP_LEFT, {"test": FakeView}, Model, MockFrameBuffer)

        sut(0, 0)
        mock.assert_called_with(0)

        sut(1, 1)
        mock.assert_called_with(4)

        sut(2, 2)
        mock.assert_called_with(8)

    @unittest.mock.patch(f'{__name__}.MockFrameBuffer.__getitem__')
    def test_top_right(self, mock):
        sut = Display([3, 3, 3], FIRST_PIXEL_POSITION.TOP_RIGHT, {"test": FakeView}, Model, MockFrameBuffer)

        sut(0, 0)
        mock.assert_called_with(2)

        sut(1, 1)
        mock.assert_called_with(4)

        sut(2, 2)
        mock.assert_called_with(6)

    @unittest.mock.patch(f'{__name__}.MockFrameBuffer.__getitem__')
    def test_bottom_left_odd_number_of_rows(self, mock):
        sut = Display([3, 3, 3], FIRST_PIXEL_POSITION.BOTTOM_LEFT, {"test": FakeView}, Model, MockFrameBuffer)

        sut(0, 0)
        mock.assert_called_with(6)

        sut(1, 1)
        mock.assert_called_with(4)

        sut(2, 2)
        mock.assert_called_with(2)

    @unittest.mock.patch(f'{__name__}.MockFrameBuffer.__getitem__')
    def test_bottom_left_even_number_of_rows(self, mock):
        sut = Display([3, 3, 3, 3], FIRST_PIXEL_POSITION.BOTTOM_LEFT, {"test": FakeView}, Model, MockFrameBuffer)

        sut(0, 0)
        mock.assert_called_with(11)

        sut(1, 1)
        mock.assert_called_with(7)

        sut(2, 2)
        mock.assert_called_with(3)

    @unittest.mock.patch(f'{__name__}.MockFrameBuffer.__getitem__')
    def test_bottom_right_odd_number_of_rows(self, mock):
        sut = Display([3, 3, 3], FIRST_PIXEL_POSITION.BOTTOM_RIGHT, {"test": FakeView}, Model, MockFrameBuffer)

        sut(0, 0)
        mock.assert_called_with(8)

        sut(1, 1)
        mock.assert_called_with(4)

        sut(2, 2)
        mock.assert_called_with(0)

    @unittest.mock.patch(f'{__name__}.MockFrameBuffer.__getitem__')
    def test_bottom_right_even_number_of_rows(self, mock):
        sut = Display([3, 3, 3, 3], FIRST_PIXEL_POSITION.BOTTOM_RIGHT, {"test": FakeView}, Model, MockFrameBuffer)

        sut(0, 0)
        mock.assert_called_with(9)

        sut(1, 1)
        mock.assert_called_with(7)

        sut(2, 2)
        mock.assert_called_with(5)
