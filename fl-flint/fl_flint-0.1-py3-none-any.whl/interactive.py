"""
Copyright (C) 2016, 2017, 2020 biqqles.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

This file provides an interactive prompt for working with flint
(and therefore a Freelancer installation). Run with `python -i`,
e.g. `python -i interactive.py -I "<freelancer_dir>"`.
"""
import argparse
import os
import sys

# override interpreter prompts
sys.ps1 = '(flint as fl) >>> '
sys.ps2 = '              ... '

parser = argparse.ArgumentParser(description='flair, a tool for freelancer')
parser.add_argument('-I', '--install-path', help='Path to Freelancer\'s install directory', required=True)
parser.add_argument('-d', '--discovery', help='Whether Freelancer installation is Discovery-modded.', default=False)
parser.add_argument('-c', '--cache-expiry', help='Description for bar argument')
args = vars(parser.parse_args())

# noinspection PyBroadException
import flint as fl
fl.paths.set_install_path(args['install_path'], args['discovery'])
