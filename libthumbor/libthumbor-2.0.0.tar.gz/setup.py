# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['libthumbor', 'libthumbor.django', 'libthumbor.url_signers']

package_data = \
{'': ['*']}

install_requires = \
['six>=1.14.0,<2.0.0']

setup_kwargs = {
    'name': 'libthumbor',
    'version': '2.0.0',
    'description': 'libthumbor is the python extension to generate thumbor URLs',
    'long_description': None,
    'author': 'Bernardo Heynemann',
    'author_email': 'heynemann@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
