"""
    Game Environment test
"""
import unittest

from game_of_life.game import Universe


class TestGame(unittest.TestCase):
    """
        Handles testing of game environment
    """

    def setUp(self):
        self.world = Universe()

    def test_game_created_with_world_(self):
        """
            The game is initialized with unpopulated
        """
        self.assertIsNone(self.world.world)
