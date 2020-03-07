# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioimport']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aioimport',
    'version': '0.1.1',
    'description': 'Asynchronous module import for asyncio',
    'long_description': '# aioimport\nAsynchronous module import for asyncio\n\n## Getting Started\n\n### Installing\n\nInstall from [PyPI](https://pypi.org/project/aioimport/) using:\n\n```\npip install aioimport\n```\n\n### The problem\n\nSome nasty modules have long running operations during import\n\n### The naive solution\n\nFirst thing that comes to mind is to postpone import by moving it into the function that need that module:\n\n```python\nasync def my_work(self) -> None:\n    import this  # will block until imported\n```\n\nIt reduces your startup time, but it is still blocking your event loop.\n\nThat\'s where `aioimport` comes in.\n\n### Usage\n\nThe preferred way to use `aioimport` is:\n```python\nimport aioimport\n\nasync def my_work(self) -> None:\n    await aioimport.cache_module("this")  # will asynchronously import module\n    import this  # will be instantaneous since `this` is already in import cache \n```\n\nAlso `aioimport` can be also used the following way:\n```python\nimport aioimport\n\nasync def my_work(self) -> None:\n    this = await aioimport.import_module("this")  # will asynchronously import module\n    # now `this` has exactly the same module as you would have gotten be doing `import this`\n```\nBut your types will be all messed up.\n\n### How it works\n\nModule import is done in thread executor.\n\nBe aware of the fact that GIL still exists and technically import is done concurrently rather than in parallel with your code.\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details\n',
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
