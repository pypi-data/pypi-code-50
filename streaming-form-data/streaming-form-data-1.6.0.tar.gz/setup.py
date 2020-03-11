# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['streaming_form_data']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'streaming-form-data',
    'version': '1.6.0',
    'description': 'Streaming parser for multipart/form-data',
    'long_description': "Streaming multipart/form-data parser\n====================================\n\n.. image:: https://github.com/siddhantgoel/streaming-form-data/workflows/streaming-form-data/badge.svg\n    :target: https://github.com/siddhantgoel/streaming-form-data/workflows/streaming-form-data/badge.svg\n\n.. image:: https://badge.fury.io/py/streaming-form-data.svg\n    :target: https://pypi.python.org/pypi/streaming-form-data\n\n.. image:: https://readthedocs.org/projects/streaming-form-data/badge/?version=latest\n    :target: https://streaming-form-data.readthedocs.io/en/latest/\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n\n\n:code:`streaming_form_data` provides a Python parser for parsing\n:code:`multipart/form-data` input chunks (the most commonly used encoding when\nsubmitting data over HTTP through HTML forms).\n\nInstallation\n------------\n\n.. code-block:: bash\n\n    $ pip install streaming-form-data\n\nIn case you prefer cloning the Github repository and installing manually, please\nnote that :code:`master` is the development branch, so :code:`stable` is what\nyou should be working with.\n\nUsage\n-----\n\n.. code-block:: python\n\n    >>> from streaming_form_data import StreamingFormDataParser\n    >>> from streaming_form_data.targets import ValueTarget, FileTarget, NullTarget\n    >>>\n    >>> headers = {'Content-Type': 'multipart/form-data; boundary=boundary'}\n    >>>\n    >>> parser = StreamingFormDataParser(headers=headers)\n    >>>\n    >>> parser.register('name', ValueTarget())\n    >>> parser.register('file', FileTarget('/tmp/file.txt'))\n    >>> parser.register('discard-me', NullTarget())\n    >>>\n    >>> for chunk in request.body:\n    ...     parser.data_received(chunk)\n    ...\n    >>>\n\nDocumentation\n-------------\n\nUp-to-date documentation is available on `Read the Docs`_.\n\nDevelopment\n-----------\n\nPlease make sure you have Python 3.5+ and Poetry_ installed.\n\n1. Git clone the repository -\n   :code:`git clone https://github.com/siddhantgoel/streaming-form-data`\n\n2. Install the packages required for development -\n   :code:`poetry install`\n\n3. That's basically it. You should now be able to run the test suite -\n   :code:`poetry run py.test`.\n\nPlease note that :code:`tests/test_parser_stress.py` stress tests the parser\nwith large inputs, which can take a while. As an alternative, pass the filename\nas an argument to :code:`py.test` to run tests selectively.\n\n\n.. _Poetry: https://poetry.eustace.io/\n.. _Read the Docs: https://streaming-form-data.readthedocs.io/\n",
    'author': 'Siddhant Goel',
    'author_email': 'me@sgoel.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/siddhantgoel/streaming-form-data',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
