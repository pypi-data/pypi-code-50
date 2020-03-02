# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['steck']
install_requires = \
['click>=7.0,<8.0', 'python-magic>=0.4.15,<0.5.0', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['steck = steck:main']}

setup_kwargs = {
    'name': 'steck',
    'version': '0.1.1',
    'description': 'Client for pinnwand pastebin.',
    'long_description': '.. image:: https://travis-ci.org/supakeen/steck.svg?branch=master\n    :target: https://travis-ci.org/supakeen/steck\n\n.. image:: https://readthedocs.org/projects/steck/badge/?version=latest\n    :target: https://steck.readthedocs.io/en/latest/\n\n.. image:: https://steck.readthedocs.io/en/latest/_static/license.svg\n    :target: https://github.com/supakeen/steck/blob/master/LICENSE\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n\n.. image:: https://img.shields.io/pypi/v/steck\n    :target: https://pypi.org/project/steck\n\n.. image:: https://codecov.io/gh/supakeen/steck/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/supakeen/steck\n\nsteck\n#####\n\n``steck`` is a Python application to interface with the pinnwand_ pastebin\nsoftware.\n\nPrerequisites\n=============\n* Python >= 3.6\n* click\n* requests\n* python-magic\n\nUsage\n=====\n\nSimple use::\n\n  € steck paste *.py\n  View Paste http://localhost:8000/AK6A\n  Remove Paste http://localhost:8000/remove/DAST4HSEGG3UJDL4PAONH6RJXQ\n\n\nLicense\n=======\n``steck`` is distributed under the MIT license. See `LICENSE`\nfor details.\n\n.. _project page: https://github.com/supakeen/steck\n.. _documentation: https://steck.readthedocs.io/en/latest/\n.. _pinnwand: https://supakeen.com/project/pinnwand\n',
    'author': 'supakeen',
    'author_email': 'cmdr@supakeen.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/supakeen/steck',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
