# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['manjaro_torrent_find']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'getopt2>=0.0.3,<0.0.4',
 'lxml>=4.5.0,<5.0.0',
 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['mtf = manjaro_torrent_find.mtf:goBabe']}

setup_kwargs = {
    'name': 'manjaro-torrent-find',
    'version': '0.3.1',
    'description': 'Searches the OSDN Manjaro project for torrent files and downloads them.',
    'long_description': "Manjaro Torrent Find\n====================\n\nReads the RSS feed from osdn.net/projects/manjaro/storage/!rss and parses out the\n.torrent, .sig, .sha1 and .sha256 files. It then attempts to download them to the\ncurrent directory.\n\nInstallation\n------------\n\nAvailable from pypi, so `pip3 install manjaro-torrent-find --user` should suffice.\nYou'll then have a new command at `$HOME/.local/bin/mtf` so add that dir to your path.\n\nUsage\n-----\n\nOnce the local python scripts directory is on your path, just execute `mtf`.::\n\n    Manjaro Torrent Find will scrape osdn.net for Manjaro torrents.\n\n    Usage:\n        mtf [options]\n\n    Options:\n        -h this help\n        -o output directory (default: current directory)\n        -p project (either 'manjaro' or 'manjaro-community') (default: both)\n        -r only scrape the OSDN RSS feeds to find the torrent files\n        -t length of time to wait before requesting a new page/file from OSDN (default: 1 second)\n\n    With `-o` the output directory must already exist, otherwise the\n    current directory is used.\n\n    `-t` defaults to 1, though it could be a fracion i.e. 0.25 and is amount of time\n    to wait before requesting a new 'thing' from OSDN - this is to ensure that we don't\n    overload the OSDN servers (leave it at 1 second to be nice).\n\n",
    'author': 'Chris Allison',
    'author_email': 'chris.charles.allison+mtf@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ccdale/manjaro-torrent-find',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
