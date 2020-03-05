# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['urmarketscraper']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'urmarketscraper',
    'version': '1.0.1',
    'description': 'Collects market offers for Urban Rivals.',
    'long_description': '# Urban Rivals Market Scraper\n\n## Collects market offers for Urban Rivals.\n\n#### Install from https://pypi.org/project/urmarketscraper/\n\nThis is a screen scraper utility for [Urban Rivals](https://www.urban-rivals.com).\n\nTo use, call `market.get_market_offers`\n\nThe first parameter is the `requests.Session()` object which contains a logged-in\nuser. The second parameter is the list of `ids` for the characters in question.\nThe third parameter is an optional override for what what the base market address\nis. Default is `https://www.urban-rivals.com/market/?`. Any url given here must end\nwith a `?` so that the URL encoding can complete correctly.\n\n[Basic Usage Example](docs/market/basic-usage.rst)\n\n[Full Documentation](https://urmarketscraper.readthedocs.io/en/latest/)\n\n### Example\n```python\n>>> from urmarketscraper import market\n>>> market.get_market_offers(session, ["1462", "1463"])\nReturns:\n    {"1462": {"_Offer__id": 1462, "_Offer__level_price_dict": {"1": "799", "4": "799"}}, "1463": {"_Offer__id": 1463, \n "_Offer__level_price_dict": {"2": "27887"}}}\n```',
    'author': 'Brent Spector',
    'author_email': 'brent.spector@yahoo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/brentspector/urmarketscraper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
