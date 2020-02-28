#!/usr/bin/env python3
"""
This in example of how to tweak the (default) settingss of musicraft.
Here a timidity port is selected for MIDI output. This can be useful when
the default woudl otherwise be a non-existent 'real' MIDI port.

Copyright 2020 Larry Myerscough
"""
from musicraft.__main__ import deal_with_keywords, main
from musicraft.abcraft import AbcRaft

from musicraft.abcraft.midiplayer import MidiPlayer  # prepare to tweak default Midi setting
#
# enable andmaybe the following line if more tweaking code is needed.
# from musicraft.abcraft.external import Abc2midi, Abcm2svg, Abc2abc

# parse keyword arguments in the same way as if we were called with 'python -m musicraft...' ...
#
deal_with_keywords()
#
# .. but before launching into musicraft, first tweak the odd setting:
#
# avoid the 'readl' MIDI port in favour of a Timidity synthesise port:
#
# comment this line out if you want to stick with default midi output.
MidiPlayer.outputPort = 'TiMidity port 0'

# Below are examples of how to further 'doctor' the behaviour of musicraft.
# This can be handy if e.g. you've installed a newer version of abcm2ps than that on the standard path.
#
# Abc2midi.exec_dir = '/usr/local/bin/'
# Abc2midi.reMsg = r'.*in\s+line-char\s(\d+)\-(\d+).*'
#
# now call the 'raft' with just the 'musicraft' plugin; other optional experimental plugins are currently disabled.
#
main(
    Plugins=(AbcRaft,
           #  PyRaft,
           #  FreqRaft,
             )
)
