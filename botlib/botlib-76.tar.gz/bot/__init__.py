# BOTLIB - Framework to program bots.
#
#

__version__ = 76

import bot
import bot.dft
import bot.flt
import bot.usr
import bot.krn
import time

#:
starttime = time.time()

#:
k = bot.krn.Kernel()

import bot.irc
import bot.rss
import bot.udp
