#!/usr/bin/env python

from setuptools import setup  # type: ignore

setup(name='fpandas',
      version='0.2',
      description='For a pandas with a functional design pattern.',
      # url='',
      author='Quinn Dougherty',
      author_email='quinn.dougherty92@gmail.com',
      license='MIT',
      packages=['fpandas'],
      install_requires=[
          'pandas'
      ],
      zip_safe=False)
