# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coderadio',
 'coderadio.core',
 'coderadio.plugins',
 'coderadio.tui',
 'coderadio.tui.buffers',
 'coderadio.tui.widget']

package_data = \
{'': ['*']}

install_requires = \
['notify-send>=0.0.13,<0.0.14',
 'prompt-toolkit==3.0.4',
 'pygments>=2.6.1,<3.0.0',
 'pyradios>=0.0.21,<0.0.22',
 'python-mpv>=0.4.5,<0.5.0',
 'python-vlc>=3.0.7110,<4.0.0',
 'streamscrobbler3>=0.0.4,<0.0.5']

entry_points = \
{'console_scripts': ['coderadio = coderadio.__main__:main']}

setup_kwargs = {
    'name': 'coderadio',
    'version': '0.0.dev18',
    'description': 'Terminal radio for geeks.',
    'long_description': '# coderadio\n\nListen to your favorite internet radio stations with coderadio.\n\n> Terminal radio for geeks.\n\n[![coderadio](./header.gif)](https://youtu.be/rPRMGupW2wY "coderadio")\n\n\nYoutube Video (https://youtu.be/rPRMGupW2wY )\n\n## Installation\n\nLinux and Windows:\n\n\n```console\n$ sudo pip install coderadio\n```\n\n## Usage example\n\n```console\n$ coderadio\n```\n\n## Development setup\n```console\n$ git clone git@github.com:andreztz/coderadio.git\n$ poetry install\n```\n\n## Release History\n\n    -   Work in progress\n\n## Meta\n\nAndré P. Santos – [@ztzandre](https://twitter.com/ztzandre) – andreztz@gmail.com\n\nDistributed under the XYZ license. See `LICENSE` for more information.\n\n[https://github.com/andreztz/coderadio](https://github.com/andreztz/)\n\n## Contributing\n\n1. Fork it (<https://github.com/andreztz/coderadio/fork>)\n2. Create your feature branch (`git checkout -b feature/fooBar`)\n3. Commit your changes (`git commit -am \'Add some fooBar\'`)\n4. Push to the branch (`git push origin feature/fooBar`)\n5. Create a new Pull Request\n',
    'author': 'André P. Santos',
    'author_email': 'andreztz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
