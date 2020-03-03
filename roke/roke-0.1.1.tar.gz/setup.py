# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roke']

package_data = \
{'': ['*'], 'roke': ['data/*']}

install_requires = \
['click>=7,<8']

entry_points = \
{'console_scripts': ['roke = roke:main']}

setup_kwargs = {
    'name': 'roke',
    'version': '0.1.1',
    'description': 'A library to name and identify things',
    'long_description': '# Roke\n\nRoke is a tool and a library to create identifiers. The goal is that these\nidentifiers should be:\n\n* More or less unique.\n* Easy to read, so you can read it to someone else over a phone, for example.\n* Configurable: not a single format in how they look\n* Customizable: it should be easy to do things like "make it work in spanish"\n\nTo do this, inspired by a talk about [Magic Wormhole](https://github.com/warner/magic-wormhole) ... \nI did pretty much the same thing they did.\n\n## Command Line Tool\n\nBy default, Roke will give you identifiers made out of two nouns and a small number. Like this:\n\n```\n$ roke\n19-hassock-disregard\n```\n\nYou can tell roke to print more than one identifier, so you can choose a nice one.\n\n```\n$ roke --count 5\n9-vibrissae-truth\n4-bathrobe-somewhere\n10-dysfunction-overview\n19-aardvark-viola\n5-mutt-pamphlet\n```\n\nYou can change the format of the identifiers:\n\n```\n$ roke --count 5 --format \'{noun}+{noun}\'\nplate+pasture\npickle+syrup\ncolloquy+bracelet\nprisoner+businessman\nmembrane+approach\n```\n\nRoke comes with two basic dictionaries:\n\n* "noun" which is a list of english nouns taken from http://www.desiquintans.com/nounlist\n* "smallnum" which is the numbers from 1 to 20\n\nYou can add more dictionaries by putting files with the ".txt" extension and one \nword per line in any of the following places:\n\n```\n~/.local/roke\n.roke\n```\n\n## Python Library\n\nYou can use Roke inside your own projects by using it as a library. This example \nshows how:\n\n```\n>>> import roke\n>>> roke.load_dicts()\n>>> roke.gen_identifier(\'{noun}-{smallnum}\')\n\'village-18\'\n```\n\nThat\'s all there is to it.\n\n## Technical Notes\n\nSo, how unique are the identifiers?\n\nIf you use the default format `{smallnum}-{noun}-{noun}` there are only \n925 072 020 possible identifiers. So: NOT VERY UNIQUE.\n\n**Do not use this as a password or a secret!** ... at least not using that format.\n\nThey should be unique **enough** for situations where you just need something \nto be "unique for a while" in a certain environment. Like, container names, \nor maybe your children.\n\nMandatory XKCD:\n\n![XKCD](https://imgs.xkcd.com/comics/password_strength.png)\n\n[Full Comic](https://xkcd.com/936/)\n\n## Why the name?\n\nRoke is the name of an island in Earthsea. To know more about Roke and names,\njust read the Earthsea books by Ursula K LeGuin, they are awesome.',
    'author': 'Roberto Alsina',
    'author_email': 'roberto.alsina@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ralsina/roke',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
