# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pwnedpasswds']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['pwnedpasswds = pwnedpasswds:pwnedpasswds.cli']}

setup_kwargs = {
    'name': 'pwnedpasswds',
    'version': '0.1.0',
    'description': '',
    'long_description': '# pwnedpasswds\n\nA python wrapper for the [Pwned Passwords](https://haveibeenpwned.com/Passwords) API.\n\n\n## Usage\n\nYou can either use pwnedpasswds in your python code or as a command line utility.\n\n### Inside python\n\n```python\n>>> from pwnedpasswds import check_passwd\n>>> count = check_passwd("Password1")\n>>> count\n116789\n```\n\n### Inside the commandline\n\nYou can supply passwords to pwnedpasswds as a command line argument, or thorugh stdin.\n\n\n```bash\n$ pwnedpasswds correcthorsebatterystaple\n120\n```\n\n```bash\n$ echo "linux4life" | pwnedpasswds\n44\n```\n\n```bash\n$ cat passwds.txt\ntroyhunt\np455w0rd\n14m501337\n\n$ cat passwds.txt | pwnedpasswds\n11\n15611\n14\n```\n\n',
    'author': 'Luke Spademan',
    'author_email': 'info@lukespademan.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/mokytis/pwnedpasswds',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
