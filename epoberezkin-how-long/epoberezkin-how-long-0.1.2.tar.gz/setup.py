# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['epoberezkin_how_long']

package_data = \
{'': ['*']}

install_requires = \
['pendulum>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'epoberezkin-how-long',
    'version': '0.1.2',
    'description': '',
    'long_description': 'how_long\n========\n\nSimple Decorator to measure a function execution time.\n\nExample\n_______\n\n.. code-block:: python\n\n    from epoberezkin_how_long import timer\n\n\n    @timer\n    def some_function():\n        return [x for x in range(10_000_000)]',
    'author': 'Efim Poberezkin',
    'author_email': 'efim.poberezkin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
