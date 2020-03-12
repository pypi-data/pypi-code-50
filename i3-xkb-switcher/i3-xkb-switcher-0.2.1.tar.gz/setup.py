# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['i3_xkb_switcher']

package_data = \
{'': ['*']}

install_requires = \
['i3ipc>=2.1.1,<3.0.0', 'xkbgroup>=0.2.0,<0.3.0']

entry_points = \
{'console_scripts': ['i3-xkb-switcher = i3_xkb_switcher.switcher:main']}

setup_kwargs = {
    'name': 'i3-xkb-switcher',
    'version': '0.2.1',
    'description': 'Keyboard layout switcher for i3 windows',
    'long_description': 'i3-xkb-switcher\n===============\n\n## Description\n\nThis app records keyboard layout for a i3 windows when you leave them.\nAnd when you come back it is restore keyboard layout.\n\n## Install\n\n```bash\n$ pip install i3-xkb-switcher\n```\n\nAlso you can download compiled binary from [release page](https://github.com/inn0kenty/i3-xkb-switcher/releases).\n\n## Usage\n\n```bash\n$ i3-xkb-switcher\n```\n\nTo enable debug mode run with `--debug` key.\n\nBy default it writes logs to stdout. You can specify path by `--log-path` option.\n',
    'author': 'Innokenty Lebedev',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/inn0kenty/i3-xkb-switcher',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
