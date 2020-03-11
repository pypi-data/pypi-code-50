# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsonpath']

package_data = \
{'': ['*']}

install_requires = \
['lark-parser>=0.8.1,<0.9.0', 'typing_extensions>=3.7,<4.0']

extras_require = \
{'docs': ['sphinx>=2.3.1,<3.0.0', 'livereload>=2.6.1,<3.0.0'],
 'lint': ['black>=19.3b0,<20.0',
          'flake8>=3.7.8,<4.0.0',
          'isort>=4.3.21,<5.0.0',
          'mypy>=0.750,<0.751',
          'pytest>=5.2.0,<6.0.0',
          'flake8-bugbear>=19.8,<20.0',
          'blacken-docs>=1.5.0,<2.0.0',
          'doc8>=0.8.0,<0.9.0',
          'pygments>=2.5.2,<3.0.0',
          'livereload>=2.6.1,<3.0.0'],
 'test': ['pytest>=5.2.0,<6.0.0', 'pytest-cov>=2.7.1,<3.0.0']}

setup_kwargs = {
    'name': 'jsonpath-extractor',
    'version': '0.2.0a0',
    'description': 'A selector expression for extracting data from JSON.',
    'long_description': '========\nJSONPATH\n========\n\n|license| |Pypi Status| |Python version| |Package version| |PyPI - Downloads|\n|GitHub last commit| |Code style: black| |Build Status| |codecov|\n\nA selector expression for extracting data from JSON.\n\nQuickstarts\n<<<<<<<<<<<\n\n\nInstallation\n~~~~~~~~~~~~\n\nInstall the stable version from PYPI.\n\n.. code-block:: shell\n\n    pip install jsonpath-extractor\n\nOr install the latest version from Github.\n\n.. code-block:: shell\n\n    pip install git+https://github.com/linw1995/jsonpath.git@master\n\nUsage\n~~~~~\n\n.. code-block:: json\n\n    {\n        "goods": [\n            {"price": 100, "category": "Comic book"},\n            {"price": 200, "category": "magazine"},\n            {"price": 200, "no category": ""}\n        ],\n        "targetCategory": "book"\n    }\n\n\nHow to parse and extract all the comic book data from the above JSON file.\n\n.. code-block:: python3\n\n    import json\n\n    from jsonpath import parse\n\n    with open("example.json", "r") as f:\n        data = json.load(f)\n\n    assert parse("$.goods[contains(@.category, $.targetCategory)]").find(\n        data\n    ) == [{"price": 100, "category": "Comic book"}]\n\nOr use the `jsonpath.core <https://jsonpath.readthedocs.io/en/latest/api_core.html>`_ module to extract it.\n\n.. code-block:: python3\n\n    from jsonpath.core import Root, Contains, Self\n\n    assert Root().Name("goods").Array(\n        Contains(Self().Name("category"), Root().Name("targetCategory"))\n    ).find(data) == [{"price": 100, "category": "Comic book"}]\n\nChangelog\n<<<<<<<<<\n\nv0.2.0-alpha\n~~~~~~~~~~~~\n\n- 1be3dbf New:Add scripts/export_requirements_txt.sh\n- 56d09bd Chg:Upgrade dependencies\n- ba5868c Chg:Update GitHub Actions config\n- 944fe7b New:Add caches action\n- 8625aeb New:Upload release built from actions\n- b882c38 Chg:Use lark-parser to replace sly\n- dad27f8 Fix,Dev:CI err because of poetry install git dep\n- 1fd8c41 Chg:Replace tab with space in grammar.lark\n- e1a73a4 Chg:more specific type annotation\n- 9dbbdfb Chg:Upgrade lark to 0.8.1\n- b62b848 Chg:Rafactoring for reducing non-neccessory code\n- b84fb93 Fix:Not raise JSONPath undefined function error explicitly\n- d9ff6f6 Chg:Use type.__new__ to overwrite expr\'s find method\n- 3b8d41d Chg:Refactoring for reducing the duplicated code\n- ce42257 New:Create docs by sphinx\n- bb31c2c Fix,Dev:lint docs error\n- b09ec5e New,Dev:Watch related files,\n  build and serve Sphinx documentation automatically.\n- a078e8f Fix,Dev:Isort error\n- db56773 New,Dev:Test with doctest by pytest\n- 48ad21c Fix,Dev:shell function not inherits envs of parent process\n- 28a4fc0 Fix,Dev:lint error\n- a78fdf8 Fix,Dev:Live reload docs error\n  due to .venv/bin/python not setting env-values\n- 2995f46 New,Doc:API reference\n- d918d80 Chg,Doc:Update quickstarts.rst\n- f18d92c New:Add .readthedocs.yaml for docs deployment\n- e6b7576 New,Doc:Translate :py:mod: directive into link\n\n\n\n.. |license| image:: https://img.shields.io/github/license/linw1995/jsonpath.svg\n    :target: https://github.com/linw1995/jsonpath/blob/master/LICENSE\n\n.. |Pypi Status| image:: https://img.shields.io/pypi/status/jsonpath-extractor.svg\n    :target: https://pypi.org/project/jsonpath-extractor\n\n.. |Python version| image:: https://img.shields.io/pypi/pyversions/jsonpath-extractor.svg\n    :target: https://pypi.org/project/jsonpath-extractor\n\n.. |Package version| image:: https://img.shields.io/pypi/v/jsonpath-extractor.svg\n    :target: https://pypi.org/project/jsonpath-extractor\n\n.. |PyPI - Downloads| image:: https://img.shields.io/pypi/dm/jsonpath-extractor.svg\n    :target: https://pypi.org/project/jsonpath-extractor\n\n.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/linw1995/jsonpath.svg\n    :target: https://github.com/linw1995/jsonpath\n\n.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n\n.. |Build Status| image:: https://img.shields.io/github/workflow/status/linw1995/jsonpath/Python%20package\n    :target: https://github.com/linw1995/jsonpath/actions?query=workflow%3A%22Python+package%22\n\n.. |codecov| image:: https://codecov.io/gh/linw1995/jsonpath/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/linw1995/jsonpath\n',
    'author': '林玮',
    'author_email': 'linw1995@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/linw1995/jsonpath',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
