#!/bin/python
# first create a version file
from simple_plotter4a import __version__
import subprocess
import os

version = __version__
print('Checking version...\n\nVersion extracted:', version)

# take care of some version limitation of p4a/buildozer
if len(version.split('+')) > 1:
    print('Found development version - stripping to next patch...')
    last_version = version.split('+')[0]
    major, minor, patch = last_version.split('.')
    version = major + '.' + minor + '.' + str(int(patch)+1)
    print('\nBuild version will be: {}'
          '\n'
          '\nNote: Although the APK version will be {} '
          '- the \'About\' tab will still show the dev. version {}.'
          '\n'
          '\nFor an official release, first add a git tag and then run this script.\n'.format(version, version,
                                                                                              __version__))
    # input('Press Enter to continue.')

# this serves the version for buildozer
with open('simple_plotter4a/version.py', 'w') as file:
    file.write('__version__ = \"{}\"'.format(version))

# this serves the version for the application
with open('simple_plotter4a/version.txt', 'w') as file:
    file.write(__version__)
