"""
    Handles the Game's Input Output
"""

import os
import json
import urllib.request

import numpy as np

from .game import Universe


class Runner:
    """
        Handles loading of the game and
        interations with user

        Parameters
        ----------
        data_path: str
            - absolute path to the pattern files
    """

    def __init__(self, data_path='game_of_life/.data/'):
        self.load_config()
        if not os.path.exists(data_path):
            os.mkdir(data_path)
            print('Fetching patterns...Just a moment\n')
            self.get_patterns()
        self.data_path = data_path

    def get_patterns(self):
        """
            Retrieves stored patterns
        """

        file_names = self.cfg.get('patterns')
        req = f'https://raw.githubusercontent.com/' +\
            'hogum/game-of-life/master/game_of_life/.data/'

        for file_name in file_names:
            with open(f'game_of_life/.data/{file_name}', 'w'):
                pass

            urllib.request.urlretrieve(
                req + file_name, f'game_of_life/.data/{file_name}')

    def run(self, n_evolutions=100, pause=.1):
        """
            Initializes the game.

            Paramaters
            ----------
            n_evolutions: int
                - Number of generations to evolve
            pause: float | (default = .1)
                - Duration in seconds to pause while printing
                  each generation
        """
        from time import sleep

        world = Universe(random=False)
        pattern_name = self._prompt_user()
        pattern = self.init_pattern(pattern_name)
        n_evolutions, pause, print_Xs = self.cfg.get(
            'evolutions'), self.cfg.get(
            'delay_interval'), self.cfg.get('display_X')

        for i in range(n_evolutions):
            world.evolve(pattern)
            print(f'\nGeneration: {i}')
            with np.printoptions(threshold=np.inf, linewidth=np.inf):

                if print_Xs:
                    # This part gives the user the option to
                    # print X | . instead of 0 | 1 at the
                    # expense of recopying each generation

                    ptn = pattern.copy()
                    ptn = ptn.astype(np.str)
                    ptn[ptn == '0'] = '.'
                    ptn[ptn == '1'] = 'X'
                    str_array = [[''.join(x)] for x in ptn]
                    print(np.asarray(str_array))
                else:
                    print(world)
            sleep(pause)

    def _prompt_user(self):
        """
            Handles the user interface.
            Requests the user for the pattern to be used
            in initializing the game.
        """
        import platform
        import subprocess

        choices = []

        if platform.system().lower().startswith('win'):
            clear_scr = 'clr'
        else:
            clear_scr = 'clear'
        try:
            subprocess.run(clear_scr, check=True)
        except subprocess.CalledProcessError:
            ...

        print('\n\t\t\t-------------------------------------------')
        print('\n\t\t\t\t\tGAME of LIFE')
        print('\n\t\t---------------------------------' +
              '---------------------------')
        print('\tThe Game of Life is best played while sipping' +
              ' coffee amid soothing sounds of a Spanish lullaby', '\n')
        print('Ready to rock:)?', ' [y/n]', end=' ')
        ans = input().lower()

        while not ans or ans not in ('y', 'n'):
            ans = input()
        if ans.startswith('n'):
            exit(0)

        print('\nAlright!!', 'Select a pattern from one of these below\n')

        available_patterns = self.cfg.get('patterns')

        for i, ptn in enumerate(available_patterns):
            print(f'{i + 1}.  {ptn}')
            choices += [str(i + 1)]

        print('\nDo I envy the fun you are about to have? Answer? Yes!')
        print(' **[Remember to maximize terminal window for infinite fun]**')
        print('Your choice (e.g 1) ->', end=' ')
        choice = input()

        while not choice or choice not in choices:
            print(
                f'\nOopsy, {choice} not in the choices.' +
                ' Just smile and try again')
            choice = input('Your choice -> ')
        print('Starting...')

        return available_patterns[int(choice) - 1]

    def load_config(self):
        """
            Loads the JSON game config data
        """
        cfg_path = 'game_of_life/../config.json'
        if not os.path.exists(cfg_path):
            with open('config.json', 'w'):
                pass

            urllib.request.urlretrieve(
                    'https://raw.githubusercontent.com/hogum/game-of-life/master/config.json',
                    'config.json')

        with open('config.json', 'r') as cfg:
            cfg_data = json.load(cfg)
        self.cfg = cfg_data

    def init_pattern(self, pattern_name):
        """
            Converts a given GOL pattern in text format
            to an array
        """
        short_blocks = ['beacon', 'glider', 'bee_hive',
                        'blinker', 'block', 'toad', 'tub']
        trim_size = self.cfg.get('trim_size')

        path = os.path.join(self.data_path, pattern_name)
        pattern = []
        with open(path) as f:
            line = f.readline()
            while line:
                ln = list(line)[:-1]
                length = len(ln)

                #  Shorten size for short blocks
                if trim_size and(length > trim_size and
                                 pattern_name in short_blocks):
                    idx = (length - trim_size / 2) // 2
                    ln = ln[idx:-idx - 1].copy()

                pattern.append(list(ln)[:-1])
                line = f.readline()
        pattern = np.asanyarray(pattern)

        pattern[pattern == '.'] = 0
        pattern[pattern == 'X'] = 1

        pattern = pattern.astype(np.int64, copy=False)
        check = pattern[(pattern != 1) & (pattern != 0)]
        if np.any(check):
            raise ValueError(
                'Found invalid characters in pattern.Use `.` and `X`')
        return pattern
