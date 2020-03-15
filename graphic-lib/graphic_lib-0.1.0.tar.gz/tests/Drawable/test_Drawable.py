import unittest
import unittest.mock

from graphic_lib.detail import Drawable


class TestDrawable(unittest.TestCase):

    def test_init(self):
        sut = Drawable([2, 2])
        self.assertEqual(sut.framebuffer, [[0, 0], [0, 0]])

        sut = Drawable([3, 1])
        self.assertEqual(sut.framebuffer, [[0, 0, 0], [0]])

        sut = Drawable([1, 3])
        self.assertEqual(sut.framebuffer, [[0], [0, 0, 0]])

    def test_draw_other_within_left_top_corner(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(0, 0, to_draw)
        self.assertEqual(sut.framebuffer, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_draw_other_within_middle(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(1, 1, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])

    def test_draw_other_within_right_top_corner(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(2, 0, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_draw_other_within_right_bottom_corner(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(2, 2, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])

    def test_draw_other_within_left_bottom_corner(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(0, 2, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]])

    def test_draw_other_partiali_within_left_top_corner(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(-1, -1, to_draw)
        self.assertEqual(sut.framebuffer, [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_draw_other_partiali_within_top_endge(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(1, -1, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_draw_other_partiali_within_top_right_corner(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(3, -1, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_draw_other_partiali_within_right_edge(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(3, 1, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]])

    def test_draw_other_partiali_within_right_bottom_corner(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(3, 3, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])

    def test_draw_other_partiali_within_bottom_edge(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(1, 3, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0]])

    def test_draw_other_partiali_within_bottom_left_corner(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(-1, 3, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]])

    def test_draw_other_partiali_within_left_edge(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(-1, 1, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]])

    def test_draw_other_outside(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([2, 2])

        to_draw.framebuffer = [[1, 1], [1, 1]]

        sut.draw(-10, 10, to_draw)
        self.assertEqual(sut.framebuffer, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_draw_other_bigger(self):
        sut = Drawable([4, 4, 4, 4])
        to_draw = Drawable([6, 6, 6, 6, 6, 6])

        to_draw.framebuffer = [[1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1]]

        sut.draw(-1, -1, to_draw)
        self.assertEqual(sut.framebuffer, [[1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 0, 1]])

    def test_clear(self):
        sut = Drawable([2, 2])
        sut.framebuffer = [[1, 1], [1, 1]]

        sut.clear()
        self.assertEqual(sut.framebuffer, [[0, 0], [0, 0]])
