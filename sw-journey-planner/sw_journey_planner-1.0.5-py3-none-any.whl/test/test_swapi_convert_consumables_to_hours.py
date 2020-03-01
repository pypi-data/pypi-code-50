import unittest
from sw_journey_planner.swapi import _convert_consumables_to_hours


class TestSwapiConvert(unittest.TestCase):
    def test_convert_Raises(self):
        msg = "Consumables interval could not be determined"
        test_cases = [
            (1, "gear"), (3, "yearz"), (50, "mnths")
        ]
        for increment, interval in test_cases:
            with self.subTest(f"{increment} {interval} raises: {msg}"), self.assertRaises(KeyError) as ve:
                _convert_consumables_to_hours(increment, interval)
                self.assertEqual(msg, str(ve.exception))

    def test_convert_converts(self):
        test_cases = [
            (1, "week", 168),
            (1, "hour", 1),
            (2, "day", 48),
            (1, "month", 30 * 24),
            (17, "year", 17 * 365 * 24),
            (0, "week", 0),
            (0, "day", 0)
        ]
        for increment, interval, result in test_cases:
            with self.subTest(f"{increment} {interval} -> {result}"):
                self.assertEqual(result, _convert_consumables_to_hours(increment, interval))
