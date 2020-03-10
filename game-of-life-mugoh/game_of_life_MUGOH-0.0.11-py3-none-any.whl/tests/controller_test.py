"""
    Controller tests
"""
from unittest import TestCase, mock

import numpy as np

from game_of_life.controller import Runner
from game_of_life.game import Universe
from game_of_life import controller


class TesetRunner(TestCase):
    """
        Handles testing of the game environment transitions
    """

    def setUp(self):
        self.world = Universe()
        self.runner = Runner()

    def test_fail_on_invalid_path(self):
        """
            The runner should receive a valid path
            to the patterns file
        """
        invalid_path = 'not_exists'
        with self.assertRaises(TypeError):
            Runner(invalid_path)

    def test_init_pattern(self):
        """
            We should be able to read a pattern from file
            and convert it to an array
        """
        pattern = self.runner.init_pattern('glider')

        self.assertIsInstance(pattern, np.ndarray)

    def test_init_pattern_with_invalid_symbols(self):
        """

            The pattern file should be composed of only
            X and .
        """
        runner = Runner()
        runner.data_path = 'tests'
        with self.assertRaises(ValueError):
            runner.init_pattern('pattern_test')

    def test_init_non_existent_pattern(self):
        """
            To be able to initialize a pattern,
            it must be present in a given pattern file
        """
        with self.assertRaises(FileNotFoundError):
            self.runner.init_pattern('missing_pattern_file')

    def test_user_input(self):
        """
            User reply `n` on input should exit
        """
        user_input = ['', 'n']
        with self.assertRaises(SystemExit):
            with mock.patch('builtins.input', side_effect=user_input):
                self.runner._prompt_user()

    def test_user_input_yes(self):
        """
            User reply `y` on input should select a name
            for the desired game pattern.
            Selecting a non-given option should lead to
            a re-prompt
        """
        non_existent_option = 404
        user_input = ['y', non_existent_option, '', '3']
        with mock.patch('builtins.input', side_effect=user_input):
            res = self.runner._prompt_user()
        self.assertIsInstance(res, str)

    def test_run_game(self):
        """
            On successful user prompt, the game creates
            generations
        """
        m = Runner()
        m._prompt_user = mock.MagicMock(return_value = 'loaf')
        m.cfg['evolutions'] = 3
        m.run(3, 0)

