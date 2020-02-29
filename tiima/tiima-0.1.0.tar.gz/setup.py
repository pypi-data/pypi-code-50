# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['tiima']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8,<5.0', 'environs>=7.2,<8.0', 'requests>=2.23,<3.0']

setup_kwargs = {
    'name': 'tiima',
    'version': '0.1.0',
    'description': 'Python API Client for Visma Tiima',
    'long_description': '# Tiima\n\nA Python wrapper around the Visma Tiima mobile REST API\n\n## Installation\n\n### PIP\n`pip install tiima`\n\n### Poetry\n`poetry add tiima`\n\n\n## Usage\n\n\n```\nfrom tiima import Tiima\n\n# Usage with env vars\ntiima = Tiima()\ntiima.login()\n\n# Setting auth variables explicitly\ntiima = Tiima(company_id="foo", api_key="bar)\ntiima.login(username="example@example.com", password="example")\n\n# Calling an API endpoint\nprint(tiima.user())\n```\n\n### Configuration\n\nAuthentication can be done either explcitly or by settings the following environment variables:\n\n\n| Variable          | Description                          |\n| ----------------- | ------------------------------------ |\n| TIIMA_USERNAME    | Users Tiima username (email)         |\n| TIIMA_PASSWORD    | Users Tiima password                 |\n| TIIMA_COMPANY_ID  | Users company id (usually all caps)  |\n| TIIMA_API_KEY     | Tiima API Key                        |\n\n\n## Disclaimer\n\nThis software has no connection to Visma, nor is it in any way endorsed by Visma or any other company\naffiliated with the product (Visma Tiima). This project was created to make it easier for developers\nto use the API and for them to be able to create their own application around the API.\n\n## License\n\nMIT\n',
    'author': 'Frank Wickström',
    'author_email': 'no-email@example.com',
    'url': 'https://gitlab.com/python-poetry/poetry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
