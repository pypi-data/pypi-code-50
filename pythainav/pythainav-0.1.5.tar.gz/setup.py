# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pythainav', 'pythainav.utils']

package_data = \
{'': ['*']}

install_requires = \
['dateparser>=0.7.2,<0.8.0',
 'furl>=2.1,<3.0',
 'fuzzywuzzy[speedup]>=0.17.0,<0.18.0',
 'requests>=2.22,<3.0']

extras_require = \
{':python_version == "3.6"': ['dataclasses>=0.7.0,<0.8.0']}

setup_kwargs = {
    'name': 'pythainav',
    'version': '0.1.5',
    'description': 'a Python interface to pull thai mutual fund NAV',
    'long_description': '# PythaiNAV: ทำให้การดึงข้อมูลกองทุนไทยเป็นเรื่องง่าย\n<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->\n[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)\n<!-- ALL-CONTRIBUTORS-BADGE:END -->\n\n[![Github_workflow_tatus](https://img.shields.io/github/workflow/status/CircleOnCircles/pythainav/Python%20package)](https://github.com/CircleOnCircles/pythainav/actions?query=workflow%3ATests)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/CircleOnCircles/pythainav.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/CircleOnCircles/pythainav/context:python)\n[![Total alerts](https://img.shields.io/lgtm/alerts/g/CircleOnCircles/pythainav.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/CircleOnCircles/pythainav/alerts/)\n\n\n\n![cover image](https://github.com/CircleOnCircles/pythainav/raw/master/extra/pythainav.png)\n\n\n\n> อยากชวนทุกคนมาร่วมพัฒนา ติชม แนะนำ เพื่อให้ทุกคนเข้าถึงข้อมูลการง่ายขึ้น [เริ่มต้นได้ที่นี้](https://github.com/CircleOnCircles/pythainav/issues) หรือเข้ามา Chat ใน [Discord](https://discord.gg/jjuMcKZ) ได้เลย 😊\n\n📖 Documentation is here. คู่มือการใช้งานอยู่ที่นี่ <https://pythainav.nutchanon.org/>\n\n## Get Started - เริ่มต้นใช้งาน\n\n```bash\n$ pip install pythainav\n```\n\n```python\nimport pythainav as nav\n\nnav.get("KT-PRECIOUS")\n> Nav(value=4.2696, updated=\'20/01/2020\', tags={\'latest\'}, fund=\'KT-PRECIOUS\')\n\nnav.get("TISTECH-A", date="1 week ago")\n> Nav(value=12.9976, updated=\'14/01/2020\', tags={}, fund=\'TISTECH-A\')\n\nnav.get_all("TISTECH-A")\n> [Nav(value=12.9976, updated=\'21/01/2020\', tags={}, fund=\'TISTECH-A\'), Nav(value=12.9002, updated=\'20/01/2020\', tags={}, fund=\'TISTECH-A\'), ...]\n\nnav.get_all("KT-PRECIOUS", asDataFrame=True)\n> pd.DataFrame [2121 rows x 4 columns]\n```\n\n## Source of Data - ที่มาข้อมูล\n\nดูจาก <https://pythainav.nutchanon.org/datasource/>\n\n## Disclaimer\n\nเราไม่รับประกันความเสียหายใดๆทั้งสิ้นที่เกิดจาก แหล่งข้อมูล, library, source code,sample code, documentation, library dependencies และอื่นๆ\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tr>\n    <td align="center"><a href="http://nutchanon.org"><img src="https://avatars2.githubusercontent.com/u/8089231?v=4" width="100px;" alt=""/><br /><sub><b>Nutchanon Ninyawee</b></sub></a><br /><a href="https://github.com/CircleOnCircles/pythainav/commits?author=CircleOnCircles" title="Code">💻</a></td>\n    <td align="center"><a href="https://github.com/sctnightcore"><img src="https://avatars2.githubusercontent.com/u/23263315?v=4" width="100px;" alt=""/><br /><sub><b>sctnightcore</b></sub></a><br /><a href="https://github.com/CircleOnCircles/pythainav/commits?author=sctnightcore" title="Code">💻</a> <a href="#talk-sctnightcore" title="Talks">📢</a> <a href="#ideas-sctnightcore" title="Ideas, Planning, & Feedback">🤔</a></td>\n  </tr>\n</table>\n\n<!-- markdownlint-enable -->\n<!-- prettier-ignore-end -->\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n\n## Related and Alternative\n\nตัวที่ใช้ได้ในปัจจุบัน 22/02/20\n* [uncleEngineer](https://github.com/UncleEngineer/uncleengineer) - ดึงข้อมูลหุ้น ณ ปัจจุบัน\n* [pandas-datareader](https://www.patanasongsivilai.com/blog/stock-thai-python/) - ดึงข้อมูลหุ้นย้อนหลังผ่าน `pdr.get_data_yahoo`\n',
    'author': 'Nutchanon Ninyawee',
    'author_email': 'me@nutchanon.org',
    'maintainer': 'Nutchanon Ninyawee',
    'maintainer_email': 'me@nutchanon.org',
    'url': 'https://github.com/CircleOnCircles/pythainav',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.8,<4.0.0',
}


setup(**setup_kwargs)
