# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notate']

package_data = \
{'': ['*']}

install_requires = \
['PyInquirer>=1.0.3,<2.0.0',
 'icalendar>=4.0.4,<5.0.0',
 'pdfkit>=0.6.1,<0.7.0',
 'pendulum>=2.0.5,<3.0.0',
 'requests>=2.23.0,<3.0.0',
 'youtube_dl>=2020.2.16,<2021.0.0']

entry_points = \
{'console_scripts': ['notate = notate.take_note:take_note']}

setup_kwargs = {
    'name': 'notate',
    'version': '0.1.0',
    'description': 'Note generation scripts for note-taking with Notable.',
    'long_description': '',
    'author': 'David Cabinian',
    'author_email': 'dhcabinian@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
