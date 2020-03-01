# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hyperglass_agent',
 'hyperglass_agent.api',
 'hyperglass_agent.cli',
 'hyperglass_agent.models',
 'hyperglass_agent.nos_utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'cryptography>=2.8,<3.0',
 'fastapi>=0.45.0,<0.46.0',
 'httpx>=0.11,<0.12',
 'inquirer>=2.6.3,<3.0.0',
 'loguru>=0.4.0,<0.5.0',
 'pydantic>=1.3,<2.0',
 'pyjwt>=1.7.1,<2.0.0',
 'pyyaml>=5.2,<6.0',
 'stackprinter>=0.2.3,<0.3.0',
 'ujson>=1.35,<2.0',
 'uvicorn>=0.11.1,<0.12.0',
 'uvloop>=0.14.0,<0.15.0']

entry_points = \
{'console_scripts': ['hyperglass-agent = hyperglass-agent.console:cli']}

setup_kwargs = {
    'name': 'hyperglass-agent',
    'version': '0.1.1',
    'description': 'The Linux Routing Agent for hyperglass',
    'long_description': '<div align="center">\n\n<img width=300 src="https://github.com/checktheroads/hyperglass/blob/master/logo.png"/>\n\n<hr>\n\n**The hyperglass agent is a RESTful API agent for [hyperglass](https://github.com/checktheroads/hyperglass), currently supporting:**\n\n### [Free Range Routing](https://frrouting.org/)\n### [BIRD Routing Daemon](https://bird.network.cz/)\n\n</div>\n\n# Installation\n\n### [Check out the docs](https://hyperglass.io/docs/agent)\n\n# License\n\n[Clear BSD License](https://github.com/checktheroads/hyperglass-agent/master/LICENSE)\n',
    'author': 'Matt Love',
    'author_email': 'matt@hyperglass.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://hyperglass.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
