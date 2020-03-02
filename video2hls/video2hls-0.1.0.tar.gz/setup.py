# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['video2hls']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['seg = video2hls.seg:run']}

setup_kwargs = {
    'name': 'video2hls',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
