# BOTLIB - Framework to program bots.
#
#

__version__ = "72"

import bot
import bot.dft
import bot.flt
import bot.krn
import bot.usr
import time

starttime = time.time()
kernels = bot.krn.Kernels()

def kernel():
    return kernels.get_first()
