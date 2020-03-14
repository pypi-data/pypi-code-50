# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_strings']

package_data = \
{'': ['*']}

install_requires = \
['flake8-plugin-utils']

entry_points = \
{'flake8.extension': ['STR = flake8_strings.plugin:StringsPlugin']}

setup_kwargs = {
    'name': 'flake8-strings',
    'version': '0.1.1',
    'description': 'Flake8 Linter for Strings',
    'long_description': "# flake8-strings\n\n[![pypi](https://badge.fury.io/py/flake8-strings.svg)](https://pypi.org/project/flake8-strings)\n[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/flake8-strings)\n[![Downloads](https://img.shields.io/pypi/dm/flake8-strings.svg)](https://pypistats.org/packages/flake8-strings)\n[![Build Status](https://travis-ci.org/d1618033/flake8-strings.svg?branch=master)](https://travis-ci.org/d1618033/flake8-strings)\n[![Code coverage](https://codecov.io/gh/d1618033/flake8-strings/branch/master/graph/badge.svg)](https://codecov.io/gh/d1618033/flake8-strings)\n[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\n## Description\n\nFlake8 Linter for Strings\n\n\n### Checks:\n\n\n* STR001: Unnecessary use of backslash escaping \n\ne.g: \n\nBad:\n\n```python\npath = 'C:\\\\Users\\\\root'\n```\n\nGood:\n\n```python\npath = r'C:\\Users\\root'\n```\n\n\n## Installation\n\n    pip install flake8-strings\n\n## Usage\n\n`flake8 <your code>`\n\n## For developers\n\n### Create venv and install deps\n\n    make init\n\n### Install git precommit hook\n\n    make precommit_install\n\n### Run linters, autoformat, tests etc.\n\n    make pretty lint test\n\n### Bump new version\n\n    make bump_major\n    make bump_minor\n    make bump_patch\n\n## License\n\nMIT\n\n## Change Log\n\nUnreleased\n-----\n\n* ...\n\n0.1.1 - 2020-03-14\n-----\n\n* ...\n\n0.1.0 - 2020-03-14\n-----\n\n* initial\n",
    'author': 'David S',
    'author_email': 'd1618033@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/flake8-strings',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
