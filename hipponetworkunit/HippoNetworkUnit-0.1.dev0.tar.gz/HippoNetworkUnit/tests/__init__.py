# Loads Python classes for validation-tests to be used in HippoNetworkUnit

# tests/
# from . import test_CA1_laminar_distribution_synapses
# from . import test_CA1Layers_NeuritePathDistance_MeanSD
from os.path import dirname, basename, isfile
import glob

files = glob.glob(dirname(__file__)+"/test_*.py")
modules = [ basename(f)[:-3] for f in files if isfile(f)]

for module in modules:
    exec("from %s import *" % module)
