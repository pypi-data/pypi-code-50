#!/usr/bin/env python

from setuptools import setup  # type: ignore

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='fpandas',
      version='0.5',
      description='Utils toward a monad-inspired pandas design-pattern.',
      # url='',
      author='Quinn Dougherty',
      author_email='quinn.dougherty92@gmail.com',
      license='MIT',
      packages=['fpandas'],
      install_requires=[
          'pandas'
      ],
      zip_safe=False)
