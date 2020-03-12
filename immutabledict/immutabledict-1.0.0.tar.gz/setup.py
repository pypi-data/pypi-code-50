# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['immutabledict']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'immutabledict',
    'version': '1.0.0',
    'description': 'Immutable wrapper around dictionaries (a fork of frozendict)',
    'long_description': '# immutabledict\n\n![PyPI](https://img.shields.io/pypi/v/immutabledict) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/immutabledict) ![License](https://img.shields.io/pypi/l/immutabledict) ![Build](https://img.shields.io/travis/com/corenting/immutabledict) ![Codecov](https://img.shields.io/codecov/c/github/corenting/immutabledict) ![PyPI - Downloads](https://img.shields.io/pypi/dm/immutabledict)\n\nA fork of ``frozendict``, an immutable wrapper around dictionaries.\n\nSee the original project here: https://github.com/slezica/python-frozendict .\n\n## Differences with frozendict\n\n- Dropped support of Python 2\n- Fixed `collections.Mapping` deprecation warning\n',
    'author': 'Corentin Garcia',
    'author_email': 'corenting@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/corenting/immutabledict',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
