#!/usr/bin/env python3
"""
This in example of how to customise the (default) settings of musicraft.
The script name reflects the fact that the the only customisation in effect
concerns "Timidity", but several other possibilities are provided in
'commented out' form.
Copyright 2020 Larry Myerscough
"""

# -----------------------------------------------------------------------------
# import the code of the plugins we intend to launch 'on the raft':
from musicraft.abcraft import AbcRaft  # , PyRaft, PyRaft
# -----------------------------------------------------------------------------
# import the code to start 'the raft':
from musicraft.__main__ import main


# -----------------------------------------------------------------------------
# but first let's do some tweaking (customisation)...

# -----------------------------------------------------------------------------
# select a specific MIDI output port name (this is useful for my ubuntu setup)
from musicraft.abcraft.midiplayer import MidiPlayer
MidiPlayer.outputPort = 'TiMidity port 0'
#  comment the above two lines out if you want to stick with default midi output.
# -----------------------------------------------------------------------------
#
# -----------------------------------------------------------------------------
# # enable the following lines to select a different directory for the abc2midi program.
# from musicraft.abcraft.external import Abc2midi
# Abc2midi.exec_dir = '/usr/local/bin/'
# # ... and maybe tweak the way musicraft parses the output of abc2mdi ...
# Abc2midi.reMsg = r'.*in\s+line-char\s(\d+)\-(\d+).*'
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# # enable the following lines to select a different docking scheme
# # for the various components of 'the raft'.
# from musicraft import QtCore, EditBook, StdBook, DisplayBook
# EditBook.whereToDock = QtCore.Qt.RightDockWidgetArea
# StdBook.whereToDock = QtCore.Qt.RightDockWidgetArea
# DisplayBook.whereToDock = QtCore.Qt.LeftDockWidgetArea


# -----------------------------------------------------------------------------
# now call the 'raft' with just the 'musicraft' plugin;
# other optional experimental plugins are currently disabled.
#
main(
    Plugins=(AbcRaft,
           #  PyRaft,
           #  FreqRaft,
             )
)
