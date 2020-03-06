# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cfntool']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.12.15,<2.0.0',
 'ccalogging>=0.3.3,<0.4.0',
 'chaim>=0.8.0,<0.9.0',
 'getopt2>=0.0.3,<0.0.4']

entry_points = \
{'console_scripts': ['cfn = cfntool.installtemplate:main']}

setup_kwargs = {
    'name': 'cfntool',
    'version': '0.2.1',
    'description': '',
    'long_description': None,
    'author': 'ccdale',
    'author_email': 'chris.allison@hivehome.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
