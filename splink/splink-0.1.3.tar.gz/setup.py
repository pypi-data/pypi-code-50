# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['splink']

package_data = \
{'': ['*'], 'splink': ['files/*']}

install_requires = \
['jsonschema>=3.2,<4.0']

setup_kwargs = {
    'name': 'splink',
    'version': '0.1.3',
    'description': "WORK IN PROGRESS:  Implementation in Apache Spark of the EM algorithm to estimate parameters of Fellegi-Sunter's canonical model of record linkage.",
    'long_description': None,
    'author': 'Robin Linacre',
    'author_email': 'robinlinacre@hotmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
