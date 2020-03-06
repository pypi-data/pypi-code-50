# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tiimaweb']

package_data = \
{'': ['*']}

install_requires = \
['mechanicalsoup>=0.12.0,<0.13.0', 'pytz>=2016.0']

entry_points = \
{'console_scripts': ['tiimaweb = tiimaweb.cli:main']}

setup_kwargs = {
    'name': 'tiimaweb',
    'version': '0.1.2',
    'description': 'Tiima Web Controller',
    'long_description': "TiimaWeb - Tiima Web Controller\n===============================\n\nThis library can be used to control the Tiima web UI through a simple\nPython API.  It uses MechanicalSoup for mimicing browser actions.\n\n|PyPI|\n\n.. |PyPI| image::\n   https://img.shields.io/pypi/v/tiimaweb.svg\n   :target: https://pypi.org/project/tiimaweb/\n\n\nInstalling\n----------\n\nTiimaWeb is in PyPI and can be installed simply by::\n\n  pip install tiimaweb\n\nor if you use Poetry::\n\n  poetry add tiimaweb\n\n\nUsage\n-----\n\nThe library can be used from Python code like this:\n\n.. code:: python\n\n  from datetime import date, datetime\n  \n  import tiimaweb\n\n  client = tiimaweb.Client()\n\n  with client.login('username', 'password', 'company') as tiima:\n      # Get all time blocks of 2020-02-29\n      time_blocks = tiima.get_time_blocks_of_date(date(2020, 2, 29))\n\n      # Print and delete all those time blocks\n      for time_block in time_blocks:\n          print(time_block)\n          tiima.delete_time_block(time_block)\n\n      # Add new time block\n      tiima.add_time_block(\n          start=datetime(2020, 3, 1, 8, 30),\n          end=datetime(2020, 3, 1, 11, 45))\n",
    'author': 'Tuomas Suutari',
    'author_email': 'tuomas@nepnep.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/suutari/tiimaweb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
