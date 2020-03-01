# -*- coding: utf-8 -*-
"""Rubix :class:`Cube <rubix_cube.cube.Cube` class :mod:`tests` Module

Module Description
==================


Module Contents
===============

.. moduleauthor:: David Grethlein <djg329@drexel.edu>

"""

import copy
import unittest

from ..cube import Cube
from ..cube_game import Cube_Game


class TestCubeGameMethods(unittest.TestCase):

    def test_up(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('U')
        cg.manipulate_cube('Ui')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_equator(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('E')
        cg.manipulate_cube('Ei')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_down(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('D')
        cg.manipulate_cube('Di')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_left(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('L')
        cg.manipulate_cube('Li')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_middle(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('M')
        cg.manipulate_cube('Mi')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_right(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('R')
        cg.manipulate_cube('Ri')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_front(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('F')
        cg.manipulate_cube('Fi')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_standing(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('S')
        cg.manipulate_cube('Si')
        self.assertEqual(copy_cube , cg.game_cube)


    def test_back(self):
        cg = Cube_Game()
        seq = Cube_Game.get_scramble_sequence()
        for mv in seq:
            cg.manipulate_cube(mv)

        copy_cube = copy.deepcopy(cg.game_cube)
        cg.manipulate_cube('B')
        cg.manipulate_cube('Bi')
        self.assertEqual(copy_cube , cg.game_cube)


if __name__ == '__main__':
    unittest.main()