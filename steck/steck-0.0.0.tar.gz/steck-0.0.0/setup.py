# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['steck']
install_requires = \
['click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['pinnwand = pinnwand.__main__:main']}

setup_kwargs = {
    'name': 'steck',
    'version': '0.0.0',
    'description': 'Command line client for pinnwand pastebin.',
    'long_description': '',
    'author': 'supakeen',
    'author_email': 'cmdr@supakeen.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/supakeen/stich',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
