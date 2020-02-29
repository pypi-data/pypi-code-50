# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sparcli']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.1,<2.0.0']

setup_kwargs = {
    'name': 'sparcli',
    'version': '0.1.1',
    'description': 'Visualize metrics as text in real-time (sparklines)',
    'long_description': '![Tests](https://github.com/z0u/sparcli/workflows/Tests/badge.svg)\n![Linters](https://github.com/z0u/sparcli/workflows/Linters/badge.svg)\n![Canary build](https://github.com/z0u/sparcli/workflows/Canary%20build/badge.svg)\n![Publish](https://github.com/z0u/sparcli/workflows/Publish/badge.svg)\n\nSparCLI is a library for visualising metrics on the command line.\n\nUse this library to see the shape of data during execution of data pipelines and other long-running programs. Each metric is displayed as a sparkline that updates as the data changes.\n\n\n```\npip install --user py-make poetry\npymake all\n```\n\n```\npoetry run python demo.py\n```\n',
    'author': 'Alex Fraser',
    'author_email': 'alex.d.fraser@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/z0u/sparcli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
