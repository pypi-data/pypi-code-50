# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['adw']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.3,<2.0.0']

setup_kwargs = {
    'name': 'adw',
    'version': '0.1.0',
    'description': 'appdirs wrapper library',
    'long_description': None,
    'author': 'Mark Gemmill',
    'author_email': 'gitlab@markgemmill.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/mgemmill-pypi/adw',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
