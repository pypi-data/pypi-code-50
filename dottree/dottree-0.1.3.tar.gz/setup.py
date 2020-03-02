# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dottree']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dottree',
    'version': '0.1.3',
    'description': '',
    'long_description': '# dottree\n\nAn "Enhanced defaultdict", I have been using this construct in my code many time ends up writing the biolerplate getter setter many times. So packed into a module to share with you all.\n\n\n# How to install\n\n- Use pip to install \n- tested in Python2\n\n\n```bash \npip install dottree \n```\n\n# Quick check\n\n```python \n\n\'\'\'\nHow to use:\n- use like a dict\n- use like an object \n- Go as deep you need\n\n\'\'\'\n\nfrom dottree import dotree as dot\n\nd = dot()\nd.M.J = 7\nassert  d.M.J  == 7\nassert  d[\'M\'][\'J\']  == 7\n\n# downgrade to a dict any time\nprint dict(d.M) # {\'J\': 7}\n\n```\n',
    'author': 'Jitender',
    'author_email': 'gitbackspacer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gitbackspacer/dottree',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
