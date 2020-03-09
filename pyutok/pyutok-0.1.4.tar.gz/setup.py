# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['utok']
entry_points = \
{'console_scripts': ['utok = utok:main']}

setup_kwargs = {
    'name': 'pyutok',
    'version': '0.1.4',
    'description': 'Inspired by a tool I can not find anymore on the internet: utok 1.5. I use it to clean up path settings in large shell script configuration setups.',
    'long_description': "# pyUTok - Unique TOKens in python\n\nInspired by a tool I can not find anymore on the internet: utok 1.5. I\nuse it to clean up path settings in large shell script configuration\nsetups.\n\nutok has the following options:\n\n```plaintext\nusage: utok [-h] [--delimiter DELIMITER] [--delete-list DELETE_LIST]\n            [--version]\n            token [token ...]\n\npositional arguments:\n  token\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --delimiter DELIMITER, -s DELIMITER\n                        Allows one to change the delimiter. If you use csh you\n                        might want to set your path with something like: set\n                        path = (`utok -s \\ /usr/local/bin $path`) (default: :)\n  --delete-list DELETE_LIST, -d DELETE_LIST\n                        Allows one to remove tokens from a list, to remove\n                        /usr/sbin and . from a path in Bourne Shell one might\n                        use: PATH=`utok $PATH -d .:/usr/sbin` (default: None)\n  --version, -V         show program's version number and exit\n```\n\n## Availability\n\nThe latest version should be available at <https://gitlab.com/berhoel/python/pyutok>\n\n## Description\n\nutok, Unique TOKens, takes a list of arguments with delimiters and\nreject all duplicate entries. Here is a example using MANPATH:\n\n```console\n$ echo $MANPATH\n/usr/man:/usr/local/man\n$ MANPATH=`utok $HOME/local/man /usr/local/man $MANPATH /usr/openwin/man`\n$ export MANPATH\n$ echo $MANPATH\n/home/sven/local/man:/usr/local/man:/usr/man:/usr/openwin/man\n```\n\nEven though /usr/local/man was included a second time it is only in\nthe MANPATH once, though it is now before the /usr/man entry instead\nof after it.\n\nThis version adds the -d option to remove tokens. To remove . from the\nPATH one would do the following:\n\n```console\n$ echo $PATH\n/usr/local/bin:.:/usr/bin:/usr/sbin\n$ PATH=`utok -d .: $PATH`\n$ echo PATH\n/usr/local/bin:/usr/bin:/usr/sbin\n$ export PATH\n```\n\n## Requested Features\n\n * Have a way to to push an element further back in the path. A work\n   around of this would be be something like \n   ```console\n   utok `utok a:b:c:d -d b` b\n   ```\n   , which returns: a:c:d:b\n\n  * Have a way to include multiple -s options. \n\n## Feedback\n\nComments or bug reports/fixes go to Berthold Höllmann <bhoel@web.de>.\n\nCopyright © 2020 Berthold Höllmann <bhoel@web.de>\n\nOriginal C version:\nCopyright © 1998 Sven Heinicke <sven@zen.org>\n",
    'author': 'Berthold Höllmann',
    'author_email': 'berthold@xn--hllmanns-n4a.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/berhoel/python/pyutok.git',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
