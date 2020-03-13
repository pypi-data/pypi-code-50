import os
import unittest

import autofile


class TestOpenFileForRead(unittest.TestCase):

    def setUp(self):
        self.test_sentence = "Αυτή είναι μια δοκιμαστική εγγραφή για τα python unit tests. Να μην διαγραφεί!"
        self.cwd = os.path.dirname(__file__)
        self.input_files = {}
        for enc in ['iso-8859-7', 'utf-8-sig', 'utf-8', 'windows-1253', 'ucs-2-be', 'ucs-2-le']:
            self.input_files[enc] = os.path.join(self.cwd, enc + '.txt')

    def test_is_sentence_included(self):
        for encoding, filename in self.input_files.items():
            with self.subTest(encoding=encoding):
                with autofile.open(filename) as f_obj:
                    data = f_obj.read()
                    self.assertIn(self.test_sentence, data)
