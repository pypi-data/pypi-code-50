# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repacolors', 'repacolors.palette']

package_data = \
{'': ['*'], 'repacolors': ['command/*']}

install_requires = \
['click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['repacolor = repacolors.command.repacolor:color']}

setup_kwargs = {
    'name': 'repacolors',
    'version': '0.5.0',
    'description': 'Small library for color conversion, manipulation, etc.',
    'long_description': '# repacolors\n\nSmall library for color conversion, manipulation, etc.\n\n[![Build Status](https://travis-ci.com/dyuri/repacolors.svg?branch=master)](https://travis-ci.com/dyuri/repacolors)\n\n## Install\n\n```\n$ pip install repacolors\n```\n\n## `repacolor` command\n\n```\n$ repacolor --help                                                                         \nUsage: repacolor [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  colorwheel  Display colorwheel defined by `name` or created by the colors...\n  display     Display information about the provided colors.\n  palette     Get colors of given palette\n  pick        Pick colors from your desktop.\n  scale       Display color scale defined by the colors provided via stdin.\n```\n\n### `display`\n\nDisplay color information in the terminal.\n\n```\n$ repacolor display red\n\n+--------+ red - #ff0000  \n|  BIG   | rgb(255, 0, 0)  \n|  RED   | hsl(0, 100%, 50%)  \n| SQUARE | lab(53.24% 80.09 67.2)  \n+--------+   \n\n$ repacolor display "#ffaad5" "rgb(128, 12, 46, .8)"\n... (displays both colors)\n$ echo "#ffffff" | repacolor display\n... (displays `white`)\n```\n\n### `pick`\n\nExecutes color picker (`xcolor`) and displays the picked color.\n\n```\n$ repacolor pick\n```\n\n### `palette`\n\nDisplay the colors of the palette. If no palette name provided, it shows the palettes available.\n\n```\n$ repacolor palette\nList of available palette names:\nryb, rybw3, orrd, pubu, ...\n\n$ repacolor palette viridis\n#440154\n#482777\n...\n```\n\n### `scale`\n\nDisplay a color scale defined by the input colors.\n\n```\n$ repacolor scale red white\n[colors from red to white]\n$ repacolor palette viridis | repacolor scale\n[color scale defined by `viridis` colors]\n```\n\n### `colorwheel`\n\nDisplay a color wheel.\n\nPre defined color wheels:\n\n- `ryb` - The RYB color wheel\n- `rgb` or `hsl` - The RGB color wheel\n- `lab` or `lch` - CIELAB color wheel\n\nIf no color wheel name provided, it will create one from the colors provided on `stdin`.\n\n```\n$ repacolor colorwheel rgb\n[RGB color wheel]\n$ repacolor palette red white black red | repacolor colorwheel\n[red - white - black color wheel]\n```\n',
    'author': 'Gyuri Horak',
    'author_email': 'dyuri@horak.hu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dyuri/repacolors',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
