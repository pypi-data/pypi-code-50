import os
from setuptools import setup
#from distutils.core import setup

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version_str = open(os.path.join('ntp', '_version.txt'), 'r').read().strip()

setup(
    name='ntp',
    version=version_str,
    packages=['ntp'],

    author='Yeison Cardona',
    author_email='yencardonaal@unal.edu.com',
    maintainer='Yeison Cardona',
    maintainer_email='yencardonaal@unal.edu.com',

    # url='http://yeisoncardona.com/',
    download_url='https://bitbucket.org/gcpds/python-ntp',

    install_requires=[],

    include_package_data=True,
    license='BSD License',
    description="GCPDS: ntp",
    #    long_description = README,

    classifiers=[

    ],

)
