from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
  name = 'cambio',
  packages = ['cambio'],
  package_dir = {'cambio': 'cambio'},
  package_data = {'cambio': ['__init__.py', 'tests/__init__.py', 'tests/test.py']},
  version = "0.0.0",
  description = 'Change Python Source Code Files',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/cambio',
  download_url = 'https://github.com/DanielJDufour/cambio/tarball/download',
  keywords = ['cli', 'edit', 'modify', 'python'],
  classifiers = [
    'Development Status :: 1 - Planning',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Operating System :: OS Independent',
  ],
  install_requires=[""]
)
