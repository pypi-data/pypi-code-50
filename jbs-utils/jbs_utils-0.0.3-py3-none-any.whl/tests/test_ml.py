import unittest
from jbs import ml


class TestML(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_doc_df(self):
        doc_df = ml.init('מדרש תהילים')
        self.assertEqual(143, len(doc_df))

        # now should check sentence_df but we should pass a sentence_tokenizer
        # since we should first split by ':' and then by '.'

    def test_default_sentence_tokenizer(self):
        text = 'hello there. My name is Oren. Nice to meet you'
        self.assertEqual(3, len(ml.default_sentence_tokenizer(text)))

        # here we have a period and space after the last sentence and we still expect 3 sentences
        text = 'hello there. My name is Oren. Nice to meet you. '
        self.assertEqual(3, len(ml.default_sentence_tokenizer(text)))
