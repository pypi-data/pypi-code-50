# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dial_core',
 'dial_core.datasets',
 'dial_core.datasets.datatype',
 'dial_core.node_editor',
 'dial_core.project',
 'dial_core.utils',
 'dial_core.utils.log']

package_data = \
{'': ['*']}

install_requires = \
['dependency-injector>=3.15.6,<4.0.0', 'tensorflow==2.0.0b1']

setup_kwargs = {
    'name': 'dial-core',
    'version': '0.6a5',
    'description': 'Deep Learning, node-based framework',
    'long_description': '# Dial\nDeep Learning GUI Framework\n\n![PyPI](https://img.shields.io/pypi/v/dial-core)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dial-core)\n[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n\n[![Build Status](https://travis-ci.com/dial-app/dial-core.svg?branch=master)](https://travis-ci.com/dial-app/dial-core)\n[![codecov](https://codecov.io/gh/dial-app/dial-core/branch/master/graph/badge.svg)](https://codecov.io/gh/dial-app/dial-core)\n',
    'author': 'David Afonso',
    'author_email': 'davafons@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dial-app/dial-core',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.8',
}


setup(**setup_kwargs)
