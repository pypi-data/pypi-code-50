# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['consoler']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=0.15.5,<0.16.0', 'loguru>=0.4.1,<0.5.0']

setup_kwargs = {
    'name': 'consoler',
    'version': '0.1.1',
    'description': '',
    'long_description': '## Consoler\n\nA terminal printer that\'s totally tailored to how I like terminal printouts. If this happens to also be how you like terminal printouts, this package may well be for you too.\n\n### Installing\n\n`poetry add consoler` or `pip install consoler`\n\n### Usage\n\n    from consoler import console\n    console.log("This is a log level print out")\n    console.info("This is an info level print out")\n    console.warn("This is a warning level print out")\n\n    try:\n        1 / 0\n    except Exception as e:\n        console.error("Oh no!", e)\n\n',
    'author': 'Hactar',
    'author_email': 'systems@hactar.is',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hactar-is/consoler',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
