# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['remotecv',
 'remotecv.detectors',
 'remotecv.detectors.complete_detector',
 'remotecv.detectors.face_detector',
 'remotecv.detectors.feature_detector',
 'remotecv.detectors.glasses_detector',
 'remotecv.detectors.profile_detector',
 'remotecv.result_store']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=7.0.0,<8.0.0',
 'opencv-python-headless>=4.2.0,<5.0.0',
 'pyres>=1.5,<2.0']

entry_points = \
{'console_scripts': ['remotecv = remotecv.worker:main']}

setup_kwargs = {
    'name': 'remotecv',
    'version': '3.0.0',
    'description': 'remotecv is an OpenCV worker for facial and feature recognition',
    'long_description': None,
    'author': 'Bernardo Heynemann',
    'author_email': 'heynemann@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
