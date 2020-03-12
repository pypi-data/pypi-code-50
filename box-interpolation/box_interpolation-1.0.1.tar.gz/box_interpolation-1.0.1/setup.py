from setuptools import setup, Extension
from pathlib import Path

import numpy

USE_CYTHON = False
VERSION = '1.0.1'


def read(filename: str):
    with open(Path(__file__).parent / filename, mode='r', encoding='utf-8') as f:
        return f.read()


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
    long_description_content_type='text/markdown',
    license='MIT',
    long_description=read('README.md'),
    ext_modules=extensions,
    include_dirs=include_dirs,
    include_package_data=True,
    python_requires='>=3.6.*',
    install_requires=[
        'numpy>=1.18.1',
    ],
    keywords='non-grid interpolation box_interpolation cython',
    url='https://pypi.org/project/box_interpolation/',
)
