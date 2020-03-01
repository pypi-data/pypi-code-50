# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli_parser']

package_data = \
{'': ['*'], 'cli_parser': ['.git/*', '.git/hooks/*', '.git/info/*']}

setup_kwargs = {
    'name': 'cli-parser',
    'version': '0.1.3',
    'description': 'Simple CLI Parser with command chaining',
    'long_description': '# CLI Parser\n## Simple Chained Command Parser\n\nThis tool will allow you to create a simple command hierarchy to execute from the command line.\n\n### Example\n```python\nfrom cli_parser import command, CliParser, ParentCommand, CommandException\n\nget = ParentCommand(\'get\')\n\n@command\ndef product(x, y):\n    return x * y\n\n@command\ndef sum(x, y):\n    return x + y\n    \nget.add_sub_cmds(product, sum)\n\nparser = CliParser([get])\n\nwhile True:\n    in_ = input("Enter command:\\n==> ")\n    \n    try:\n        response = parser.process_response(in_)\n        print(response)\n    except CommandException:\n       pass\n```  \n\nExecute your script from the command line:\n\n```\nEnter command:\n==> get product 5 10\n50\n\nEnter command:\n==> get sum 10 20\n30\n\nEnter command:\n==> q\n\n\'Quitting Interpreter\'\n\n```\n\npypi: https://pypi.org/project/cli-parser/',
    'author': 'Ran Zvi',
    'author_email': 'ran.zvi@bluevine.com',
    'maintainer': 'Ran Zvi',
    'maintainer_email': 'ran.zvi@bluevine.com',
    'url': 'https://github.com/ranzvi/cli_parser',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
