# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mkdocs_code_runner']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8.2,<5.0.0', 'mkdocs>=1.1,<2.0']

entry_points = \
{'mkdocs.plugins': ['mkdocs-code-runner = '
                    'mkdocs_code_runner.plugin:CodeRunner']}

setup_kwargs = {
    'name': 'mkdocs-code-runner',
    'version': '0.0.1',
    'description': 'Mkdocs plugin for converting JavaScript code into runnable scripts.',
    'long_description': '<p align="center">\n  <h1>mkdocs-code-runner</h1>\n</p>\n<p align="center">\n  <img src="https://img.shields.io/pypi/v/mkdocs-code-runner" alt="PyPI Version">\n  <img src="https://img.shields.io/github/license/wolfgangwazzlestrauss/mkdocs-code-runner" alt="License">\n  <img src="https://github.com/wolfgangwazzlestrauss/mkdocs-code-runner/workflows/build/badge.svg" alt="Build Status">\n  <img src="https://img.shields.io/github/repo-size/wolfgangwazzlestrauss/mkdocs-code-runner" alt="Repository Size">\n</p>\n\nmkdocs-code-runner is an [MkDocs](https://www.mkdocs.org/) plugin which converts Javascript code\nblocks in Markdown files into runnable scripts for your browser.\n\n\n## Getting Started\n\n### Installation\n\nmkdocs-code-runner can be installed for Python 3.6+ with\n\n```bash\npip install --user mkdocs-code-runner\n```\n\n\n## Contributing\n\nFor guidance on setting up a development environment and making a contribution to mkdocs-code-runner,\nsee the [contributing guide](CONTRIBUTING.md).\n\n\n## License\n\nDistributed under the terms of the [MIT license](LICENSE.md), mkdocs-code-runner is\nfree and open source software.\n',
    'author': 'Macklan Weinstein',
    'author_email': 'wolfgangwazzlestrauss@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wolfgangwazzlestrauss/mkdocs-code-runner',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
