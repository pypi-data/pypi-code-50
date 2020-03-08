# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioimport']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aioimport',
    'version': '0.1.4',
    'description': 'Asynchronous module import for asyncio',
    'long_description': '# aioimport\nAsynchronous module import for asyncio\n\n## Getting Started\n\n### Installing\n\nInstall from [PyPI](https://pypi.org/project/aioimport/) using:\n\n```\npip install aioimport\n```\n\n### The problem\n\nSome naughty modules have long running operations during import\n\n#### Naive solution\n\nFirst thing that comes to mind is make import local:\n\n```python\nasync def my_work() -> None:\n    import naughty  # will block event loop\n```\n\nIt reduces time your program takes to start (or library to import),\nbut it is still blocking your event loop.\n\n### Usage\n\n```python\nimport aioimport\n\nasync def my_work() -> None:\n    await aioimport.import_module("naughty")  # will asynchronously import module\n    import naughty  # will be instantaneous since `naughty` is already in `sys.modules`\n    await aioimport.reload(naughty)  # and you can asynchronously reload modules too\n```\n\n### How it works\n\nModule import is done in asyncio default executor.\n\nBe aware of the fact that GIL still exists and technically import is done concurrently rather than in parallel with your code.\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details\n',
    'author': 'rndr',
    'author_email': 'rndr@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rndr/aioimport',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
