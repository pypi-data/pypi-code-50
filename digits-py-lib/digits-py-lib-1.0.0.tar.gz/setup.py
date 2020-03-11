# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['digits']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'digits-py-lib',
    'version': '1.0.0',
    'description': 'export ten first numbers',
    'long_description': '# digits py lib\n\nA useful library !\n\n## installation\n\n````shell script\npip install digits-py-lib\n````\n\n## usage\n\n````python\nfrom digits import digits\n\ndigits.one\ndigits.two\n# ...\n````\n',
    'author': 'thomas-marquis',
    'author_email': 'thomas.marquis314@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thomas-marquis/digits-py-lib',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
