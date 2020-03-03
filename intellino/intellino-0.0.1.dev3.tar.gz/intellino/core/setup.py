from distutils.core import setup
from Cython.Build import cythonize

setup(name='neuron_cell',
      ext_modules=cythonize("neuron_cell.pyx"))
