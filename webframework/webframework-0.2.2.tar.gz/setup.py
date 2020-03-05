# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webframework', 'webframework.core', 'webframework.web']

package_data = \
{'': ['*']}

install_requires = \
['allure-behave>=2.8.11,<3.0.0',
 'behave>=1.2.6,<2.0.0',
 'selenium>=3.141.0,<4.0.0']

setup_kwargs = {
    'name': 'webframework',
    'version': '0.2.2',
    'description': 'Framework para desarrollar tests automatizados',
    'long_description': '',
    'author': 'cmejia',
    'author_email': 'cmejia@kiusys.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://source.olleros/qa-automation/python-web-framework-automation',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
