# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttp_tus']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0']

setup_kwargs = {
    'name': 'aiohttp-tus',
    'version': '1.0.0a0',
    'description': 'tus.io protocol implementation for aiohttp.web applications',
    'long_description': '===========\naiohttp-tus\n===========\n\n.. image:: https://github.com/pylotcode/aiohttp-tus/workflows/ci/badge.svg\n   :target: https://github.com/pylotcode/aiohttp-tus/actions?query=workflow%3A%22ci%22\n   :alt: CI Workflow\n\n`tus.io <https://tus.io>`_ server implementation for\n`aiohttp.web <https://docs.aiohttp.org/en/stable/web.html>`_ applications.\n\nFor uploading large files, please consider using\n`aiotus <https://pypi.org/project/aiotus/>`_ (Python 3.7+) library instead.\n\n- Works on Python 3.6+\n- Works with aiohttp 3.5+\n- BSD licensed\n- Source, issues, and pull requests `on GitHub\n  <https://github.com/pylotcode/aiohttp-tus>`_\n\nQuickstart\n==========\n\nCode belows shows how to enable tus-compatible uploads on ``/uploads`` URL for\n``aiohttp.web`` application. After upload, files will be available at ``../uploads``\ndirectory.\n\n.. code-block:: python\n\n    from pathlib import Path\n\n    from aiohttp import web\n    from aiohttp_tus import setup_tus\n\n\n    app = setup_tus(\n        web.Application(),\n        upload_url="/uploads",\n        upload_path=Path(__file__).parent.parent / "uploads",\n    )\n',
    'author': 'Igor Davydenko',
    'author_email': 'iam@igordavydenko.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pylotcode/aiohttp-tus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
