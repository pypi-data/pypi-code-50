#!/usr/bin/env python

PROJECT = 'parking-app'

__VERSION__="0.0.5"

from setuptools import setup, find_packages

try:
    long_description = open('README.md', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=__VERSION__,

    description='Parking desktop app',
    long_description=long_description,

    author='Richard Holly',
    author_email='rho@optimaideas.com',

    url='https://gitlab.com/optima_iot/parking_desktop_app',

    classifiers=['Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['PyQt5','imutils','pyqtgraph','opencv-python',
                      'requests','micropipes-cli==0.6', 'qdarkgraystyle','Pillow','matplotlib'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        'app': ['img/*'],
    },

    entry_points={
        'gui_scripts': [
            'parking-app = app.gui:main'
        ],
        'console_scripts': [
            'parking-app-debug = app.gui:main'
        ]
    },
    zip_safe=False,
)