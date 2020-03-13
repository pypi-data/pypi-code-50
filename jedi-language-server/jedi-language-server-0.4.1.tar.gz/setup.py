# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jedi_language_server']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0', 'jedi>=0.15.1', 'pygls>=0.8.1']

entry_points = \
{'console_scripts': ['jedi-language-server = jedi_language_server.cli:cli']}

setup_kwargs = {
    'name': 'jedi-language-server',
    'version': '0.4.1',
    'description': 'A language server for Jedi!',
    'long_description': '# jedi-language-server\n\n[![image-version](https://img.shields.io/pypi/v/jedi-language-server.svg)](https://python.org/pypi/jedi-language-server)\n[![image-license](https://img.shields.io/pypi/l/jedi-language-server.svg)](https://python.org/pypi/jedi-language-server)\n[![image-python-versions](https://img.shields.io/pypi/pyversions/jedi-language-server.svg)](https://python.org/pypi/jedi-language-server)\n\nA [Language Server](https://microsoft.github.io/language-server-protocol/) for the latest version(s) [Jedi](https://jedi.readthedocs.io/en/latest/).\n\n**Note:** this tool is actively used by its primary author. He\'s happy to review pull requests / respond to issues you may discover.\n\n## Installation\n\nFrom your command line (bash / zsh), run:\n\n```bash\npip install -U jedi jedi-language-server\n```\n\n`-U` ensures that you\'re pulling the latest version from pypi.\n\n## Overview\n\njedi-language-server aims to support all of Jedi\'s capabilities and expose them through the Language Server Protocol. It currently supports the following Language Server requests:\n\n* [textDocument/completion](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_completion)\n* [textDocument/definition](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_definition)\n* [textDocument/documentSymbol](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_documentSymbol)\n* [textDocument/hover](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_hover)\n* [textDocument/references](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_references)\n* [textDocument/rename](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#textDocument_rename)\n* [workspace/symbol](https://microsoft.github.io/language-server-protocol/specifications/specification-current/#workspace_symbol)\n\nThese language server requests are not currently configurable by the user, but we expect to relax this constraint in a future release.\n\n## Usage\n\nThe following instructions show how to use jedi-language-server with your development tooling. The instructions assume you have already installed jedi-language-server.\n\n### Command line (bash / zsh)\n\nAt your terminal prompt:\n\n```bash\njedi-language-server\n```\n\njedi-language-server currently works only over IO. This may change in the future.\n\n### Neovim\n\nConfigure jedi-language-server with [coc.nvim](https://github.com/neoclide/coc.nvim/wiki/Language-servers#register-custom-language-servers). For diagnostics, we recommend installing and using the latest version of [efm-langserver](git@github.com:mattn/efm-langserver.git) + [pylint](https://github.com/PyCQA/pylint).\n\n~/.config/nvim/coc-settings.json:\n\n```json\n"languageserver": {\n  "efm": {\n    "command": "efm-langserver",\n    "args": [],\n    "filetypes": ["python"]\n  },\n  "jls": {\n    "command": "jedi-language-server",\n    "args": [],\n    "filetypes": ["python"]\n  }\n}\n```\n\n~/.config/efm-langserver/config.yaml:\n\n```yaml\nversion: 2\ntools:\n  python-pylint: &python-pylint\n    lint-command: \'pylint\'\n    lint-formats:\n      - \'%f:%l:%c: %t%m\'\nlanguages:\n  python:\n    - <<: *python-pylint\n```\n\n## Local Development\n\nLike everything else in this project, local development is quite simple.\n\n### Dependencies\n\nInstall the following tools manually.\n\n* [Poetry](https://github.com/sdispater/poetry#installation)\n* [GNU Make](https://www.gnu.org/software/make/)\n\n#### Recommended\n\n* [asdf](https://github.com/asdf-vm/asdf)\n\n### Set up development environment\n\n```bash\nmake setup\n```\n\n### Run tests\n\n```bash\nmake test\n```\n\n## Inspiration\n\nPalantir\'s [python-language-server](https://github.com/palantir/python-language-server) inspired this project. jedi-language-server differs from python-language-server. jedi-language-server:\n\n* Uses `pygls` instead of creating its own low-level Language Server Protocol bindings\n* Supports one powerful 3rd party library: Jedi. By only supporting Jedi, we can focus on supporting all Jedi features without exposing ourselves to too many broken 3rd party dependencies (I\'m looking at you, [rope](https://github.com/python-rope/rope)).\n* Is supremely simple. Given its scope constraints, it will continue to be super simple and leave complexity to the Jedi [master](https://github.com/davidhalter). Feel free to submit a PR!\n\n## Written by\n\nSamuel Roeca *samuel.roeca@gmail.com*\n',
    'author': 'Sam Roeca',
    'author_email': 'samuel.roeca@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pappasam/jedi-language-server',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
