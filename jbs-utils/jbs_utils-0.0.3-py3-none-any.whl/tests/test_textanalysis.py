import unittest
import re
from textanalysis import TagMatcher, match_dataframe
from jbs import ir as ir
from pathlib import Path


class RashiMatcher(TagMatcher):
    def match(self, doc_uri: str, text: str) -> list:
        result = []
        for match in re.finditer(r'רש"י', text):
            result.append(self.create_match(doc_uri, 'jbr:tag-person', match.start(), match.end(),
                                            entity='jbr:author-rashi',
                                            mention=match.group()))

        return result


class TestTextAnalysis(unittest.TestCase):
    def test_match_rashi_single_text(self):
        text = 'ראה רש"י שם וגם רש"י שם רשי'
        matcher = RashiMatcher()
        res = matcher.match('jbr:text-123', text)

        self.assertEqual(2, len(res))
        match = res[0]
        self.assertEqual(4, match['start'])
        self.assertEqual(8, match['end'])

        ramban_1_1_1 = 'בְּרֵאשִׁית – כתב רש"י: ואם באת לפרשו כפשוטו כך פרשהו: בְּרֵאשִׁית בריית שמים וארץ, והארץ היתה תהו ובהו וחושך, ויאמר הקב"ה יהי אור. אם כן, הכל נמשך לבריאת האור.'
        res = matcher.match('jbr:text-123', ramban_1_1_1)
        self.assertEqual(1, len(res))

    def test_match_rashi_in_dataframe(self):
        # get perusim ramban
        ir.scope_clear()
        ir.scope_add_book('רמב"ן')
        df = ir.fetch()  # shape (1738, 4)
        rashi_matcher = RashiMatcher()
        res = match_dataframe(df, rashi_matcher, json_path=Path('ramban_mentions_rashi.json'))
        self.assertTrue(len(res) > 500)