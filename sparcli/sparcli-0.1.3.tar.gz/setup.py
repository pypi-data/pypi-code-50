# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sparcli']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.1,<2.0.0']

setup_kwargs = {
    'name': 'sparcli',
    'version': '0.1.3',
    'description': 'Visualize metrics as text in real-time (sparklines)',
    'long_description': '# Sparcli\n\nSparcli is a library for visualising metrics on the command line.\n\nUse this library to see the shape of data during execution of data pipelines, simulators and other long-running programs. Each metric is displayed as a sparkline that updates as the data changes. Sparcli is thread-safe and non-blocking.\n\n![Build](https://github.com/z0u/sparcli/workflows/Build/badge.svg)\n![Publish](https://github.com/z0u/sparcli/workflows/Publish/badge.svg)\n![Canary build](https://github.com/z0u/sparcli/workflows/Canary%20build/badge.svg)\n\n\n## Usage\n\nSparcli is [available on pypi](https://pypi.org/project/sparcli/):\n\n```sh\npip install sparcli\n```\n\nYou can wrap an iterable that produces scalars:\n\n```python\nimport sparcli, time\n\nfor y in sparcli.gen(ys, name="y"):\n    do_something(y)\n```\n\nYou can produce metrics using a context manager:\n\n```python\nwith sparcli.ctx() as ctx:\n    for a, b in do_something_else():\n        ctx.record(a=a, b=b)\n```\n\nYou can also manage the context manually. Just don\'t forget to close it:\n\n```python\nclass MyMetricsPlugin:\n    def start(self):\n        self.ctx = sparcli.context()\n\n    def callback(self, metrics: Dict[str, Real]):\n        self.ctx.record(**metrics)\n\n    def stop(self):\n        self.ctx.close()\n\nsome_library.register_plugin(MyPlugin())\n```\n\n\n## Development\n\n```sh\npip install --user py-make poetry\npoetry install\npymake all\n```\n\n```sh\npoetry run python demo.py\n```\n',
    'author': 'Alex Fraser',
    'author_email': 'alex.d.fraser@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/z0u/sparcli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
