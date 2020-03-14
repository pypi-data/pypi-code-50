# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['getproxies', 'getproxies.spiders']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.1,<8.0.0', 'parsel>=1.5.2,<2.0.0', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['getproxies = getproxies.cli:main']}

setup_kwargs = {
    'name': 'getproxies',
    'version': '1.0.0',
    'description': 'Scraper of free online proxies',
    'long_description': "# getproxies\n\nGet some free proxies scraped from free proxy sources.\n\n```python\nfrom getproxies import get_proxies\n\nproxies = get_proxies()\nprint(proxies[:10])\n# [http://196.18.215.153:3128, https://36.67.89.179:65205, http://35.247.192.53:3128, socks5://113.54.158.40:1080, https://180.122.51.154:9999, socks4://117.44.28.152:9201, https://178.20.137.178:43980, https://109.86.121.118:46333, https://148.77.34.194:39175, socks4://114.99.16.195:1080]\n```\n\nor using cli:\n\n```shell script\n$ poetry run getproxies --help\nUsage: getproxies [OPTIONS]\n\n  scrape free proxies from all sources and put it to STDOUT\n\nOptions:\n  -p, --protocol [https|http|socks4|socks5]\n                                  restrict to specific protocol\n  -c, --country TEXT              only proxies from specified country (ISO\n                                  double char code, e.g. US)\n\n  -l, --limit INTEGER             limit proxy retrieval - increases\n                                  performance\n\n  -f, --format TEXT               proxy output format, available variables: ho\n                                  st,port,protocol,code,country,anonymous,sour\n                                  ce  [default: {protocol}://{host}:{port}]\n\n  --help                          Show this message and exit.\n```\n\n## Install\n\n```shell script\n$ pip install getproxies\nor for latest code\n$ pip install -U git+https://github.com/granitosaurus/getproxies\n```\n\n## Sources\n\nCurrently these sources are supported \n\n|source|spider|\n|---|---|\n|[http://free-proxy-list.net](http://free-proxy-list.net)|[FreeProxyListSpider](./getproxies/spiders/freeproxylist.py)|\n|[http://proxy-daily.com](http://proxy-daily.com)|[ProxyDailySpider](./getproxies/spiders/proxydaily.py)|\n\n## extended usage\n\nFor more detailed proxy query a `ProxyManager` can be used:\n\n```python\nfrom getproxies import ProxyManager\n\nproxies = ProxyManager(\n    limit=10,  # only 10 proxies\n    protocol='socks5',  # only socks5 proxies\n    country='us',  # only us proxies\n)\n```\n\n_limit parameter can reduce retrieval time_\n\n`Proxy` objects also have extended attributes:\n\n```python\nclass Proxy:\n    host: str\n    port: str\n    protocol: str\n    code: str = ''\n    country: str = ''\n    anonymous: bool = False\n    source: str = ''\n```\n\nas strings they resolve to `protocol://host:port` template.\n\n",
    'author': 'granitosaurus',
    'author_email': 'bernardas.alisauskas@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/granitosaurus/getproxies',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
