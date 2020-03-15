# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bareasgi_auth_common',
 'bareasgi_auth_common.utils',
 'bareasgi_auth_common.utils.yaml_types']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=1.7,<2.0', 'PyYaml>=5.1,<6.0', 'bareclient>=4,<5']

setup_kwargs = {
    'name': 'bareasgi-auth-common',
    'version': '2.0.0',
    'description': '',
    'long_description': '# bareASGI-auth-common\n\nCommon code for authentication with bareASGI.',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
