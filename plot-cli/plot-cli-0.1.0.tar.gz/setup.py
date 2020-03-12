# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plot_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.1,<8.0.0', 'matplotlib>=3.2.0,<4.0.0', 'pandas>=1.0.1,<2.0.0']

entry_points = \
{'console_scripts': ['plot = plot_cli.core:cli']}

setup_kwargs = {
    'name': 'plot-cli',
    'version': '0.1.0',
    'description': 'Command Line Interface for Data Visualization',
    'long_description': '# Plot CLI\n\n[![GitHub Workflow Status][actions-status]][actions] [![codecov][codecov-status]][codecov] [![License][license]][license-file]\n\nThis tool is command line interface for data visualization.\n\nThe plot-cli works on Python version 3.6.1 and greater.\n\n## Installation\n\nInstall and update using pip:\n\n```sh\npip install plot-cli\n```\n\n## Usage\n\nTo plot from file, use "-i" option:\n\n```sh\nplot -i data.csv\n```\n\nTo plot from stdin:\n\n```sh\ncat data.csv | plot\n```\n\nTo save to file, use "-o" option:\n\n```sh\nplot -i data.csv -o plot.png\n```\n\nIf you do not use "-o" option, it is saved in a temporary file and opened.\n\nSee also `plot --help`.\n\n### Examples\n\n```sh\necho "0\\n1\\n4" | plot\n```\n\n## Change Log\n\nSee [Change Log](CHANGELOG.md).\n\n[actions]: https://github.com/xkumiyu/plot-cli/actions\n[actions-status]: https://img.shields.io/github/workflow/status/xkumiyu/plot-cli/Python%20package\n[codecov]: https://codecov.io/gh/xkumiyu/plot-cli\n[codecov-status]: https://img.shields.io/codecov/c/github/xkumiyu/plot-cli\n[license]: https://img.shields.io/github/license/xkumiyu/plot-cli\n[license-file]: https://github.com/xkumiyu/plot-cli/blob/master/LICENSE\n',
    'author': 'xkumiyu',
    'author_email': 'xkumiyu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/xkumiyu/plot-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4',
}


setup(**setup_kwargs)
