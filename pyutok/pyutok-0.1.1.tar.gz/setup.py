# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['utok']
entry_points = \
{'console_scripts': ['utok = utok:main']}

setup_kwargs = {
    'name': 'pyutok',
    'version': '0.1.1',
    'description': 'Inspired by a tool I can not find anymore on the internet: utok 1.5. I use it to clean up path settings in large shell script configuration setups.',
    'long_description': None,
    'author': 'Berthold Höllmann',
    'author_email': 'berthold@xn--hllmanns-n4a.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/berhoel/python/pyutok.git',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
