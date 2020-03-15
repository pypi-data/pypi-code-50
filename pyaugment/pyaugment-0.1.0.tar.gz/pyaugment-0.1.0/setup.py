# Copyright (c) 2020 smarsu. All Rights Reserved.

"""
```sh
python setup.py sdist
twine upload dist/*
```
"""

import os
from setuptools import find_packages, setup


packages = find_packages()

setup(
  name = 'pyaugment',
  version = '0.1.0',
  packages = packages,
  install_requires = [
      'numpy',
      'opencv-python',
  ],
  author = 'smarsu',
  author_email = 'smarsu@foxmail.com',
  url='https://github.com/smarsu/augment',
  zip_safe = False,
)