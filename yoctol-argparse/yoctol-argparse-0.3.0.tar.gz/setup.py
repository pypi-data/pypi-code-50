import os
from pathlib import Path

from setuptools import setup, find_packages


readme = Path(__file__).parent.joinpath('README.md')
if readme.exists():
    with readme.open() as f:
        long_description = f.read()
else:
    long_description = '-'


here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'yoctol_argparse', '__version__.py'), 'r') as filep:
    exec(filep.read(), about)


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    packages=find_packages(),
    author=about['__author__'],
    author_email='jsaon@yoctol.com',
    url='',
    license='MIT',
    install_requires=[],
)
