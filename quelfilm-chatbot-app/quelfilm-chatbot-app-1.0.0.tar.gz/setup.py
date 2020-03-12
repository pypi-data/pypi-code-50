# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quelfilm']

package_data = \
{'': ['*']}

install_requires = \
['flask>=1.1.1,<2.0.0', 'nlp-tools-py-lib==0.1.1']

entry_points = \
{'console_scripts': ['start = quelfilm.app:start']}

setup_kwargs = {
    'name': 'quelfilm-chatbot-app',
    'version': '1.0.0',
    'description': 'webapp for choose a movie',
    'long_description': None,
    'author': 'thomas.marquis.dev',
    'author_email': 'thomas.marquis.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
