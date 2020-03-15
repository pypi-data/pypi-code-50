import unittest

from graphic_lib.Font import Glyph


class TestGlyph(unittest.TestCase):

    def test_height(self):
        sut = Glyph([[1, 2], [3, 4]])
        self.assertEqual(sut.height(), 2)

        sut = Glyph([[1, 2, 3]])
        self.assertEqual(sut.height(), 1)

        sut = Glyph([[1], [3], [5]])
        self.assertEqual(sut.height(), 3)

    def test_width(self):
        sut = Glyph([[1, 2], [3, 4]])
        self.assertEqual(sut.width(), 2)

        sut = Glyph([[1, 2, 3]])
        self.assertEqual(sut.width(), 3)

        sut = Glyph([[1], [3], [5]])
        self.assertEqual(sut.width(), 1)

    def test_glyph(self):
        sut = Glyph([[1, 2], [3, 4]])
        self.assertEqual(sut.glyph(), [[1, 2], [3, 4]])

        sut = Glyph([[1, 2, 3]])
        self.assertEqual(sut.glyph(), [[1, 2, 3]])

        sut = Glyph([[1], [3], [5]])
        self.assertEqual(sut.glyph(), [[1], [3], [5]])
