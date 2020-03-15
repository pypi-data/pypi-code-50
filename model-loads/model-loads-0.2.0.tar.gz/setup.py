#!/usr/bin/env python
import os
import sys
from distutils.core import setup

from setuptools import find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def setup_package():
    src_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    # The f2py scripts that will be installed
    # if sys.platform == 'win32':
    #     raise Exception("Not support windows pytorch yet!")
    #
    # else:
    setup(name='model-loads',
          version='0.2.0',
          long_description=long_description,  # Optional
          long_description_content_type='text/markdown',  # Optional (see note above)

          url='https://github.com/cwh94/model_loads',  # Optional
          description='Loads GPU or CPU pytorch models',
          author='wangchao',
          author_email='chaowanghs@gmail.com',
          packages=find_packages(),
          )


if __name__ == "__main__":
    setup_package()
