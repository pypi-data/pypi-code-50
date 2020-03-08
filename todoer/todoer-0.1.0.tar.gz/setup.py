# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['todoer']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.4.1,<0.5.0', 'python-gitlab>=2.1.0,<3.0.0']

entry_points = \
{'console_scripts': ['todoer = todoer.__main__:main']}

setup_kwargs = {
    'name': 'todoer',
    'version': '0.1.0',
    'description': 'Removes todo that match a certain regex.',
    'long_description': '# todoer\n\nRemove your todos on GitLab based on different criteria.\n\n### build\n\n```sh\npoetry install --no-dev --no-root\npoetry build\n```\n\n### installation\n\n```sh\npip3 install dist/todoer-0.1.0-py3-none-any.whl\n```\n\n### usage\n\nSpecific the following environment variables:\n\n* GITLAB_URL (defaults to `https://gitlab.com`)\n* GITLAB_TOKEN\n\n```sh\nusage: todoer [-h] [-t TITLE] [-d DESCRIPTION] [-c CREATOR]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -t TITLE, --title TITLE\n                        Regex of todo title to remove\n  -d DESCRIPTION, --description DESCRIPTION\n                        Regex of todo description to remove\n  -c CREATOR, --creator CREATOR\n                        Username of the issue creator\n```\n\n',
    'author': 'Max Wittig',
    'author_email': 'max.wittig95@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/max-wittig/todoer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
