import unittest
import audio
import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE = os.path.join(TEST_DIR, "test.flac")

TEST_RATE = 44100
TEST_SHAPE = (44100, 2)
FIRST_SAMPLE = (0, 0)
LAST_SAMPLE = (-1164, -1164)

class ReadTests(unittest.TestCase):
    def test_memread(self):
        rate, a = audio.memread(TEST_FILE)
        self.assertEqual(rate, TEST_RATE)
        self.assertEqual(a.shape, TEST_SHAPE)
        self.assertEqual(tuple(a[0, :]), FIRST_SAMPLE)
        self.assertEqual(tuple(a[-1, :]), LAST_SAMPLE)

    def test_tempread(self):
        rate, a = audio.tempread(TEST_FILE)
        self.assertEqual(rate, TEST_RATE)
        self.assertEqual(a.shape, TEST_SHAPE)
        self.assertEqual(tuple(a[0, :]), FIRST_SAMPLE)
        self.assertEqual(tuple(a[-1, :]), LAST_SAMPLE)
