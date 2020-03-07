# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioimport']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aioimport',
    'version': '0.1.2',
    'description': 'Asynchronous module import for asyncio',
    'long_description': '# aioimport\nAsynchronous module import for asyncio\n\n## Getting Started\n\n### Installing\n\nInstall from [PyPI](https://pypi.org/project/aioimport/) using:\n\n```\npip install aioimport\n```\n\n### The problem\n\nSome nasty modules have long running operations during import\n\n### Naive solution\n\nFirst thing that comes to mind is to postpone import by moving it into the function that need that module:\n\n```python\nasync def my_work(self) -> None:\n    import this  # will block until imported\n```\n\nIt reduces your startup time, but it is still blocking your event loop.\n\n### Usage\n\nThe preferred way to use `aioimport` is:\n```python\nimport aioimport\n\nasync def my_work(self) -> None:\n    await aioimport.import_module("this")  # will asynchronously import module\n    import this  # will be instantaneous since `this` is already in `sys.modules`\n    # and you can asynchronously reload it too:\n    await aioimport.reload(this)\n```\n\n### How it works\n\nModule import is done in new thread worker.\n\nBe aware of the fact that GIL still exists and technically import is done concurrently rather than in parallel with your code.\n\n## Future work\n\nCurrently after your first use of `aioimport` it\'s workers threads run forever waiting for new imports.\n\nThe plan is to have some form of automatic shutdown after some time passes since last import.\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details\n',
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
