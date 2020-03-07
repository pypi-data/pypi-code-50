# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cipher_tools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cipher-tools',
    'version': '0.0.3',
    'description': 'A python library to assist in the creation of ciphers',
    'long_description': '# Cipher Tools\nThis is a python library that contains some tools for making ciphers.\nIn was originaly made of use at a childrens workshop at PyCon UK 2019.\n\n[![pipeline status](https://gitlab.com/mokytis/cipher-tools/badges/master/pipeline.svg)](https://gitlab.com/mokytis/cipher-tools/commits/master)\n\n\n## Installation\nRun the following to install:\n```python\npip install cipher-tools\n```\n\n## Usage\n### Shift\nShift some text by an arbitrary amount. Text case is preserved.\n\nCode:\n```python\nfrom cipher_tools import shift\n\nshifted_text = shift("AbCdEfgYZ", 2)\nprint(shifted_text)\n```\nOutput:\n```\nCdEfGhiAB\n```\n### Rot13\nYou can encrypt / decrypt text using rot13.\n\nCode:\n```python\nfrom cipher_tools import rot13\n\n# Apply Rot13 to a phrase\ncipher_text = rot13("Hello, World!")\nprint(cipher_text)\n```\nOutput:\n```\nUryyb, Jbeyq!\n```\n\nCode:\n```python\nfrom cipher_tools import rot13\n\n# Decrtpt the text\nplain_text = rot13("Uryyb, Jbeyq!")\nprint(plain_text)\n```\nOutput:\n```\nHello, World!\n```\n\n\n',
    'author': 'Luke Spademan',
    'author_email': 'info@lukespademan.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/mokytis/cipher-tools',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
