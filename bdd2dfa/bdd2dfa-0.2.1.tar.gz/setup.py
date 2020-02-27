# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bdd2dfa']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0', 'dfa>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'bdd2dfa',
    'version': '0.2.1',
    'description': 'Python library for converting binary decision diagrams to automata.',
    'long_description': '# bdd2dfa\n\n[![Build Status](https://cloud.drone.io/api/badges/mvcisback/bdd2dfa/status.svg)](https://cloud.drone.io/mvcisback/bdd2dfa)\n[![codecov](https://codecov.io/gh/mvcisback/bdd2dfa/branch/master/graph/badge.svg)](https://codecov.io/gh/mvcisback/bdd2dfa)\n[![PyPI version](https://badge.fury.io/py/bdd2dfa.svg)](https://badge.fury.io/py/bdd2dfa)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n\nA simple python wrapper around Binary Decision Diagrams (BDDs) to interpret them\nas Deterministic Finite Automata (DFAs).\n\nThe package takes as input a BDD from the [`dd` package](https://github.com/tulip-control/dd)\nand returns a DFA from the [`dfa` package](https://github.com/mvcisback/dfa).\n\nFormally, the resulting `DFA` objects are quasi-reduced BDDs (QDDs)\nwhere the label of non-leaf states in the original BDD is `None` and\nall leaves self loop.\n\n\n<!-- markdown-toc start - Don\'t edit this section. Run M-x markdown-toc-generate-toc again -->\n**Table of Contents**\n\n- [Installation](#installation)\n- [Usage](#usage)\n\n<!-- markdown-toc end -->\n\n# Installation\n\nIf you just need to use `bdd2dfa`, you can just run:\n\n`$ pip install bdd2dfa`\n\nFor developers, note that this project uses the\n[poetry](https://poetry.eustace.io/) python package/dependency\nmanagement tool. Please familarize yourself with it and then\nrun:\n\n`$ poetry install`\n\n# Usage\n\n```python\n# Create BDD\n\nfrom dd import BDD\n\nmanager.declare(\'x\', \'y\', \'z\')\nx, y, z = map(manager.var, \'xyz\')\nbexpr = x & y & z\n\n\n# Convert to DFA\n\nfrom bdd2dfa import to_dfa\n\nqdd = to_dfa(bexpr)\n\nassert len(qdd.states()) == 7\n\nassert qdd.label([1, 1, 1, 1])      # QDD rejects.\nassert qdd dfa.label([0, 1, 1, 1])  # QDD accepts.\nassert qdd.label([1, 1]) is None    # Non-leaf node.\n```\n\nEach state of the resulting `DFA` object has three attribute:\n\n1. `time`: A number between #vars and 0. This number indicates the\n    number of decisions left to be made.\n2. `node`: A reference to the internal BDD node given by `dd`.\n3. `parity`: `dd` supports Edge Negated `BDD`s, where some edges point\n   to a Boolean function that is the negation of the Boolean function\n   the node would point to in a standard `BDD`. Parity value determines\n   whether or not the node \n\nFor example,\n```python\nassert qdd.start.parity is True\nassert qdd.start.time == 3\nassert qdd.start.node.var == \'x\'\n```\n\n## BDD vs QDD\n\n`to_dfa` also supports exporting a `BDD` rather than a `QDD`. This is done\nby toggling the `qdd` flag.\n\n```python\nbdd = to_dfa(bexpr, qdd=False)\n```\n\nThe `DFA` uses a similar state as the `QDD` case, but does not have a\ntime attribute.\n\nIf the `dfa` package was installed with the `draw` option, we can\nvisualize the difference between `qdd` and `bdd` by exporting to a\ngraphviz `dot` file.\n\n```python\nfrom dfa import write_dot\n\nwrite_dot(qdd, "qdd.dot")\nwrite_dot(bdd, "bdd.dot")\n```\n\nCompiling using the `dot` command yields the following for `qdd.dot`\n\n![qdd](assets/qdd.svg)\n\nand the following for `bdd.dot`:\n\n![bdd](assets/bdd.svg)\n',
    'author': 'Marcell Vazquez-Chanlatte',
    'author_email': 'mvc@linux.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mvcisback/bdd2dfa',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
