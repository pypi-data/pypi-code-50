# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smartsquash']

package_data = \
{'': ['*']}

install_requires = \
['gitpython>=3.0.5,<4.0.0', 'loguru>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['sq = smartsquash.__main__:main']}

setup_kwargs = {
    'name': 'smartsquash',
    'version': '0.2.1',
    'description': 'Makes daily git workflows easier, automates rebases or fixups.',
    'long_description': '# smartsquash\n\n[![PyPI](https://badge.fury.io/py/smartsquash.svg)](https://badge.fury.io/py/smartsquash)\n[![PyPI - License](https://img.shields.io/pypi/l/smartsquash.svg)](https://github.com/max-wittig/smartsquash/blob/master/LICENSE)\n<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n\n> This is still in testing phase.\n\nMakes daily git workflows easier, automates rebases or fixups.\n\n### build\n\n```sh\npoetry install --no-dev --no-root\npoetry build\n```\n\n### installation\n\n```sh\npip3 install smartsquash\n```\n\n### usage\n\n```sh\nusage: sq [-h] [--target-branch TARGET_BRANCH] [--repo REPO] [--dry] [-s] [--no-add]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --target-branch TARGET_BRANCH\n                        Specify branch to target. Default is \'master\'\n  --repo REPO           Specify repo to modify. Uses pwd by default\n  --dry                 Run dry\n  -s, --squash          Squash similar commits on your feature branch\n  --no-add              Don\'t add modified files to staging area\n```\n\n### run tests\n\n```sh\npoetry run coverage run --source . -m pytest  \npoetry run coverage report\n```\n',
    'author': 'Max Wittig',
    'author_email': 'max.wittig95@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/max-wittig/smartsquash',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
