# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cutty']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.5.0,<2.0.0']}

entry_points = \
{'console_scripts': ['cutty = cutty.console:main']}

setup_kwargs = {
    'name': 'cutty',
    'version': '0.1.0',
    'description': 'Cutty',
    'long_description': '[![Tests](https://github.com/cjolowicz/cutty/workflows/Tests/badge.svg)](https://github.com/cjolowicz/cutty/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/cjolowicz/cutty/branch/master/graph/badge.svg)](https://codecov.io/gh/cjolowicz/cutty)\n[![PyPI](https://img.shields.io/pypi/v/cutty.svg)](https://pypi.org/project/cutty/)\n[![Python Version](https://img.shields.io/pypi/pyversions/cutty)](https://pypi.org/project/cutty)\n[![Read the Docs](https://readthedocs.org/projects/cutty/badge/)](https://cutty.readthedocs.io/)\n[![License](https://img.shields.io/pypi/l/cutty)](https://opensource.org/licenses/MIT)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# cutty\n',
    'author': 'Claudio Jolowicz',
    'author_email': 'mail@claudiojolowicz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cjolowicz/cutty',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
