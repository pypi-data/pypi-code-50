import unittest
import jbs_nlp as nlp


class TestIr(unittest.TestCase):
    def test_stopwords(self):
        stopwords = nlp.get_stopwords('midrashraba-mishna-tanach')
        self.assertTrue(len(stopwords) > 10)
        self.assertTrue('את' in stopwords)
        self.assertFalse('רבי' in stopwords)
