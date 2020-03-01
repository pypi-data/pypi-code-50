import unittest

from sw_journey_planner import Starship


class TestStarship(unittest.TestCase):

    def test_name_property(self):
        starship = Starship(mglt=10, name="ship", consumables=40)
        self.assertEqual("ship", starship.name)

    def test_journey_duration_Equal(self):
        starship = Starship(mglt=10, name="ship", consumables=40)
        self.assertEqual(10, starship._journey_duration(100))

    def test_journey_duration_Equal_0(self):
        starship = Starship(mglt=10, name="ship", consumables=40)
        self.assertEqual(0, starship._journey_duration(0))

    def test_journey_duration_NotEqual(self):
        starship = Starship(mglt=10, name="ship", consumables=40)
        self.assertNotEqual(12, starship._journey_duration(100))

    def test_journey_duration_IsNone(self):
        starship = Starship(mglt=0, name="ship", consumables=40)
        self.assertIsNone(starship._journey_duration(100))

    def test_journey_duration_NoneSpeed_IsNone(self):
        starship = Starship(mglt=None, name="ship", consumables=40)
        self.assertIsNone(starship._journey_duration(100))

    def test_plan_journey_NoneConsumables_IsNone(self):
        starship = Starship(mglt=100, name="ship", consumables=None)
        self.assertIsNone(starship.plan_journey(1000))

    def test_plan_journey_ZeroConsumables_IsNone(self):
        starship = Starship(mglt=100, name="ship", consumables=0)
        self.assertIsNone(starship.plan_journey(1000))

    def test_plan_journey_Equal(self):
        starship = Starship(mglt=1, name="ship", consumables=40)
        self.assertEqual(1, starship.plan_journey(41))

    def test_plan_journey_Equal_0(self):
        starship = Starship(mglt=100, name="ship", consumables=400)
        self.assertEqual(0, starship.plan_journey(100))

    def test_plan_journey_Equal_None(self):
        starship = Starship(mglt=0, name="ship", consumables=400)
        self.assertIsNone(starship.plan_journey(100))
