# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['refreeze_scripts']

package_data = \
{'': ['*']}

install_requires = \
['setuptools>=45.2.0,<46.0.0', 'typing-extensions>=3.7.4,<4.0.0']

entry_points = \
{'console_scripts': ['refreeze-scripts = refreeze_scripts.cli:main']}

setup_kwargs = {
    'name': 'refreeze-scripts',
    'version': '0.2.0',
    'description': 'Rewrite EXE files in Scripts directory on Windows',
    'long_description': '# refreeze-scripts\n\nA *refreeze-scripts* refreeze EXE files in `Scripts` directory on Windows.\n\nIt extract a script part from [simple_launcer](https://bitbucket.org/vinay.sajip/simple_launcher/src/default/); which is used in pip internally to make `console_script` executable; EXE file and make it executable via `cli.exe` in setuptools.\n',
    'author': 'Fixpoint, Inc.',
    'author_email': 'developer@fixpoint.co.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fixpoint/refreeze-scripts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
