import unittest
from unittest.mock import patch
from semi_semantic import Version, VersionSegment, ParseError


class TestVersion(unittest.TestCase):
    def test_release(self):
        self.assertEqual(Version.parse("1.0").release, VersionSegment.parse("1.0"))
        self.assertEqual(
            Version.parse("1.0-alpha").release, VersionSegment.parse("1.0")
        )
        self.assertEqual(Version.parse("1.0+dev").release, VersionSegment.parse("1.0"))
        self.assertEqual(
            Version.parse("1.0-alpha+dev").release, VersionSegment.parse("1.0")
        )

    def test_pre_release(self):
        self.assertIsNone(Version.parse("1.0").pre_release)
        self.assertEqual(
            Version.parse("1.0-alpha").pre_release, VersionSegment.parse("alpha")
        )
        self.assertIsNone(Version.parse("1.0+dev").pre_release)
        self.assertEqual(
            Version.parse("1.0-alpha+dev").pre_release, VersionSegment.parse("alpha")
        )

    def test_post_release(self):
        self.assertIsNone(Version.parse("1.0").post_release)
        self.assertIsNone(Version.parse("1.0-alpha").post_release)
        self.assertEqual(
            Version.parse("1.0+dev").post_release, VersionSegment.parse("dev")
        )
        self.assertEqual(
            Version.parse("1.0-alpha+dev").post_release, VersionSegment.parse("dev")
        )

    def test_parses(self):
        segment_a = VersionSegment.parse("1.0.a")
        segment_b = VersionSegment.parse("1.0.b")
        segment_c = VersionSegment.parse("1.0.c")

        self.assertEqual(
            Version.parse("1.0.a-1.0.b+1.0.c").segments,
            [segment_a, segment_b, segment_c],
        )

        self.assertEqual(Version.parse("1.0.a-1.0.b").segments, [segment_a, segment_b])

        self.assertEqual(Version.parse("1.0.a+1.0.c").segments, [segment_a, segment_c])

        self.assertEqual(Version.parse("1.0.a").segments, [segment_a])

    @patch.object(VersionSegment, "parse")
    def test_parse_error(self, mock_method):
        mock_method.side_effect = ParseError
        with self.assertRaises(ParseError):
            Version.parse("1.0")

    def test_parse_hyphenation(self):
        v = Version.parse("1-1-1")
        self.assertEqual(v.release, VersionSegment.parse("1"))
        self.assertEqual(v.pre_release, VersionSegment.parse("1-1"))
        self.assertIsNone(v.post_release)

        v = Version.parse("1+1-1")
        self.assertEqual(v.release, VersionSegment.parse("1"))
        self.assertIsNone(v.pre_release)
        self.assertEqual(v.post_release, VersionSegment.parse("1-1"))

        v = Version.parse("1-1-1+1-1")
        self.assertEqual(v.release, VersionSegment.parse("1"))
        self.assertEqual(v.pre_release, VersionSegment.parse("1-1"))
        self.assertEqual(v.post_release, VersionSegment.parse("1-1"))

    def test_parse_raises_error_for_empty_segments(self):
        self.assertRaises(ParseError, Version.parse, "+1")
        self.assertRaises(ParseError, Version.parse, "1+")
        self.assertRaises(ParseError, Version.parse, "-1")
        self.assertRaises(ParseError, Version.parse, "1-")
        self.assertRaises(ParseError, Version.parse, "1-+1")
        self.assertRaises(ParseError, Version.parse, "1-1+")

    def test_parse_raises_error_multiple_post_release_segments(self):
        self.assertRaises(ParseError, Version.parse, "1+1+1")

    def test_parse_raises_error_empty_string(self):
        self.assertRaises(ValueError, Version.parse, "")

    def test_parse_raises_error_for_invalid_chars(self):
        self.assertRaises(ParseError, Version.parse, " ")
        self.assertRaises(ParseError, Version.parse, "1 1")
        self.assertRaises(ParseError, Version.parse, "can't do it cap'n")

    def test_str(self):
        release = VersionSegment.parse("1.1.1.1")
        pre_release = VersionSegment.parse("2.2.2.2")
        post_release = VersionSegment.parse("3.3.3.3")

        self.assertEqual(str(Version(release)), "1.1.1.1")

        self.assertEqual(str(Version(release, pre_release)), "1.1.1.1-2.2.2.2")

        self.assertEqual(str(Version(release, None, post_release)), "1.1.1.1+3.3.3.3")

        self.assertEqual(
            str(Version(release, pre_release, post_release)), "1.1.1.1-2.2.2.2+3.3.3.3"
        )

    def test_eq(self):
        self.assertEqual(Version.parse("1.0"), Version.parse("1.0"))
        self.assertEqual(Version.parse("1.0"), Version.parse("1.0.0"))
        self.assertEqual(Version.parse("1-1+1"), Version.parse("1-1+1"))
        self.assertNotEqual(Version.parse("1-1+0"), Version.parse("1-1"))

    def test_eq_none_is_distinct_from_zero(self):
        self.assertNotEqual(Version.parse("1-0+1"), Version.parse("1+1"))
        self.assertNotEqual(Version.parse("1-1+0"), Version.parse("1-1"))

    def test_lt(self):
        self.assertLess(Version.parse("1.0-alpha"), Version.parse("1.0"))
        self.assertLess(Version.parse("1.0"), Version.parse("1.0+dev"))
        self.assertLess(Version.parse("1.0+1"), Version.parse("1.0+2"))

    def test_hashable(self):
        v = Version.parse('1.2.3')
        d = {v: 1}
        self.assertEqual(d[v], 1)
