# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['togglstandup']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.1,<8.0.0',
 'crayons>=0.3.0,<0.4.0',
 'humanfriendly>=8.1,<9.0',
 'maya>=0.6.1,<0.7.0',
 'togglwrapper>=1.2.0,<2.0.0',
 'typer>=0.0.9,<0.0.10']

entry_points = \
{'console_scripts': ['standup = togglstandup:cli']}

setup_kwargs = {
    'name': 'toggl-standup',
    'version': '0.4.1',
    'description': 'Removes the pain of using Toggl with Geekbot',
    'long_description': '# Stand Up for Toggl\n\nThis tool helps generate my daily Geekbot stand up report in an format which I may copy and paste into Slack.\n\n## Usage\n\n```shell\n$ export TOGGL_API_KEY="PASTE_YOUR_KEY_HERE"\n\n$ standup --help\nUsage: standup [OPTIONS] SLANG_DATE\n\n  Standup tool to help with Toggl\n\nOptions:\n  --show-time / --no-show-time\n  --timezone TEXT\n  --version / --no-version\n  --help                        Show this message and exit.\n```\n\n## To generate a report for yesterday\n\n```shell\n$ standup yesterday\n```\n',
    'author': 'Jeff Triplett',
    'author_email': 'jeff.triplett@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jefftriplett/toggl-standup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
