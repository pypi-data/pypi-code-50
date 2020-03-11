import unittest
import quotationdetection as qt
import pandas as pd


class QuotationDetection(unittest.TestCase):
    def test_to_ngram_dataframe(self):
        text = 'כמו שנאמר את השמים ואת הארץ'

        df = qt.to_ngram_dataframe(text)
        self.assertEqual(5, len(df))
        self.assertEqual('כמו שנאמר', df.ngram[0])
        # test start,end index
        self.assertEqual(0, df.start[0])
        self.assertEqual(1, df.end[0])
        self.assertEqual(1, df.start[1])
        self.assertEqual(2, df.end[1])

        df = qt.to_ngram_dataframe(text, n=5)
        self.assertEqual(2, len(df))
        self.assertEqual('כמו שנאמר את השמים ואת', df.ngram[0])
        # test start,end index
        self.assertEqual(0, df.start[0])
        self.assertEqual(4, df.end[0])
        self.assertEqual(1, df.start[1])
        self.assertEqual(5, df.end[1])

    def test_detect_quotations(self):
        text = 'כמו שנאמר את השמים ואת הארץ'
        df = qt.detect(text)
        # we expect a 'candidates' column to be added:
        self.assertTrue(pd.isna(df.candidates[0]))
        self.assertTrue(pd.isna(df.candidates[1]))

        self.assertTrue(pd.notna(df.candidates[2]))
        self.assertTrue('jbr:text-tanach-1-1-1' in df.candidates[2])

        self.assertTrue(pd.notna(df.candidates[3]))
        self.assertTrue('jbr:text-tanach-1-1-1' in df.candidates[3])

        self.assertTrue(pd.notna(df.candidates[4]))
        self.assertTrue('jbr:text-tanach-1-1-1' in df.candidates[4])
