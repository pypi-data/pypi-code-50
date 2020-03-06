from distutils.core import setup
from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
import numpy as np

numpy_include = np.get_include()

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(
        [Extension('area_py_s', ["area_py_s.py" ], depends=["area_py_s.pxd"], include_dirs=[".", numpy_include])],
        annotate=True),
)
