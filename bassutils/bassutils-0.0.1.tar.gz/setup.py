# -*- coding: utf-8 -*-

from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(name='bassutils',
      version='0.0.1',
      description='Python package testing',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='https://github.com/basameera/bass-utils',
      author='Sameera Sandaruwan',
      author_email='basameera@pm.com',
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
      ],
      packages=["bassutils"],
      include_package_data=True,
      # install_requires=["requests"],
      # entry_points={
      #     "console_scripts": [
      #         "weather-reporter=weather_reporter.cli:main",
      #     ]
      # },
      )
