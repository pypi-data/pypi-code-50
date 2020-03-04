# Loads Python classes for capabilities needed in HippoNetworkUnit

# capabilities/
# from . import cap_ProvidesCA1NeuritePathDistanceInfo
# from . import cap_Provides_CA1_laminar_distribution_synapses_info

from os.path import dirname, basename, isfile
import glob

files = glob.glob(dirname(__file__)+"/cap_*.py")
modules = [ basename(f)[:-3] for f in files if isfile(f)]

for module in modules:
    exec("from %s import *" % module)

