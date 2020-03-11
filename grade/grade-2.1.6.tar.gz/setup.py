# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grade', 'grade.cli', 'grade.pipeline']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0']

setup_kwargs = {
    'name': 'grade',
    'version': '2.1.6',
    'description': 'a package focused on autograding',
    'long_description': '# Grade\n\nA python package focused on making autograding easy, especially for executable programs and scripts.\n\n[![Documentation Status](https://readthedocs.org/projects/grade/badge/?version=latest)](https://grade.readthedocs.io/en/latest/)\n[![Release](https://img.shields.io/github/v/release/thoward27/grade)](https://github.com/thoward27/grade/releases)\n[![AGPL License](https://img.shields.io/github/license/thoward27/grade)](https://github.com/thoward27/grade/blob/master/LICENSE)\n[![Code Quality](https://img.shields.io/lgtm/grade/python/github/thoward27/grade)](https://lgtm.com/projects/g/thoward27/grade/context:python)\n[![codecov](https://codecov.io/gh/thoward27/grade/branch/master/graph/badge.svg)](https://codecov.io/gh/thoward27/grade)\n\n---\n\n## Setup\n\n### Pip\n\n`python -m pip install grade`\n\n### Docker\n\n```docker\nFROM thoward27/grade:latest\n```\n\n### Sources\n\n```\ngit clone https://github.com/thoward27/grade.git\ncd grade\npython -m pip install .\n```\n\n## Documentation\n\nAvailable on [ReadTheDocs](https://grade.readthedocs.io/en/latest/)\n\n## Example\n\nSee `example.py` for an example on how to work with Grade.\n',
    'author': 'Tom',
    'author_email': 'info@tomhoward.codes',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thoward27/grade',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
