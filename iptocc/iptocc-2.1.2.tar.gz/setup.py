# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iptocc']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0.1,<2.0.0']

entry_points = \
{'console_scripts': ['update_rir = updater:update_rir_databases']}

setup_kwargs = {
    'name': 'iptocc',
    'version': '2.1.2',
    'description': 'Get country code of IPv4/IPv6 address. Address lookup is done offline.',
    'long_description': "# IPToCC\n\n Get ISO country code of IPv4/IPv6 address. Address lookup is done locally.\n\n<table>\n    <tr>\n        <td>License</td>\n        <td><img src='https://img.shields.io/pypi/l/IPToCC.svg'></td>\n        <td>Version</td>\n        <td><img src='https://img.shields.io/pypi/v/IPToCC.svg'></td>\n    </tr>\n    <tr>\n        <td>Travis CI</td>\n        <td><img src='https://travis-ci.org/roniemartinez/IPToCC.svg?branch=master'></td>\n        <td>Coverage</td>\n        <td><img src='https://codecov.io/gh/roniemartinez/IPToCC/branch/master/graph/badge.svg'></td>\n    </tr>\n    <tr>\n        <td>AppVeyor</td>\n        <td><img src='https://ci.appveyor.com/api/projects/status/1xmd0gr278bhu090/branch/master?svg=true'></td>\n        <td>Supported versions</td>\n        <td><img src='https://img.shields.io/pypi/pyversions/IPToCC.svg'></td>\n    </tr>\n    <tr>\n        <td>Wheel</td>\n        <td><img src='https://img.shields.io/pypi/wheel/IPToCC.svg'></td>\n        <td>Implementation</td>\n        <td><img src='https://img.shields.io/pypi/implementation/IPToCC.svg'></td>\n    </tr>\n    <tr>\n        <td>Status</td>\n        <td><img src='https://img.shields.io/pypi/status/IPToCC.svg'></td>\n        <td>Downloads</td>\n        <td><img src='https://img.shields.io/pypi/dm/IPToCC.svg'></td>\n    </tr>\n    <tr>\n        <td>Show your support</td>\n        <td><a href='https://saythanks.io/to/roniemartinez'><img src='https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg'></a></td>\n    </tr>\n</table>\n\n## Features\n\n- [x] No external API call\n- [x] No paid GeoIP service\n- [x] Thread-safe\n- [x] Offline\n\nTo learn about using IP addresses for geolocation, read the [Wikipedia article](https://en.wikipedia.org/wiki/Geolocation_software) to gain a basic understanding.\n\n## Install\n\n```bash\npip install IPToCC\n```\n\n## Usage\n\n```python\nfrom iptocc import get_country_code\ncountry_code = get_country_code('<IPv4/IPv6 address>')\n```\n\n## Databases\n\n- ftp://ftp.afrinic.net/stats/afrinic/delegated-afrinic-extended-latest\n- ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest\n- ftp://ftp.apnic.net/public/apnic/stats/apnic/delegated-apnic-extended-latest\n- ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest\n- ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest\n\n## Dependencies\n\n- [pandas](https://github.com/pandas-dev/pandas)\n- [ipaddress](https://github.com/phihag/ipaddress)\n- [backports.functools_lru_cache import lru_cache](https://github.com/jaraco/backports.functools_lru_cache)\n\n## References\n\n- [RIR Statistics Exchange Format](https://www.apnic.net/about-apnic/corporate-documents/documents/resource-guidelines/rir-statistics-exchange-format/)\n- [How can I compile an IP address to country lookup database to make available for free?](https://webmasters.stackexchange.com/questions/34628/how-can-i-compile-an-ip-address-to-country-lookup-database-to-make-available-for)\n- [ISO 3166 Country Codes](https://dev.maxmind.com/geoip/legacy/codes/iso3166/)\n\n## Maintainers\n\n- [Ronie Martinez](mailto:ronmarti18@gmail.com)\n",
    'author': 'Ronie Martinez',
    'author_email': 'ronmarti18@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roniemartinez/IPToCC',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4',
}


setup(**setup_kwargs)
