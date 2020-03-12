# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hootsweet']

package_data = \
{'': ['*']}

install_requires = \
['cherrypy>=18.5.0,<19.0.0',
 'requests>=2.23,<3.0',
 'requests_oauthlib>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'hootsweet',
    'version': '0.3.2',
    'description': 'A python library for the HootSuite REST API.',
    'long_description': '## HootSweet\n\nA python API for the HootSuite REST API.\n\n### Installation\n\n```shell\npip install hootsweet\n```\n\n### Usage\n\n```python\nfrom hootsweet import HootSweet\n\nclient_id = "Your-HootSuite-Client-ID"\nclient_secret = "Your-HootSuite-Client-Secret"\nredirect_uri = "http://redirect.uri/"\n\ndef handle_refresh(token):\n    # callback function to save token to a database or file\n    save_token_to_db(token)\n\nclient = HootSweet(client_id, client_secret, redirect_uri=redirect_uri, refresh_cb=handle_refresh)\n\n# Step 1 get authorization url from HootSuite\nurl, state = client.authorization_url()\n\n# Step 2 go to url above and get OAuth2 code\ntoken = client.fetch_token(code)\n\n# client.token now contains your authentication token\n# Step 3 (optional) refresh token periodically, this automatically calls handle_refresh\ntoken = client.refresh_token()\n\n# retrieve data from https://platform.hootsuite.com/v1/me\nme = client.get_me()\n\n# retrieve authenticated members organizations https://platform.hootsuite.com/v1/me/organizations\norganizations = client.get_me_organizations()\n```\n',
    'author': 'Ciaran McCormick',
    'author_email': 'ciaran@ciaranmccormick.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
