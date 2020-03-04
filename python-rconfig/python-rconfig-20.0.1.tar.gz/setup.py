# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rconfig']

package_data = \
{'': ['*']}

install_requires = \
['python-consul>=1.1.0,<2.0.0']

extras_require = \
{'cli': ['click>=7.0,<8.0']}

entry_points = \
{'console_scripts': ['rconfig = rconfig.cli:cli']}

setup_kwargs = {
    'name': 'python-rconfig',
    'version': '20.0.1',
    'description': 'Helps get configuration from consul server',
    'long_description': 'rconfig\n=======\n\n  .. image:: https://travis-ci.org/ArtemAngelchev/python-rconfig.svg?branch=master\n      :target: https://travis-ci.org/ArtemAngelchev/python-rconfig\n\n  .. image:: http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat\n\n\n  ``rconfig`` helps you to bring configs from a consul server to your\n  application.\n\n\nInstallation\n------------\n\n  Install the latest version with:\n\n  ::\n\n    pip install -U python-rconfig\n\n\n  For command-line support, use the CLI option during installation:\n\n  ::\n\n    pip install -U "python-rconfig[cli]"\n\n\nUsage\n-----\n\n  First off all ``rconfig`` expects that you have the following key structure\n  on the consul server:\n\n  ::\n\n    <root-key>\n        |____<common-config-key>\n        |          |\n        |          |___<some-env-key>\n        |          |           |_____<key-value>\n        |          |           |_____<key-value>\n        |          |\n        |          |___<another-env-key>\n        |                      |_____<key-value>\n        |                      |_____<key-value>\n        |____<app-config-key>\n                   |\n                   |___<some-env-key>\n                   |           |_____<key-value>\n                   |           |_____<key-value>\n                   |\n                   |___<another-env-key>\n                               |_____<key-value>\n                               |_____<key-value>\n\n\n  Here root key stands for the name of the project when some have multiple\n  applications that grouped under some kind of common purpose (often when talk\n  about microservices).\n  Under common configuration key, you should store configurations that common\n  to all your applications in the project, in this case, it\'s much easier to\n  change the config in one place than go to multiple.\n',
    'author': 'Artem Angelchev',
    'author_email': 'artangelchev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ArtemAngelchev/python-rconfig',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
