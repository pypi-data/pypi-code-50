# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fakeit',
 'fakeit.advanced',
 'fakeit.advanced.person',
 'fakeit.basics',
 'fakeit.basics.boolean',
 'fakeit.basics.bytes',
 'fakeit.basics.geo',
 'fakeit.basics.hashes',
 'fakeit.basics.ip',
 'fakeit.basics.numerics',
 'fakeit.basics.personal',
 'fakeit.basics.strings',
 'fakeit.basics.texts',
 'fakeit.basics.uuids',
 'fakeit.constance',
 'fakeit.constance.email',
 'fakeit.constance.tld',
 'fakeit.extras',
 'fakeit.extras.alchemy',
 'fakeit.extras.django']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fakeit',
    'version': '0.1.8',
    'description': 'Generate fake data',
    'long_description': '# Meet the FAKE IT project which provide generating simple fake data\n\n-----\n\n## INSTALL:\n- python setup.py install\n- pip install fakeit\n- pip install git+https://github.com/RCheese/fakeit\n\n## USAGE:\nGenerating fake data for python types\n\n### Bytes\n```python\n    >>> from fakeit import bytes\n    >>> bytes.fake_bytes(min_length=2, max_length=5)\n    ... b\'/\\xf5Q\\x9a\\xcd\'\n    \n    >>> bytes.fake_b64(min_length=2, max_length=5)\n    ... b\'QpwJug==\'\n```\n\n### Hashes\n```python\n    >>> from fakeit import hashes\n    >>> hashes.fake_md5()\n    ... \'37c6c63ee4dd8516d3d8ee4319b3e7b8\'\n    >>> hashes.fake_sha256()\n    ... \'bc6c64d150e869cf10e3d9c0cf582fa78fe46282de75911b464c46a023a08038\'\n```\n\n### Numerics\n```python\n    >>> from fakeit import numerics\n    >>> numerics.fake_complex(1,2,3,4)\n    ... (1.2157335093960198+3.17909803327301j)\n    >>> numerics.fake_complex(1,2,3,4, round=True)\n    ... (2+4j)\n    >>> numerics.fake_int(1 ,20)\n    ... 11\n    >>> numerics.fake_float(1, 20)\n    ... 3.448023122876366\n```\n\n### Strings\n```python\n    >>> from fakeit import strings\n    >>> strings.fake_string(min_length=5, max_length=5)\n    ... \'CPOcO\'\n    \n    >>> fake_string(min_length=5, max_length=5, unique=True)\n    ... \'qEiwW\'\n    \n    >>> fake_string(min_length=5, max_length=5, alphabet="ABCdE")\n    ... \'EdBdB\'\n    \n    >>> fake_strings(5)\n    ... <generator object fake_strings at 0x7f67579e4660>\n    \n    >>> for i in fake_strings(5):\n    >>>     print(i)\n    >>>\n    ... 1r3OxTKis20KF\n    ... \n    ... 3YN28kOPLuc\n    ... DaLQ\n    ... j7J9MMJcF2\n    \n    >>> for i in all_combinations_with_replacement_fake_string(min_length=3, max_length=3, alphabet="abc"):\n    >>>     print(i)\n    ... aaa\n    ... aab\n    ... aac\n    ... abb\n    ... abc\n    ... acc\n    ... bbb\n    ... bbc\n    ... bcc\n    ... ccc\n```\n\n### Personal\n``\n```python\n    >>> from fakeit import personal\n    >>> personal.names.fake_fullname()\n    ... \'Justin Hall\'\n    >>> personal.names.fake_name()\n    ... \'Johnny\'\n    >>> personal.names.fake_surname()\n    ... \'Gill\'\n    \n    >>> personal.phones.fake_international()\n    ... \'+67-910-8211582\'\n    >>> personal.phones.fake_international(mediator="")\n    ... \'+974665503991\'\n    >>> fake_international(country_code=7, area_code=923)\n    ... \'+7-923-4915850\'\n    \n    >>> personal.emails.fake_email()\n    ... \'0mfJz0QD@VqujvpRDiuMfuyB.VRQfn\'\n    >>> personal.emails.fake_enough_email()\n    ... \'Henry.Hill@google.cn\'\n    \n    >>> personal.fake_person()\n    ... <Person Stephen Robertson> (FirstName=Stephen, LastName=Robertson, Email=Stephen.Robertson@whatsapp.net, Phone=+1-990-5674435)\n```\n\n## TODO:\n\n- Geo\n    - Position\n    - Named (Country, City, and etc.)\n    - Address\n- Text data\n- Tables\n    - ?\n- Unit tests\n- SQLAlchemy type casting\n- Django type casting\n- Sphinx docs\n- CI\n- Compilation request\n\n<a href="https://www.buymeacoffee.com/RussianCheese" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/arial-violet.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>\n',
    'author': 'Ruslan Samoylov',
    'author_email': 'ruslan.v.samoylov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
