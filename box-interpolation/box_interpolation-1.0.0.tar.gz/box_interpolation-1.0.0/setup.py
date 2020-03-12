from setuptools import setup, Extension

import numpy

USE_CYTHON = False
VERSION = '1.0.0'

if USE_CYTHON:
    try:
        from Cython.Build import cythonize
    except ImportError:
        USE_CYTHON = False
        cythonize = None
else:
    cythonize = None

ext = '.pyx' if USE_CYTHON else '.c'

include_dirs = []
extensions = [Extension('box_interpolation', [f'box_interpolation{ext}'],
              include_dirs=[numpy.get_include()])]

if USE_CYTHON:
    extensions = cythonize(extensions)
    include_dirs = [numpy.get_include()]


setup(
    name='box_interpolation',
    version=VERSION,
    author='Vladimir Starostin',
    author_email='vladimir.starostin@uni-tuebingen.de',
    description='Simple fast box interpolation powered by Cython.',
    # long_description_content_type='text/markdown',
    license='MIT',
    ext_modules=extensions,
    include_dirs=include_dirs,
    python_requires='>=3.6.*',
    install_requires=[
        'numpy>=1.18.1',
    ],
)
