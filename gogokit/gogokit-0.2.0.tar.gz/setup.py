try: 
   from setuptools import setup 
except ImportError: 
   from distutils.core import setup 

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gogokit'))
from config import __version__, __pypi_packagename__

setup(
  name=__pypi_packagename__,
  version= __version__,
  author='Viagogo',
  author_email='api@viagogo.com',
  packages=['gogokit'],
  scripts=[],
  url='https://github.com/viagogo/gogokit.py',
  description='GogoKit is a lightweight, viagogo API client library for Python.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  install_requires=['requests>=2.7.0', 'uritemplate>=0.6', 'iso8601>=0.1.10', 'six>=1.9.0'],
  classifiers=[
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  license=open('LICENSE.txt').read(),
  keywords=['viagogo', 'rest', 'sdk', 'api']
)