import unittest
import unittest.mock

from graphic_lib.Font import MetaFont, Glyph


class MockGlyph:
    def __init__(self, glyph):
        self.glyph = glyph
        self.glyph_height = 0

    def height(self):
        return self.glyph_height

    def configure(self, new_height):
        self.glyph_height = new_height

    def get_glyph(self):
        return self.glyph


class FakeFont(metaclass=MetaFont):
    glyphs = {
        "1": MockGlyph([[1, 2], [3, 4]]),
        "2": MockGlyph([[1, 2, 3], [2, 3, 4]]),
        "3": MockGlyph([[1], [2], [3]])
    }


class TestFont(unittest.TestCase):

    def test_get_item(self):
        self.assertEqual(FakeFont["1"].get_glyph(), [[1, 2], [3, 4]])
        self.assertEqual(FakeFont["2"].get_glyph(), [[1, 2, 3], [2, 3, 4]])
        self.assertEqual(FakeFont["3"].get_glyph(), [[1], [2], [3]])

    def test_height(self):
        FakeFont["1"].configure(3)
        FakeFont["2"].configure(2)
        FakeFont["3"].configure(1)

        self.assertEqual(FakeFont.height(), 3)

        FakeFont["1"].configure(0)
        FakeFont["2"].configure(5)
        FakeFont["3"].configure(7)

        self.assertEqual(FakeFont.height(), 7)
