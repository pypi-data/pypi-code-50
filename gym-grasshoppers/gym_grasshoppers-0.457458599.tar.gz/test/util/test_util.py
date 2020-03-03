from unittest import TestCase

from gym_grasshoppers.util import utils


class TestUtils(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def test_calculate_distance(self):
        # Distance between KDG Groenplaats & KDG Stadswaag ~= 689m low precision
        coord_groenplaats = (51.21806698712828, 4.4006359577178955)
        coord_stadswaag = (51.223671203253836, 4.40484166145324)
        self.assertAlmostEqual(utils.calculate_distance(coord_groenplaats, coord_stadswaag), 689, 0,
                               "Long distance calculation")
        # Small distance Antwerp with higher precision
        coord_left = (51.218451710824866, 4.400783479213715)
        coord_right = (51.2184399507595, 4.400826394557953)
        self.assertAlmostEqual(utils.calculate_distance(coord_left, coord_right), 3.259, 1,
                               "Small distance calculation with 10cm precision")
        # Large distance in Tasmania
        coord_tasmania_1 = (-41.44012858993289, 147.13189959526062)
        coord_tasmania_2 = (-41.44069962959139, 147.1325433254242)
        self.assertAlmostEqual(utils.calculate_distance(coord_tasmania_1, coord_tasmania_2), 83, 0,
                               "S/E Coordinates Tasmania")

    def test_calculate_radius(self):
        self.assertAlmostEqual(utils.calculate_scaled_radius(51.218451710824866, 1), 9e-06, 7)
