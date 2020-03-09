# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_pytest_style']

package_data = \
{'': ['*']}

install_requires = \
['flake8-plugin-utils>=1.2.0,<2.0.0']

entry_points = \
{'flake8.extension': ['PT = flake8_pytest_style.plugin:PytestStylePlugin']}

setup_kwargs = {
    'name': 'flake8-pytest-style',
    'version': '0.4.0',
    'description': 'A flake8 plugin checking common style issues or inconsistencies with pytest-based tests.',
    'long_description': "# flake8-pytest-style\n\n[![pypi](https://badge.fury.io/py/flake8-pytest-style.svg)](https://pypi.org/project/flake8-pytest-style)\n[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/flake8-pytest-style)\n[![Downloads](https://img.shields.io/pypi/dm/flake8-pytest-style.svg)](https://pypistats.org/packages/flake8-pytest-style)\n[![Build Status](https://travis-ci.com/m-burst/flake8-pytest-style.svg?branch=master)](https://travis-ci.com/m-burst/flake8-pytest-style)\n[![Code coverage](https://codecov.io/gh/m-burst/flake8-pytest-style/branch/master/graph/badge.svg)](https://codecov.io/gh/m-burst/flake8-pytest-style)\n[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\n## Description\n\nA `flake8` plugin checking common style issues or inconsistencies with `pytest`-based tests.\n\nCurrently the following errors are reported:\n\n* `PT001 use @pytest.fixture() over @pytest.fixture`\n\n* `PT002 configuration for fixture '{name}' specified via positional args, use kwargs`  \ne.g. `@pytest.fixture(scope='module')` is OK, and `@pytest.fixture('module')` is an error\n\n* `PT003 scope='function' is implied in @pytest.fixture()`  \ne.g. `@pytest.fixture(scope='function')` should be replaced with `@pytest.fixture()`\n\n* `PT004 fixture '{name}' does not return anything, add leading underscore`\n\n* `PT005 fixture '{name}' returns a value, remove leading underscore`\n\n* `PT006 wrong name(s) type in @pytest.mark.parametrize, expected {expected_type}`  \ne.g. `@pytest.mark.parametrize(('name1', 'name2'), ...)` is ok,\nand `@pytest.mark.parametrize('name1,name2', ...)` is an error\n\n* `PT007 wrong values type in @pytest.mark.parametrize, expected {expected_type}`\n\n* `PT008 use return_value= instead of patching with lambda`  \ne.g. `mocker.patch('target', return_value=7)` is OK,\nand `mocker.patch('target', lambda *args: 7)` is an error\n\n* `PT009 use a regular assert instead of unittest-style '{assertion}'`\n\n* `PT010 set the expected exception in pytest.raises()`\n\n* `PT011 set the match parameter in pytest.raises({exception})`  \ne.g. `pytest.raises(ValueError, match='exception text')` is OK,\nand `pytest.raises(ValueError)` is an error.  \nThe exception list is controlled by the configuration option \n`pytest-raises-require-match-for`.\n\n* `PT012 pytest.raises() block should contain a single simple statement`  \nthis forbids multiple statements and control flow structures within\n`pytest.raises()` blocks.\n\n## Installation\n\n    pip install flake8-pytest-style\n    \n## Configuration\n\nThe plugin has the following configuration options:\n\n* `pytest-raises-require-match-for`  \nComma-separated list of exception names that require a `match=` parameter\nin a `pytest.raises()` call, as checked by `PT011`. By default the list\ncontains the following exceptions:\n  * `BaseException`, `Exception`\n  * `ValueError`\n  * `OSError`, `IOError`, `EnvironmentError`, `socket.error`\n\n## For developers\n\n### Install deps and setup pre-commit hook\n\n    make init\n\n### Run linters, autoformat, tests etc.\n\n    make format lint test\n\n### Bump new version\n\n    make bump_major\n    make bump_minor\n    make bump_patch\n\n## License\n\nMIT\n\n## Change Log\n\n**Unreleased**\n\n...\n\n**0.4.0 - 2020-03-09**\n\n* add `PT012` (checks for multiple statements in `with pytest.raises()`)\n\n**0.3.1 - 2020-03-09**\n\n* fix default value of `pytest-raises-require-match-for` config option\n\n**0.3.0 - 2020-03-09**\n\n* add `PT010` and `PT011` (checks for `pytest.raises` parameters)\n\n**0.2.0 - 2020-03-01**\n\n* add `PT009` (ported from [flake8-pytest](https://github.com/vikingco/flake8-pytest))\n\n**0.1.3 - 2019-05-24**\n\n* add `yield` fixtures support\n* fix changelog entry for 0.1.2\n\n**0.1.2 - 2019-05-23**\n\n* fix parametrize checkers not working in decorators\n\n**0.1.1 - 2019-05-23**\n\n* update PyPI description\n\n**0.1.0 - 2019-05-23**\n\n* initial\n",
    'author': 'Mikhail Burshteyn',
    'author_email': 'mdburshteyn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/flake8-pytest-style',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
