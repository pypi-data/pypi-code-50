# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['steck']
install_requires = \
['appdirs>=1.4.3,<2.0.0',
 'click>=7.0,<8.0',
 'python-magic>=0.4.15,<0.5.0',
 'requests>=2.23.0,<3.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['steck = steck:main']}

setup_kwargs = {
    'name': 'steck',
    'version': '0.5.0',
    'description': 'Client for pinnwand pastebin.',
    'long_description': ".. image:: https://travis-ci.org/supakeen/steck.svg?branch=master\n    :target: https://travis-ci.org/supakeen/steck\n\n.. image:: https://readthedocs.org/projects/steck/badge/?version=latest\n    :target: https://steck.readthedocs.io/en/latest/\n\n.. image:: https://steck.readthedocs.io/en/latest/_static/license.svg\n    :target: https://github.com/supakeen/steck/blob/master/LICENSE\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n\n.. image:: https://img.shields.io/pypi/v/steck\n    :target: https://pypi.org/project/steck\n\n.. image:: https://codecov.io/gh/supakeen/steck/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/supakeen/steck\n\nsteck\n#####\n\n``steck`` is a Python application to interface with the pinnwand_ pastebin\nsoftware. By default ``steck`` pastes to bpaste_ but you can override the\ninstance used.\n\nPrerequisites\n=============\n* Python >= 3.6\n* click\n* requests\n* python-magic\n* termcolor\n* appdirs\n* toml\n\nUsage\n=====\n\nSimple use::\n\n  € steck paste *      \n  You are about to paste the following 7 files. Do you want to continue?\n   - LICENSE\n   - mypy.ini\n   - poetry.lock\n   - pyproject.toml\n   - README.rst\n   - requirements.txt\n   - steck.py\n  \n  Continue? [y/N] y\n  \n  Completed paste.\n  View link:    https://localhost:8000/W5\n  Removal link: https://localhost:8000/remove/TS2AFFIEHEWUBUV5HLKNAUZFEI\n\nSkip the confirmation::\n\n  € steck paste --no-confirm *\n \nDon't try to guess at filetypes::\n\n  € steck paste --no-magic *\n \n\nMore usecases are found in the documentation_.\n\n\nConfiguration\n=============\n\nThe default argument values used by ``steck`` can be configured by copying the\n``steck.toml-dist`` file to ``~/.config/steck/steck.toml``. You can turn off\nthe confirmation or choose another pinnwand instance there.\n\nMore about configuration can be found at the documentation_.\n\nLicense\n=======\n``steck`` is distributed under the MIT license. See `LICENSE`\nfor details.\n\n.. _bpaste: https://bpaste.net/\n.. _project page: https://github.com/supakeen/steck\n.. _documentation: https://steck.readthedocs.io/en/latest/\n.. _pinnwand: https://supakeen.com/project/pinnwand\n",
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
