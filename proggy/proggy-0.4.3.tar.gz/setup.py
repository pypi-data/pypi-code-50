# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proggy', 'proggy.tty']

package_data = \
{'': ['*']}

install_requires = \
['typing_extensions>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'proggy',
    'version': '0.4.3',
    'description': 'A progress bar generator.',
    'long_description': "Proggy\n======\n\nProgressively progressing through progress bar generation.\n\nProggy generates text-based progress bars. Mildly inspired by Rust's\n[indicatif](https://github.com/mitsuhiko/indicatif).\n\nProggy only renders progress bars to a string. Displaying them is, as of now,\nnot handled and left to the user.\n\nExamples\n--------\n\n### API usage\n\n```\n>>> from proggy import ProgressBar\n>>> pb = ProgressBar(30, 100, progress=75)\n>>> pb.render()\n'⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       '\n```\n\n### CLI output\n\n#### Single progress bar (`test.py`):\n```python\nimport time\n\nfrom proggy import BarInfo\nfrom proggy.tty import TTYProgressBar\n\n\nwith TTYProgressBar(BarInfo(size=30, total=100)) as p:\n    for i in range(100):\n        time.sleep(0.1)\n        p.progress += 1\n```\n\nOutput:\n\n![test.py output](gif/test.gif)\n\n#### Multi-progress bar with `asyncio` (`async_test.py`):\n```\nfrom asyncio import ensure_future, run, sleep\n\nfrom proggy import BarInfo, LogicalProgressBar\nfrom proggy.types import ProgressBar\nfrom proggy.tty import TTYMultiProgressBar\n\n\nasync def task1(p: ProgressBar):\n    for _ in range(100):\n        await sleep(0.1)\n        p.progress += 1\n\n\nasync def task2(p: ProgressBar):\n    for _ in range(50):\n        await sleep(0.1)\n        p.progress += 1\n\n\nasync def main():\n    with TTYMultiProgressBar(bar_infos=[\n        BarInfo(size=30, total=100),\n        BarInfo(size=30, total=50),\n    ]) as mp:\n        x = ensure_future(task1(mp.bar_at(0)))\n        await task2(mp.bar_at(1))\n        await x\n\nrun(main())\n```\n\nOutput:\n\n![async_test.py output](gif/async_test.gif)\n",
    'author': 'Tarcísio Eduardo Moreira Crocomo',
    'author_email': 'tarcisioe@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
