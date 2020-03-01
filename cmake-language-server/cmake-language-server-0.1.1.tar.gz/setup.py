# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cmake_language_server']

package_data = \
{'': ['*']}

install_requires = \
['pygls>=0.8.1,<0.9.0', 'pyparsing>=2.4,<3.0']

entry_points = \
{'console_scripts': ['cmake-format = cmake_language_server.formatter:main',
                     'cmake-language-server = '
                     'cmake_language_server.server:main']}

setup_kwargs = {
    'name': 'cmake-language-server',
    'version': '0.1.1',
    'description': 'CMake LSP Implementation',
    'long_description': '# cmake-language-server\n[![PyPI](https://img.shields.io/pypi/v/cmake-language-server)](https://pypi.org/project/cmake-language-server)\n[![AUR version](https://img.shields.io/aur/version/cmake-language-server)](https://aur.archlinux.org/packages/cmake-language-server/)\n[![GitHub Actions (Tests)](https://github.com/regen100/cmake-language-server/workflows/Tests/badge.svg)](https://github.com/regen100/cmake-language-server/actions)\n[![codecov](https://codecov.io/gh/regen100/cmake-language-server/branch/master/graph/badge.svg)](https://codecov.io/gh/regen100/cmake-language-server)\n[![GitHub](https://img.shields.io/github/license/regen100/cmake-language-server)](https://github.com/regen100/cmake-language-server/blob/master/LICENSE)\n\nCMake LSP Implementation.\n\nAlpha Stage, work in progress.\n\n## Features\n- [x] Builtin command completion\n- [x] Documentation for commands and variables on hover\n- [x] Formatting\n\n## Commands\n\n- `cmake-language-server`: LSP server\n- `cmake-format`: CLI frontend for formatting\n\n## Installation\n\n```bash\n$ pip install cmake-language-server\n```\n\n### Clients\n\n- Neovim ([neoclide/coc.nvim][coc.nvim])\n\n#### Neovim\n\n```jsonc\n  "languageserver": {\n    "cmake": {\n      "command": "cmake-language-server",\n      "filetypes": ["cmake"],\n      "rootPatterns": [\n        "build/"\n      ],\n      "initializationOptions": {\n        "buildDirectory": "build"\n      }\n    }\n  }\n```\n\n\n[coc.nvim]: https://github.com/neoclide/coc.nvim\n',
    'author': 'regen',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/regen100/cmake-language-server',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
