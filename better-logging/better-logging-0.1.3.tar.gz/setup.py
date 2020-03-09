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
    'version': '0.1.3',
    'description': 'Simple UI for Logback Postgres DBAppender',
    'long_description': 'Better Logging\n==============\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)\n[![Build Status](https://drone.b7w.me/api/badges/b7w/better-logging/status.svg)](https://drone.b7w.me/b7w/better-logging)\n[![Wheel Support](https://img.shields.io/pypi/wheel/better-logging)](https://pypi.org/project/better-logging/)\n[![Wheel Support](https://img.shields.io/pypi/pyversions/better-logging)](https://pypi.org/project/better-logging/)\n\n\nSimple UI for Logback Postgres DBAppender\n\n\n\nGenerate test events\n--------------------\n\n```sh\ncd _etc\n\npython generate-events.py 100000\ndocker-compose up -d;\n\necho "COPY logging_event FROM PROGRAM \'zcat /data/logging_event.csv.gz\' CSV;" | psql "postgres://root:root@127.0.0.1:5432/root"\necho "COPY logging_event_property FROM PROGRAM \'zcat /data/logging_event_property.csv.gz\' CSV;" | psql "postgres://root:root@127.0.0.1:5432/root"\n```\n\n\nRun Backend\n-----------\n\n```sh\ncd backend\n\npip3 install poetry\npoetry install\n\nexport CONFIG_PATH=../_etc/sample-config.py\npoetry run python src/better_logging/main.py\n```\n\n\nRun Frontend\n-----------\n\n```sh\ncd frontend\n\nnpm install\nnpm run serve\n```\n\n\nAbout\n-----\n\nBetter Logging is open source project, released by MIT license.\n\n\nLook, feel, be happy :-)\n',
    'author': 'B7W',
    'author_email': 'b7w@isudo.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/b7w/better-logging',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
