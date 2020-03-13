import os
import unittest

from autofile.auto_detect import file_encoding


class TestDetections(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(__file__)
        self.input_files = {}
        for enc in ['iso-8859-7', 'utf-8-sig', 'utf-8', 'windows-1253', 'ucs-2-be', 'ucs-2-le']:
            self.input_files[enc] = os.path.join(self.cwd, enc + '.txt')

    def __detect_for_enc(self, encoding):
        filename = self.input_files[encoding]
        enc = file_encoding(filename)
        return enc

    def test_utf8(self):
        encoding = 'utf-8'
        detected = self.__detect_for_enc(encoding)
        self.assertEqual(detected, encoding)

    def test_utf8sig(self):
        encoding = 'utf-8-sig'
        detected = self.__detect_for_enc(encoding)
        self.assertEqual(detected, encoding)

    def test_win1253(self):
        encoding = 'windows-1253'
        detected = self.__detect_for_enc(encoding)
        self.assertEqual(detected, encoding)

    def test_iso88597(self):
        encoding = 'iso-8859-7'
        detected = self.__detect_for_enc(encoding)
        self.assertEqual(detected, encoding)

    def test_utf16le(self):
        encoding = 'ucs-2-le'
        python_enc = 'utf-16'
        detected = self.__detect_for_enc(encoding)
        self.assertEqual(detected, python_enc)

    def test_utf16be(self):
        encoding = 'ucs-2-be'
        python_enc = 'utf-16'
        detected = self.__detect_for_enc(encoding)
        self.assertEqual(detected, python_enc)


if __name__ == '__main__':
    unittest.main()
