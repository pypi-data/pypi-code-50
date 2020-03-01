# -*- coding: utf-8 -*-
"""Rubix :class:`Cube_Game` class Module

Module Description
==================

Collection of methods that define the main Rubix :class:`Cube Game <Cube_Game>`
class and how it manipulates a :class:`Cube <rubix_cube.cube.Cube>`
object, prints to console, logs a history of both moves and re-orientations,
scrambles the state of the cube, times game-play, and performs file-system
loading and saving of games.


Module Contents
===============

    *   :class:`Cube_Game` details code for manipulating :class:`Rubix
        Cube(s) <rubix_cube.cube.Cube>`.

        .. todo::

           *    Implement file I/O operations (loading and saving games).
           *    Implement scramble cube functions.
           *    Implement color changing functions.
           *    Implement game clock functions.


.. moduleauthor:: David Grethlein <djg329@drexel.edu>

"""

from pathlib import Path
from random import randint , randrange

import os
import sys
import json

import warnings

from typing import List, Tuple, Dict

import numpy as np

from .cube import Cube


class Cube_Game(object):
    """Class in charge of directly interacting with and logging changes to
    an instance of the :class:`Cube` class.

    Attributes:
        EVENT_TYPES (List[str]): Description
        __game_cube (Cube): :class:`Rubix Cube <Cube>` that is manipulated
            throughout game-play.
        __game_log (dict): Historical record of all moves, rotations, and other
            game events that manipulate the :attr:`game_cube`.
        __game_name (str): Name of the game.
        __verbose (bool): [DEBUG]-style console output. Default value is
            ``False``.

    """

    #==========================================================================
    #       CONSTANTS FOR CUBE GAME(s)
    #==========================================================================
    EVENT_TYPES = ['<<__NEW_GAME__>>',
                   'F',
                   'Fi',
                   'B',
                   'Bi',
                   'L',
                   'Li',
                   'R',
                   'Ri',
                   'U',
                   'Ui',
                   'D',
                   'Di',
                   'M',
                   'Mi',
                   'E',
                   'Ei',
                   'S',
                   'Si',
                   'X',
                   'Xi',
                   'Y',
                   'Yi',
                   'Z',
                   'Zi',
                   '<<__START_SCRAMBLE__>>',
                   '<<__END_SCRAMBLE__>>',
                   '<<__COLOR_CHANGE__>>',
                   '<<__SAVE_GAME__>>',
                   '<<__LOAD_GAME__>>',
                   '<<__PAUSE_GAME__>>',
                   '<<__RESUME_GAME__>>',
                   '<<__SOLVE_CUBE__>>',
                   '<<__QUIT_GAME__>>']


    CUBE_FUNCS = {'U'  : Cube.move_up,
                  'Ui' : Cube.move_up_inverse,
                  'D'  : Cube.move_down,
                  'Di' : Cube.move_down_inverse,
                  'L'  : Cube.move_left,
                  'Li' : Cube.move_left_inverse,
                  'R'  : Cube.move_right,
                  'Ri' : Cube.move_right_inverse,
                  'F'  : Cube.move_front,
                  'Fi' : Cube.move_front_inverse,
                  'B'  : Cube.move_back,
                  'Bi' : Cube.move_back_inverse,
                  'M'  : Cube.move_middle,
                  'Mi' : Cube.move_middle_inverse,
                  'E'  : Cube.move_equator,
                  'Ei' : Cube.move_equator_inverse,
                  'S'  : Cube.move_standing,
                  'Si' : Cube.move_standing_inverse,
                  'X'  : Cube.rotate_pitch,
                  'Xi' : Cube.rotate_pitch_inverse,
                  'Y'  : Cube.rotate_yaw,
                  'Yi' : Cube.rotate_yaw_inverse,
                  'Z'  : Cube.rotate_roll,
                  'Zi' : Cube.rotate_roll_inverse}

    INVERSE_FUNCS = {'U'  : 'Ui',
                     'Ui' : 'U',
                     'D'  : 'Di',
                     'Di' : 'D',
                     'L'  : 'Li',
                     'Li' : 'L',
                     'R'  : 'Ri',
                     'Ri' : 'R',
                     'F'  : 'Fi',
                     'Fi' : 'F',
                     'B'  : 'Bi',
                     'Bi' : 'B',
                     'M'  : 'Mi',
                     'Mi' : 'M',
                     'E'  : 'Ei',
                     'Ei' : 'E',
                     'S'  : 'Si',
                     'Si' : 'S',
                     'X'  : 'Xi',
                     'Xi' : 'X',
                     'Y'  : 'Yi',
                     'Yi' : 'Y',
                     'Z'  : 'Zi',
                     'Zi' : 'Z'}

    #==========================================================================
    #       CLASS CONSTRUCTOR
    #==========================================================================
    def __init__(self,
                 cube : Cube = None,
                 game_name : str = None,
                 game_log : Dict = None,
                 scramble : bool = False,
                 verbose : bool = False):
        """:class:`Cube_Game` class constructor

        Args:
            cube (Cube, optional): :class:`Cube` that will be directly
                manipulated throughout gameplay.
            game_name (str, optional): Name of the current game being played.
            game_log (Dict, optional): Dictionary that contains a history of
                moves and other game events.
            scramble (bool, optional): Whether or not the game should scramble
                the :attr:`__game_cube` upon initialization. Default value is
                ``False``.
            verbose (bool, optional): [DEBUG]-style console output. Default
                value is ``False``.

        """

        # Sets Up Default Game
        self.game_name = 'Untitled_Cube_Game'
        self.game_name = game_name
        self.game_cube = Cube()
        self.game_log = {'events' : [{'type' : '<<__NEW_GAME__>>',
                              'name' : self.game_name}]}

        # Attempts to reset property values with argument values.
        self.game_cube = cube
        self.game_log = game_log
        self.verbose = verbose

        # Initializes a default cube
        if self.game_cube == Cube():

            if self.verbose:
                print(f"\n[DEBUG]\tNew DEFAULT Cube created for game : '{self.game_name}'\n")

        # Initializes a default game log
        if self.game_log != game_log:

            if self.verbose:
                print(f"\n[DEBUG]\tNew DEFAULT ``game_log`` created for game : '{self.game_name}'\n")

        else:
            self.game_log['events'].append({'type' : '<<__NEW_GAME__>>',
                                            'name' : self.game_name})

            if self.verbose:
                print(f"\n[DEBUG]\tNew game created with name : '{self.game_name}'\n")


    #==========================================================================
    #       PROPERTY INTERFACE(s)
    #==========================================================================
    @property
    def game_cube(self) -> Cube:
        """:class:`Rubix Cube <Cube>` object being manipulated in game.
        """
        return self.__game_cube


    @game_cube.setter
    def game_cube(self , cube : Cube):
        if isinstance(cube, Cube)\
        and cube.is_well_formed():

            self.__game_cube = cube


    @property
    def game_name(self) -> str:
        """Name of the Game
        """
        return self.__game_name


    @game_name.setter
    def game_name(self, name : str):
        if isinstance(name, str)\
        and len(name) > 0:

            self.__game_name = name


    @property
    def game_log(self) -> Dict:
        """JSON-style :class:`dict` recording all actions done to
        the :attr:`game_cube` stored under the ``events`` key which is a list
        of :class`dict` objects each of which has a ``type`` key with a value
        found in :attr:`EVENT_TYPES`.

        .. code-block::
           :name: game_log_EVENT_TYPES
           :linenos:
           :caption: Potential values of ``type`` in :attr:`game_log`.

           EVENT_TYPES = ['<<__NEW_GAME__>>',
                          'F',
                          'Fi',
                          'B',
                          'Bi',
                          'L',
                          'Li',
                          'R',
                          'Ri',
                          'U',
                          'Ui',
                          'D',
                          'Di',
                          'M',
                          'Mi',
                          'E',
                          'Ei',
                          'S',
                          'Si',
                          'X',
                          'Xi',
                          'Y',
                          'Yi',
                          'Z',
                          'Zi',
                          '<<__START_SCRAMBLE__>>',
                          '<<__END_SCRAMBLE__>>',
                          '<<__COLOR_CHANGE__>>',
                          '<<__SAVE_GAME__>>',
                          '<<__LOAD_GAME__>>',
                          '<<__PAUSE_GAME__>>',
                          '<<__RESUME_GAME__>>',
                          '<<__SOLVE_CUBE__>>',
                          '<<__QUIT_GAME__>>']

        .. code-block::
           :name: game_log
           :linenos:
           :caption: Required ``game_log`` dictionary keys.

           game_log = {'events' : [{'type' : '<<__NEW_GAME__>>',
                                    'name' : '...'},
                                   {'type' : ...},
                                   ...,
                                   {'type' : ...}]}
        """
        return self.__game_log


    @game_log.setter
    def game_log(self, game_log : Dict):
        if isinstance(game_log, dict)\
        and 'events' in game_log\
        and isinstance(game_log['events'], list)\
        and len(game_log['events']) > 0\
        and all([isinstance(event, dict) for event in game_log['events']]):

            # Has to ensure that all event types are valid
            valid_log = all(['type' in event\
                             and event['type'] in Cube_Game.EVENT_TYPES\
                                for event in game_log['events']])

            if valid_log:
                self.__game_log = game_log


    @property
    def verbose(self) -> bool:
        """[DEBUG]-style console output. Default value is ``False``.
        """
        return self.__verbose


    @verbose.setter
    def verbose(self, verbose : bool):
        if isinstance(verbose, bool):
            self.__verbose = verbose
        else:
            self.__verbose = False


    #==========================================================================
    #       GAME-PLAY METHOD(s)
    #==========================================================================
    def manipulate_cube(self, cube_func : str):
        """Function that interfaces the :class:`Cube_Game` class with the
        :class:`Cube` class to turn the layers or rotate the orientation.

        Args:
            cube_func (str): Look-up key to recover the proper :class:`Cube`
                method to call from :attr:`CUBE_FUNCS` class attribute to call
                a move using the :attr:`game_cube`.

        .. code-block::
           :name: move_cube_CUBE_FUNCS
           :linenos:
           :caption: Parameter ``cube_func`` will determine which
                :attr:`game_cube` move function is called. If not found,
                nothing happens.

           CUBE_FUNCS = {'U'  : Cube.move_up,
                         'Ui' : Cube.move_up_inverse,
                         'D'  : Cube.move_down,
                         'Di' : Cube.move_down_inverse,
                         'L'  : Cube.move_left,
                         'Li' : Cube.move_left_inverse,
                         'R'  : Cube.move_right,
                         'Ri' : Cube.move_right_inverse,
                         'F'  : Cube.move_front,
                         'Fi' : Cube.move_front_inverse,
                         'B'  : Cube.move_back,
                         'Bi' : Cube.move_back_inverse,
                         'M'  : Cube.move_middle,
                         'Mi' : Cube.move_middle_inverse,
                         'E'  : Cube.move_equator,
                         'Ei' : Cube.move_equator_inverse,
                         'S'  : Cube.move_standing,
                         'Si' : Cube.move_standing_inverse,
                         'X'  : Cube.rotate_pitch,
                         'Xi' : Cube.rotate_pitch_inverse,
                         'Y'  : Cube.rotate_yaw,
                         'Yi' : Cube.rotate_yaw_inverse,
                         'Z'  : Cube.rotate_roll,
                         'Zi' : Cube.rotate_roll_inverse}
        """

        if cube_func in Cube_Game.CUBE_FUNCS\
        and self.game_cube.is_well_formed():

            # Performs the desired cube move on the game cube
            Cube_Game.CUBE_FUNCS[cube_func](self.game_cube)

            if self.verbose:
                print(f"[DEBUG]\tCalling game cube function: '{cube_func}'")
                print(f"\t\tNum Matching Adjacent Tiles : {self.game_cube.get_num_matching_adjacent_tiles()}")

            self.game_log['events'].append({'type' : cube_func})


    def get_scramble_sequence(n_steps : int = 50,
                              cube_funcs : List[str] = None) -> List[str]:
        """Compiles a sequence of moves for scrambling the :attr:`game_cube`
        attribute for applying a sequence of ``n_steps`` semi-randomly selected
        cube manipulations using a defined a provided sub-set of cube functions
        ``cube_funcs``.

        Args:
            n_steps (int, optional): The number of :class:`Rubix Cube <Cube>`
                manipulations to be applied to the :attr:`game_cube`.

                Note:
                    Valid range of values, 0 < ``n_steps`` <= 500. Won't
                    call any :class:`Cube` function(s) if not in range.

            cube_funcs (List[str], optional): Sub-list of :attr:`CUBE_FUNCS`
                that defines the options for manipulating the cube. Default
                value is ``None`` which allows all functions in
                :attr:`CUBE_FUNCS` to be selected.

        Returns:
            List[str]: **sequence** - A list of cube manipulation function
            str(s) for use with :func:`manipulate_cube` function.

        Note:
            Won't perform the following sequences:

            *   ``<<ACTION>>`` , ``<<ACTION_INVERSE>>``
            *   ``<<ACTION>>``, ``<<ACTION>>``, ``<<ACTION>>``, ``<<ACTION>>``

            .. code-block::
               :name: scramble_cube_INVERSE_FUNCS
               :linenos:
               :caption: :class:`Cube_Game` static :attr:`INVERSE_FUNCS` attribute
                    for looking up the inverse function for each potential cube
                    manipulation.

               INVERSE_FUNCS = {'U'  : 'Ui',
                                'Ui' : 'U',
                                'D'  : 'Di',
                                'Di' : 'D',
                                'L'  : 'Li',
                                'Li' : 'L',
                                'R'  : 'Ri',
                                'Ri' : 'R',
                                'F'  : 'Fi',
                                'Fi' : 'F',
                                'B'  : 'Bi',
                                'Bi' : 'B',
                                'M'  : 'Mi',
                                'Mi' : 'M',
                                'E'  : 'Ei',
                                'Ei' : 'E',
                                'S'  : 'Si',
                                'Si' : 'S',
                                'X'  : 'Xi',
                                'Xi' : 'X',
                                'Y'  : 'Yi',
                                'Yi' : 'Y',
                                'Z'  : 'Zi',
                                'Zi' : 'Z'}

        """

        # Default length for sequence of random moves to be generated
        if not isinstance(n_steps, int)\
        or not (n_steps > 0 and n_steps <= 500):
            n_steps = 0

        # Default list of cube functions is all of them
        if not isinstance(cube_funcs , list)\
        or not all([func in Cube_Game.CUBE_FUNCS for func in cube_funcs]):
            cube_funcs = list(Cube_Game.CUBE_FUNCS.keys())

        sequence = []

        while len(sequence) < n_steps:

            # Generates a random choice from the current options
            # of potential cube-functions to call
            choice_func = cube_funcs[randrange(len(cube_funcs))]

            if len(sequence) == 0:
                sequence.append(choice_func)
            else:
                last_func = sequence[-1]

                # No <<FUNCTION>> , <<INVERSE_FUNCTION>> sub-sequences
                if last_func == Cube_Game.INVERSE_FUNCS[choice_func]:
                    continue

                if len(sequence) > 2:

                    last_three = sequence[-3:]

                    # No 4 of the same function in a row
                    if all([func == choice_func for func in last_three]):
                        continue

            sequence.append(choice_func)

        return sequence


    def compute_inverse_log_sequence(self) -> List[str]:
        """Computes the inverse sequence of moves from the :attr:`game_log`
        that ``SHOULD`` lead to the :class:`Rubix Cube <rubix_cube.cube.Cube>`
        being solved!

        Returns:
            List[str]: **sequence** - A list of cube manipulation function
            str(s) for use with :func:`manipulate_cube` function.

        """

        # Ensures the game is valid
        if self.game_cube.is_well_formed()\
        and isinstance(self.game_log, dict)\
        and 'events' in self.game_log:

            # Gets a reversed list of all log event types
            event_types = [event['type'] for event in\
                                            np.flip(self.game_log['events'])]

            # Filters down to cube-moves only
            log_moves = list(filter(lambda e_type: e_type in\
                                            Cube_Game.INVERSE_FUNCS,
                                            event_types))

            # Computes the inverse sequence
            sequence = [Cube_Game.INVERSE_FUNCS[mv] for mv in log_moves]

            return sequence



