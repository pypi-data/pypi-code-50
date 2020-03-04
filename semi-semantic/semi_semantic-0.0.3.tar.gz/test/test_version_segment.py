import unittest

from semi_semantic import VersionSegment, ParseError


class TestVersionSegment(unittest.TestCase):
    def test_parse(self):
        test_cases = [
            # handles one or more non-negative numerical components
            {"input": "1", "expected": [1]},
            {"input": "1.1", "expected": [1, 1]},
            {"input": "1.1.1", "expected": [1, 1, 1]},
            {"input": "1.1.1.1", "expected": [1, 1, 1, 1]},
            {"input": "123.0.1", "expected": [123, 0, 1]},
            # handles negative numerical components as strings
            {"input": "-1", "expected": ["-1"]},
            {"input": "0.-1", "expected": [0, "-1"]},
            # handles alphanumerics, hyphens & underscores in components as strings
            {"input": "a", "expected": ["a"]},
            {"input": "a.b.c", "expected": ["a", "b", "c"]},
            {"input": "1-1", "expected": ["1-1"]},
            {"input": "alpha-12.5.-", "expected": ["alpha-12", 5, "-"]},
            {"input": "1.2.3.alpha", "expected": [1, 2, 3, "alpha"]},
            {"input": "2013-03-21_01-53-17", "expected": ["2013-03-21_01-53-17"]},
        ]

        for tc in test_cases:
            with self.subTest(input_str=tc["input"]):
                self.assertEqual(
                    VersionSegment.parse(tc["input"]).components, tc["expected"]
                )

    def test_parse_raises_errors(self):
        test_cases = [
            {"input": "", "expected": ValueError},
            {"input": "+", "expected": ParseError},
            {"input": "&", "expected": ParseError},
            {"input": " ", "expected": ParseError},
            {"input": "\u6666", "expected": ParseError},
            {"input": "1.\u6666", "expected": ParseError},
        ]

        for tc in test_cases:
            with self.subTest(input_str=tc["input"]):
                with self.assertRaises(tc["expected"]):
                    VersionSegment.parse(tc["input"])

    def test_version_segment(self):

        # saves the supplied components
        components = [1, 2, 3]
        self.assertEqual(VersionSegment(components).components, components)

        test_cases = [
            ([], ValueError),
            ([""], ValueError),
            ([0, ""], ValueError),
            ([1.1], ValueError),
            ([True], ValueError),
            ([[]], ValueError),
        ]

        for (input_list, expected) in test_cases:
            with self.assertRaises(expected):
                VersionSegment(input_list)

    def test_str(self):
        test_cases = [
            ([1], "1"),
            ([1, 1, 1, 1], "1.1.1.1"),
            ([1, "a", 0, 0], "1.a.0.0"),
        ]

        for (components, expected) in test_cases:
            with self.subTest(components=components):
                self.assertEqual(str(VersionSegment(components)), expected)

    def test_increment(self):
        # increases the least significant component by default
        test_cases = [
            ([1], [2]),
            ([1, 1, 1, 1], [1, 1, 1, 2]),
            ([1, "a", 0, 0], [1, "a", 0, 1]),
        ]

        for (components, expected) in test_cases:
            with self.subTest(components=components):
                self.assertEqual(
                    VersionSegment(components).increment().components, expected
                )

        # it raises a TypeError if the specified index is not an integer
        test_cases = [
            (["a"], TypeError),
            ([1, 1, 1, "a"], TypeError),
            ([0, "-1"], TypeError),
        ]

        for (components, expected) in test_cases:
            with self.subTest(components=components):
                with self.assertRaises(expected):
                    VersionSegment(components).increment()

        # resets to 0 all numeric components after the given index
        test_cases = [
            (0, [1, 1, 1], [2, 0, 0]),
            (0, [1, 1, 1, "alpha", 5], [2, 0, 0, "alpha", 0]),
            (1, [1, 1, 1], [1, 2, 0]),
            (-1, [1, 1, 1], [1, 1, 2]),
            (-2, [1, 1, 1], [1, 2, 0]),
        ]

        for (index, components, expected) in test_cases:
            with self.subTest(index=index, omponents=components):
                self.assertEqual(
                    VersionSegment(components).increment(index=index).components,
                    expected,
                )

    def test_decrement(self):
        test_cases = [
            ([1], [0]),
            ([1, 1, 1, 1], [1, 1, 1, 0]),
            ([1, "a", 0, 1], [1, "a", 0, 0]),
        ]
        for (components, expected) in test_cases:
            with self.subTest(components=components):
                self.assertEqual(
                    VersionSegment(components).decrement().components, expected
                )

        # raises a TypeError if the specified index is not an integer
        test_cases = [["a"], [1, 1, 1, "a"], [0, "-1"]]

        for components in test_cases:
            with self.subTest(components=components):
                with self.assertRaises(TypeError):
                    VersionSegment(components).decrement()

        # raises a ValueError if the specified index is zero or less
        test_cases = [[0], [1, 1, 1, "a", 0], [0, "-1", 0], [-1]]

        for components in test_cases:
            with self.subTest(components=components):
                with self.assertRaises(ValueError):
                    VersionSegment(components).decrement()

    def test_eq(self):
        self.assertNotEqual(VersionSegment.parse("1.0.1"), None)

        # assume appended zeros
        test_cases = [
            ([0], [0, 0]),
            ([1, 0], [1, 0, 0, 0]),
            ([1, 2, 3], [1, 2, 3, 0]),
            (["a"], ["a", 0]),
        ]

        for (components, expected) in test_cases:
            with self.subTest(components=components):
                self.assertEqual(VersionSegment(components), VersionSegment(expected))

    def test_lt(self):
        test_cases = [([0], [1, 0]), ([1, 1], [1, 1, 1])]
        for (components, expected) in test_cases:
            with self.subTest(components=components):
                self.assertLess(VersionSegment(components), VersionSegment(expected))

    def test_cmp_integers(self):
        self.assertEqual(VersionSegment([1]), VersionSegment([1]))
        self.assertLess(VersionSegment([1]), VersionSegment([2]))
        self.assertLess(VersionSegment([0]), VersionSegment([1]))
        self.assertLess(VersionSegment([1, 2, 3]), VersionSegment([1, 2, 4]))

    def test_cmp_alphanumeric(self):
        self.assertEqual(VersionSegment(["a"]), VersionSegment(["a"]))

        self.assertLess(VersionSegment(["alpha", 1]), VersionSegment(["beta", 1]))
        self.assertLess(VersionSegment(["123ab"]), VersionSegment(["123abc"]))

        self.assertLess(VersionSegment(["a"]), VersionSegment(["a", 1]))

        self.assertLess(
            VersionSegment(["2013-03-21_01-53-17"]),
            VersionSegment(["2013-03-21_12-00-00"]),
        )

    def test_cmp_numbers_lower_than_alpha(self):
        self.assertLess(VersionSegment([1]), VersionSegment(["a"]))
        self.assertLess(VersionSegment([1, 0]), VersionSegment([1, "a"]))
