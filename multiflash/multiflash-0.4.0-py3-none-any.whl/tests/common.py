# Copyright 2020 John Reese
# Licensed under the MIT License

from unittest import TestCase

from .. import common


class CommonTest(TestCase):
    def test_find_numbers(self):
        for value, expected in (
            ("1 2 3", [1, 2, 3]),
            ("1,2,3", [1, 2, 3]),
            ("1, 2, 3, ", [1, 2, 3]),
            ("all", []),
            ("", []),
        ):
            with self.subTest(value=value):
                self.assertEqual(common.find_numbers(value), expected)

    def test_natural_case(self):
        values = [
            "Chapter 1",
            "Chapter 2",
            "Chapter 10",
            "Chapter 5",
            "Chapter 14",
            "Chapter 21",
        ]
        expected = [
            "Chapter 1",
            "Chapter 2",
            "Chapter 5",
            "Chapter 10",
            "Chapter 14",
            "Chapter 21",
        ]

        self.assertEqual(sorted(values, key=common.natural_sort), expected)
