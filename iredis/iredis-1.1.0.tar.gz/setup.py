# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iredis', 'iredis.data', 'iredis.data.commands']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2,<3',
 'click>=7.0,<8.0',
 'configobj>=5.0.6,<6.0.0',
 'importlib_resources>=1.0.2,<2.0.0',
 'mistune>=0.8.4,<0.9.0',
 'pendulum>=2.0.5,<3.0.0',
 'prompt_toolkit>=3,<4',
 'redis>=3,<4']

entry_points = \
{'console_scripts': ['iredis = iredis.entry:main']}

setup_kwargs = {
    'name': 'iredis',
    'version': '1.1.0',
    'description': 'Terminal client for Redis with auto-completion and syntax highlighting.',
    'long_description': '<p align="center">\n  <img width="100" height="100" src="https://raw.githubusercontent.com/laixintao/iredis/master/docs/assets/logo.png" />\n</p>\n\n<h3 align="center">Interactive Redis: A Cli for Redis with AutoCompletion and Syntax Highlighting.</h4>\n\n<p align="center">\n<a href="https://github.com/laixintao/iredis/actions"><img src="https://github.com/laixintao/iredis/workflows/Test/badge.svg" alt="Github Action"></a>\n<a href="https://badge.fury.io/py/iredis"><img src="https://badge.fury.io/py/iredis.svg" alt="PyPI version"></a>\n<img src="https://badgen.net/badge/python/3.6%20|%203.7%20|%203.8/" alt="Python version">\n<a href="https://t.me/iredis_users"><img src="https://badgen.net/badge/icon/join?icon=telegram&amp;label=usergroup" alt="Chat on telegram"></a>\n<a href="https://console.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/laixintao/iredis&amp;cloudshell_print=docs/cloudshell/run-in-docker.txt"><img src="https://badgen.net/badge/run/GoogleCloudShell/blue?icon=terminal" alt="Open in Cloud Shell"></a>\n</p>\n\n<p align="center">\n  <img src="./docs/assets/demo.svg" alt="demo">\n</p>\n\nIRedis is a terminal client for redis with auto-completion and syntax highlighting. IRedis lets you type Redis commands smoothly, and displays results in a user-friendly format.\n\nIRedis is an alternative for redis-cli. In most cases, IRedis behaves exactly the same as redis-cli. Besides, it is safer to use IRedis on production servers than redis-cli: IRedis will prevent accidentally running dangerous commands, like `KEYS *` (see [Redis docs / Latency generated by slow commands](https://redis.io/topics/latency#latency-generated-by-slow-commands)).\n\n\n## Features\n\n- Advanced code completion. If you run command `KEYS` then run `DEL`, IRedis will auto-complete your command based on `KEYS` result.\n- Command validation. E.g. try `CLUSTER MEET IP PORT`, iredis will validate IP and PORT for you.\n- Command highlighting, fully based on redis grammar. Any valid command in IRedis shell is a valid redis command.\n- Human-friendly result display.\n- `peek` command to check the key\'s type then automatically call `get`/`lrange`/`sscan`, etc, depending on types. You don\'t need to call the `type` command then type another command to get the value. `peek` will also display the key\'s length and memory usage.\n- <kbd>Ctrl</kbd> + <kbd>C</kbd> to cancel the current typed command, this won\'t exit iredis, exactly like bash behaviour. Use <kbd>Ctrl</kbd> + <kbd>D</kbd> to send a EOF to exit iredis.\n- Says "Goodbye!" to you when you exit!\n- <kbd>Ctrl</kbd> + <kbd>R</kbd> to open **reverse-i-search** to search through your command history.\n- Auto suggestions. (Like [fish shell](http://fishshell.com/).)\n- Support `--encode=utf-8`, to decode Redis\' bytes responses.\n- Command hint on bottom, include command syntax, supported redis version, and time complexity.\n- Offcial docs with built-in `HELP` command, try `HELP SET`!\n- Written in pure Python, but IRedis was packaged into a single binary with\n[PyOxidizer](https://github.com/indygreg/PyOxidizer), you can use cURL to\ndownload and run, it just works, even you don\'t have a Python interpreter.\n- For full features, please see: [iredis.io/show](https://www.iredis.io/show/)\n\n## Install\n\nInstall via pip:\n\n```\npip install iredis\n```\n\n[pipx](https://github.com/pipxproject/pipx) is recommended:\n\n```\npipx install iredis\n```\n\nOr you can download the executable binary with cURL(or wget), untar, then run.\nIt is especially useful when you don\'t have a python interpreter(E.g. the\nofficial docker image of redis doesn\'t have python):\n\n```\nwget https://github.com/laixintao/iredis/releases/download/latest/iredis.tar.gz \\\n && tar -xzf iredis.tar.gz  \\\n && ./iredis\n```\n\n(Please replace `latest` in the URL to `v1.x.x` if you want to use an old version \nof iredis)\n\n## Usage\n\nOnce you install IRedis, you will know how to use it. Just remember, IRedis\nsupports similar options like redis-cli, like `-h` for redis-server\'s host\nand `-p` for port. \n\n```\n$ iredis --help\n```\n\n### Configuration\n\nIRedis supports config files. Command-line options will always take precedence\nover config. Configuration resolution from highest to lowest precedence is:\n\n- *Options from command line*\n- `$PWD/.iredisrc`\n- `~/.iredisrc` (this path can be changed with `iredis --iredisrc $YOUR_PATH`)\n- `/etc/iredisrc`\n- default config in IRedis package.\n\nYou can copy the *self-explained* default config here:\n\nhttps://raw.githubusercontent.com/laixintao/iredis/master/iredis/data/iredisrc\n\n\nAnd then make your own changes.\n\n(If you are using an old verions of iredis, please use the config file below,\nand change the version in url):\n\nhttps://raw.githubusercontent.com/laixintao/iredis/v1.0.4/iredis/data/iredisrc\n\n### Keys\n\nIRedis support unix/readline-style REPL keyboard shortcuts, which means keys like\n<kbd>Ctrl</kbd> + <kbd>F</kbd> to forward work.\n\nAlso:\n\n- <kbd>Ctrl</kbd> + <kbd>F</kbd> (i.e. EOF) to exit; you can also use the `exit` command.\n- <kbd>Ctrl</kbd> + <kbd>L</kbd> to clear screen; you can also use the `clear` command.\n- <kbd>Ctrl</kbd> + <kbd>X</kbd> <kbd>Ctrl</kbd> + <kbd>E</kbd> to open an editor\nto edit command, or <kbd>V</kbd> in vi-mode.\n\n## Development\n\n### Release Strategy\n\nIRedis is built and released by CircleCI. Whenever a tag is pushed to the `master` branch, a new release is built and uploaded to pypi.org, it\'s very convenient.\n\nThus, we release as often as possible, so that users can always enjoy the new features and bugfixes quickly. Any bugfix or new feature will get at least a patch release, whereas big features will get a minor release.\n\n### Setup Environment\n\nIRedis favors [poetry](https://github.com/sdispater/poetry) as package management tool. To setup a develop enviroment on your computer:\n\nFirst, install poetry (you can do it in a python\'s virtualenv):\n\n```\npip install poetry\n```\n\nThen run (which is similar to `pip install -e .`):\n\n```\npoetry install\n```\n\n**Be careful running testcases locally, it may flush you db!!!**\n\n### Development Logs\n\nThis is a command-line tool, so we don\'t write logs to stdout.\n\nYou can `tail -f ~/.iredis.log` to see logs, the log is pretty clear,\nyou can see what actually happens from log files.\n\n### CI\n\nWe use [pexpect](https://pexpect.readthedocs.io/en/stable/) to test command-line\nbehavior. And since there are problems with CircleCI\'s tty, we run\npexpect-related tests on travis, and run unittest/black style check/flake8 check\non CircleCI.\n\nFor local development, just run `pytest`. If all tests pass locally, CI shall pass.\n\n### Command Reference\n\nThere is a full Redis command list in [commands.csv](docs/commands.csv) file, downloaded by:\n\n```\npython scripts/download_redis_commands.py > data/commands.csv\n```\n\n`commands.csv` is here only for test if redis.io was updated, do not package it into release.\n\nCurrent implemented commands: [command_syntax.csv](iredis/data/command_syntax.csv).\n\n## Related Projects\n\n- [redis-tui](https://github.com/mylxsw/redis-tui)\n\nIf you like iredis, you may also like other cli tools by [dbcli](https://www.dbcli.com/):\n\n- [pgcli](https://www.pgcli.com) - Postgres Client with Auto-completion and Syntax Highlighting\n- [mycli](https://www.mycli.net) - MySQL/MariaDB/Percona Client with Auto-completion and Syntax Highlighting\n- [litecli](https://litecli.com) - SQLite Client with Auto-completion and Syntax Highlighting\n- [mssql-cli](https://github.com/dbcli/mssql-cli) - Microsoft SQL Server Client with Auto-completion and Syntax Highlighting\n- [athenacli](https://github.com/dbcli/athenacli) - AWS Athena Client with Auto-completion and Syntax Highlighting\n- [vcli](https://github.com/dbcli/vcli) - VerticaDB client\n- [iredis](https://github.com/laixintao/iredis/) -  Client for Redis with AutoCompletion and Syntax Highlighting\n\nIRedis is build on the top of [prompt_toolkit](https://github.com/jonathanslenders/python-prompt-toolkit), a Python library (by [Jonathan Slenders](https://twitter.com/jonathan_s)) for building rich commandline applications.\n',
    'author': 'laixintao',
    'author_email': 'laixintao1995@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/laixintao/iredis',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
