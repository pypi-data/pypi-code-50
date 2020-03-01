import unittest
from sw_journey_planner.swapi import _parse_consumables


class TestSwapiParseConsumables(unittest.TestCase):
    def test__parse_returns_tuple(self):
        test_cases = [
            ("1 year", (1, "year")),
            ("5 years", (5, "year")),
            ("1 week", (1, "week")),
            ("50 weeks", (50, "week")),
            ("170 Hours", (170, "hour")),
            ("5", (5, ""))
        ]
        for consumables, expected_parsed_consumables in test_cases:
            with self.subTest(f"{consumables} -> {expected_parsed_consumables}"):
                self.assertTupleEqual(expected_parsed_consumables, _parse_consumables(consumables))

    def test_parse_Returns_None(self):
        self.assertIsNone(_parse_consumables("unknown"))

    def test_parse_Raises(self):
        msg = "Consumables does not contain a numeric increment"
        test_cases = [
            "a year", "one year", "year"
        ]
        for consumables in test_cases:
            with self.subTest(f"{consumables} raises: {msg}"), self.assertRaises(ValueError) as ve:
                _parse_consumables(consumables)
                self.assertEqual(msg, str(ve.exception))
