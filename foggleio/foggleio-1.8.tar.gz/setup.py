from setuptools import setup

import io
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='foggleio',
      version='1.8',
      description='Continuous deployment has never been easy but with the help of Foggle.io you can be one step closer',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://foggle.io/',
      author='Barend Erasmus',
      author_email='hirebarend@gmail.com',
      license='MIT',
      packages=['foggleio'],
      zip_safe=False)