# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['csvy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'csvy',
    'version': '0.1.3a0',
    'description': '',
    'long_description': 'csvy\n----\n\nBasic context wrappers for stardard library csv.read and csv.write methods.\n\nWriter example:\n\n    import csvy\n\n    with csvy.writer(\'csvpath.csv\') as csvfile:\n        csvfile.writerow([1, 2, 3, 4])\n\n\nReader example:\n\n    import csvy\n\n    with csvy.reader(\'csvpath.csv\') as csvfile:\n        for index, row in csvfile.iter():\n            print(f"{index}: {row}")\n',
    'author': 'Mark Gemmill',
    'author_email': 'gitlab@markgemmill.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/mgemmill-pypi/csvy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
