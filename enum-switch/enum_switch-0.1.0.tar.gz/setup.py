# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['enum_switch']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'enum-switch',
    'version': '0.1.0',
    'description': 'An Enum-based implementation of switch for Python.',
    'long_description': '# Enum-based Switch for Python\n\nThis is an attempt at creating a way to do a reliable, not-bug-prone \nimplementation, for Python, of a `switch` thing like other languages \nhave.\n\n## How it works\n\nSuppose you have an enum, like this:\n\n```\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n```\n\nAnd you want to implement logic which branches based on a value which is of type `Color`.\nYou can do it by subclassing the `Switch` class. The syntax should be obvious, but:\n\n* Inherit from Switch\n* Implement a method for each value of the Enum\n* If you are not implementing them all: add a `default` method.\n* If you leave any Enum value unaccounted for: it will raise an exception when you\n  instantiate your class.\n\nThen:\n\n* Instantiate your class\n* Call it as a function passing it a value from the Enum\n* The respective method will be executed and its return value returned\n\n```\nfrom enum_switch import Switch\n\nclass MySwitch(Switch):\n    def RED(self):\n        return "Apple"\n\n    def GREEN(self):\n        return "Kiwi"\n\n    def BLUE(self):\n        return "Sky"\n\nswitch = MySwitch()\n\nprint(switch(Color.RED))\n\nApple\n```\n\nAnd that\'s it.\n\nSome additional notes:\n\n* Passing it something that is not a value of the correct Enum type will raise ValueError\n* `default` is optional\n\nHope someone finds it useful!\n',
    'author': 'Roberto Alsina',
    'author_email': 'roberto.alsina@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ralsina/enum_switch',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.4',
}


setup(**setup_kwargs)
