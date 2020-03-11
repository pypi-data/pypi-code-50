import unittest
from jbs import quotations as qt


class TestQuotations(unittest.TestCase):
    def setUp(self):
        pass

    def test_detect_tanach_quotations_feature(self):
        pass
        # text = 'כמו שנאמר והארץ היתה תהו ובהו כפי שלמדנו'
        # df = qt.detect_tanach_quotations(text)
        #
        # # df should be in length 8, a row for each word
        # self.assertEqual(8, len(df))
        #
        # # check for individual words
        # self.assertEqual('כמו', df.at[0, 'word'])
        # self.assertEqual('והארץ', df.at[2, 'word'])
        # self.assertEqual('שלמדנו', df.at[7, 'word'])
        #
        # # check for IOB tags
        # self.assertEqual('O', df.at[0, 'iob'])
        # self.assertEqual('O', df.at[1, 'iob'])
        # self.assertEqual('B', df.at[2, 'iob'])
        # self.assertEqual('I', df.at[3, 'iob'])
        # self.assertEqual('I', df.at[4, 'iob'])
        # self.assertEqual('I', df.at[5, 'iob'])
        # self.assertEqual('O', df.at[6, 'iob'])
        # self.assertEqual('O', df.at[7, 'iob'])
        #
        # # check for pasuk URI
        # self.assertEqual(nil?, df.at[0, 'entity'])



