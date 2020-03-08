# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['typer_cli']

package_data = \
{'': ['*']}

install_requires = \
['click-completion>=0.5.2,<0.6.0',
 'colorama>=0.4.3,<0.5.0',
 'importlib_metadata>=1.5,<2.0',
 'typer>=0.0.8,<0.0.9']

entry_points = \
{'console_scripts': ['typer = typer_cli.main:main']}

setup_kwargs = {
    'name': 'typer-cli',
    'version': '0.0.2',
    'description': '',
    'long_description': '# Typer CLI\n\nEasily run your **Typer** applications without installing them, using **Typer CLI**.\n\n⚠️ **WARNING**: If you are building a CLI package you probably need [**Typer**](https://typer.tiangolo.com/), the library itself. This, **Typer CLI**, is a CLI application that simplifies running simple **Typer** applications, it is not the library itself.\n\n## Description\n\n**Typer** is a library for building CLIs (Command Line Interface applications).\n\n**Typer CLI** is a CLI application that simplifies running simple programs created with **Typer**.\n\nThe main feature it does is provide completion for your own programs built with **Typer** without you having to install them locally as a package.\n\nIt\'s probably most useful if you have a small custom Python script using **Typer** that is part of some project, for some small tasks, and it\'s not complex/important enough to build a whole CLI package for it (something to be installed with `pip`).\n\nIn that case, you can install **Typer CLI**, and run your program with `typer`, and it will provide completion for your script.\n\n## Usage\n\nInstall **Typer CLI**:\n\n```console\n$ python -m pip install typer-cli\n```\n\nThat creates a `typer` command.\n\nYou can then install completion for it:\n\n```console\n$ typer --install-completion\n```\n\nThen, let\'s say you have a script that uses **Typer** in `my_custom_script.py`:\n\n```Python\nimport typer\n\napp = typer.Typer()\n\n\n@app.command()\ndef hello(name: str = None):\n    if name:\n        typer.echo(f"Hello {name}")\n    else:\n        typer.echo("Hello World!")\n\n\n@app.command()\ndef bye(name: str = None):\n    if name:\n        typer.echo(f"Bye {name}")\n    else:\n        typer.echo("Goodbye!")\n\n\nif __name__ == "__main__":\n    app()\n```\n\nThen you could call it with normal Python:\n\n```console\n$ python my_custom_script.py hello\n\nHello World!\n\n$ python my_custom_script.py hello --name Camila\n\nHello Camila!\n\n$ python my_custom_script.py bye --name Camila\n\nBye Camila\n```\n\nBut you won\'t get completion in your terminal for any of the subcommands or options, like `hello`, `bye`, and `--name`.\n\nHere\'s where **Typer CLI** is useful. You can also run it with the `typer` command you get after installing `typer-cli`:\n\n```console\n$ typer my_custom_script.py run hello\n\nHello World!\n\n$ typer my_custom_script.py run hello --name Camila\n\nHello Camila!\n\n$ typer my_custom_script.py run bye --name Camila\n\nBye Camila\n```\n\nInstead of typing `python`, you type `typer`, and after the name of the file you add a `run` (that will be autocompleted with when you hit <kbd>TAB</kbd>) and it will give you completion for all the commands and options when you hit <kbd>TAB</kbd>.\n\n## If main\n\nBecause **Typer CLI** won\'t use the block with:\n\n```Python\nif __name__ == "__main__":\n    app()\n```\n\nYou can also remove it if you are calling that script only with **Typer CLI** (using the `typer` command).\n',
    'author': 'Sebastián Ramírez',
    'author_email': 'tiangolo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
