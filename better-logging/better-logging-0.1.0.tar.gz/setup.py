# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['better_logging']

package_data = \
{'': ['*'], 'better_logging': ['static/*', 'static/css/*', 'static/js/*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0', 'arrow>=0.15.5,<0.16.0', 'asyncpg>=0.20.1,<0.21.0']

entry_points = \
{'console_scripts': ['better-logging = better_logging.main:main']}

setup_kwargs = {
    'name': 'better-logging',
    'version': '0.1.0',
    'description': 'Simple UI for Logback Postgres DBAppender',
    'long_description': None,
    'author': 'B7W',
    'author_email': 'b7w@isudo.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
