#!/usr/bin/env python3

with open("README.md", "r") as fh:
    long_description = fh.read()

import setuptools
setuptools.setup(
  name = 'ProcBigEasyDriver',         
  packages = ['ProcBigEasyDriver'],   
  version = '0.0.2',      
  license='GPLv3',        
  description = 'PI controller for continously rotating a stepper using the big easy driver in a background process on RPi',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Matthew Davenport',      
  author_email = 'mdavenport@rockefeller.edu', 
  url = 'https://github.com/mattisabrat/Processed_PI_BigEasyDriver',
  install_requires=[            
        'gpiozero',
        'pigpio',
        'rpi-gpio'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)' ,
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: POSIX :: Linux'
  ],
)
