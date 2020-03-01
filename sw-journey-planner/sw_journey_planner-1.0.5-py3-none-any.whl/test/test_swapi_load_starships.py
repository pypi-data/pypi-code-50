import unittest
from sw_journey_planner.swapi import load_starships
import responses


class TestSwapiLoadStarships(unittest.TestCase):
    @responses.activate
    def test_loads_starships(self):
        json_response = ({
            "next": "null",
            "results": [
                {
                    "name": "Executor",
                    "consumables": "6 years",
                    "MGLT": "40"
                }
            ]
        })
        # Using responses package to stub requests.get
        responses.add(responses.GET, "https://swapi.co/api/starships",
                      json=json_response, status=200)

        # Get the first item from the generator function
        starship = next(load_starships())

        with self.subTest("instance exists"):
            self.assertIsNotNone(starship)

        with self.subTest("mglt equals 40"):
            self.assertEqual(40, starship._mglt)

        with self.subTest("consumables equals 52560"):
            self.assertEqual(52560, starship._consumables)

        with self.subTest("name is Executor"):
            self.assertEqual(40, starship._mglt)

    @responses.activate
    def test_load_starships_throws_exception(self):

        # Using responses package to stub requests.get
        responses.add(responses.GET, "https://swapi.co/api/starships",
                      json=None, status=404)

        # Get the first item from the generator function
        load_starships()

        with self.assertRaises(Exception) as he:
            self.assertEqual("Unable to load starships from Swapi. HTTP Error: 404", he.exception)