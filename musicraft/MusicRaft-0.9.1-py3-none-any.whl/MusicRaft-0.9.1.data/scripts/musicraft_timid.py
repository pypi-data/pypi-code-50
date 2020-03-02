#!python
"""
This in example of how to tweak the (default) settingss of musicraft.
Here a timidity port is selected for MIDI output. This can be useful when
the default woudl otherwise be a non-existent 'real' MIDI port.

Copyright 2020 Larry Myerscough
"""

# import the code of the plugins we intend to launch 'on the raft':
from musicraft.abcraft import AbcRaft  # , PyRaft, PyRaft
#---------------------------------------------------
# import the code to start 'the raft':
from musicraft.raft import main
#---------------------------------------------------
# but first let's do some tweaking...

#---------------------------------------------------
# select a specific MIDI output port name
from musicraft.abcraft.midiplayer import MidiPlayer
MidiPlayer.outputPort = 'TiMidity port 0'
#  comment the above two lines out if you want to stick with default midi output.
#---------------------------------------------------
#
#---------------------------------------------------
# enable the following lines to select a different directory for the abc2midi program.
# from musicraft.abcraft.external import Abc2midi
# Abc2midi.exec_dir = '/usr/local/bin/'
# ... and maybe tweak the way musicraft parses the output of abc2mdi ...
# Abc2midi.reMsg = r'.*in\s+line-char\s(\d+)\-(\d+).*'
#---------------------------------------------------

#---------------------------------------------------
# enable the following lines to select a different docking scheme
# for the variouso components of 'the raft'.
# from musicraft import QtCore, EditBook, StdBook, DisplayBook
# EditBook.whereToDock = QtCore.Qt.RightDockWidgetArea
#StdBook.whereToDock = QtCore.Qt.RightDockWidgetArea
# DisplayBook.whereToDock = QtCore.Qt.LeftDockWidgetArea


#---------------------------------------------------
# now call the 'raft' with just the 'musicraft' plugin; other optional experimental plugins are currently disabled.
#
main(
    Plugins=(AbcRaft,
           #  PyRaft,
           #  FreqRaft,
             )
)
