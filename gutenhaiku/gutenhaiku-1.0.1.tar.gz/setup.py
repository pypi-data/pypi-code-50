# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gutenhaiku', 'gutenhaiku.models']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.1,<8.0.0',
 'colorama>=0.4.3,<0.5.0',
 'deepcorrect>=1.0.5,<2.0.0',
 'numpy==1.16.4',
 'setuptools>=41.0.0',
 'silence_tensorflow>=1.1.1,<2.0.0',
 'spacy>=2.2.4,<3.0.0',
 'spacy_syllables>=1.0.0,<2.0.0',
 'tensorboard==1.14.0',
 'tensorflow==1.14.0']

entry_points = \
{'console_scripts': ['gutenhaiku = gutenhaiku.app:cli']}

setup_kwargs = {
    'name': 'gutenhaiku',
    'version': '1.0.1',
    'description': 'A Commandline tool to mine haiku poems from text',
    'long_description': '<img src="https://github.com/sloev/gutenhaiku/raw/master/assets/header.png" width="400"/>\n\n# Guten Haiku\n\n[![Build Status](https://travis-ci.org/sloev/gutenhaiku.svg?branch=master)](https://travis-ci.org/sloev/gutenhaiku) [![Latest Version](https://img.shields.io/pypi/v/gutenhaiku.svg)](https://pypi.python.org/pypi/gutenhaiku) [![Python Support](https://img.shields.io/pypi/pyversions/gutenhaiku.svg)](https://pypi.python.org/pypi/gutenhaiku)\n\nA Commandline tool to mine haiku poems from text\n\n* 80\'s cli interface with **colors**\n* Works great with gutenberg books thx to a builtin cleaner script from [Peyman Mohseni Kiasari](https://github.com/kiasar/gutenberg_cleaner)\n* Reconstructs punctuation of haikus using [deepcorrect](https://github.com/bedapudi6788/deepcorrect)\n* Appends json haiku\'s to a file\n\n## Install\n\n```bash\n$ pip install gutenhaiku\n```\n\nThen you need to download the models in cache:\n\n```bash\n$ gutenhaiku setup\n```\n\n## Usage\n\n```bash\n$ gutenhaiku -f frankenstein.txt -a \'mary shelley\' -t \'frankenstein\' -d \'1818-01-01\'\n```\n\n<a target="_blank" href="https://asciinema.org/a/9dSu3L5D7OzaOg1p5lOXNF8TC"><img src="https://github.com/sloev/gutenhaiku/raw/master/assets/gutenhaiku.gif" width="600"/></a>\n\n```bash\nWat?             Guten Haiko lets you extract haiku poems from text\nUsage:           gutenhaiku \\\n                 -f frankenstein.txt \\\n                 -a \'Mary Wollstonecraft Shelley\' \\\n                 -t \'frankenstein\' \\\n                 -d \'1818-01-01\'\nOptional params: --commandfile [-cf] a file with comma seperated \n                                     values for f,a,t,d params\n                 --outputfile   [-o] the output file path [default haiku.json\n                 --eighties     [-e] eighties mode [default 1]\n\nAdvanced usage:  gutenhaiku \\\n                 -f frankenstein.txt \\\n                 -a \'Mary Wollstonecraft Shelley\' \\\n                 -t \'frankenstein\' \\\n                 -d \'1818-01-01\' \\\n                 -f dracula.txt \\\n                 -a \'Bram Stoker\' \\\n                 -t \'dracula\' \\\n                 -d \'1897-05-26\'\n\nsetup:           gutenhaiku setup\n                 downloads AI models\n\n```\n\n### Output format\n\n*example from [assets](assets/frankenstein_haiku.json)*\n```json\n{\n    "page": 261,\n    "word_number": 65407,\n    "haiku": [\n        "He pointed towards.",\n        "The corpse of my wife I rushed.",\n        "Towards the window."\n    ],\n    "author": "mary shelley",\n    "title": "frankenstein",\n    "date": "1818-01-01T00:00:00"\n}\n```\n\n## Dev\n\nRun tests with \n\n```bash\n$ poetry run nox\n```\n',
    'author': 'sloev',
    'author_email': 'johannes.valbjorn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sloev/gutenhaiku',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
