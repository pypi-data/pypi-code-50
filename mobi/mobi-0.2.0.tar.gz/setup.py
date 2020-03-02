# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mobi']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['mobiunpack = mobi.kindleunpack:main']}

setup_kwargs = {
    'name': 'mobi',
    'version': '0.2.0',
    'description': 'unpack unencrypted mobi files',
    'long_description': '# mobi - library for unpacking unencrypted mobi files\n\n[![Version](https://img.shields.io/pypi/v/mobi.svg)](https://pypi.python.org/pypi/mobi/)\n[![Downloads](https://pepy.tech/badge/mobi)](https://pepy.tech/project/mobi)\n\n> A fork of [KindleUnpack](https://github.com/kevinhendricks/KindleUnpack) which removes the GUI part and makes it available as a python library via [PyPi](https://pypi.org/project/mobi/) for easy unpacking of mobi files.\n\n## Usage\n\n### As library\n\n```python\nimport mobi\n\ntempdir, epub_filepath = mobi.extract("mybook.mobi")\n```\n\n| NOTE: You are responsible to delete the generated tempdir! |\n| --- |\n\n### From the command line\n\nThe installer also creates a console script entrypoint that wraps the original KindleUnpack\n\n```console\n$ mobiunpack\nKindleUnpack v0.82\n   Based on initial mobipocket version Copyright © 2009 Charles M. Hannum <root@ihack.net>\n   Extensive Extensions and Improvements Copyright © 2009-2014\n       by:  P. Durrant, K. Hendricks, S. Siebert, fandrieu, DiapDealer, nickredding, tkeo.\n   This program is free software: you can redistribute it and/or modify\n   it under the terms of the GNU General Public License as published by\n   the Free Software Foundation, version 3.\n\nDescription:\n  Unpacks an unencrypted Kindle/MobiPocket ebook to html and images\n  or an unencrypted Kindle/Print Replica ebook to PDF and images\n  into the specified output folder.\nUsage:\n  mobiunpack -r -s -p apnxfile -d -h --epub_version= infile [outdir]\nOptions:\n    -h                 print this help message\n    -i                 use HD Images, if present, to overwrite reduced resolution images\n    -s                 split combination mobis into mobi7 and mobi8 ebooks\n    -p APNXFILE        path to an .apnx file associated with the azw3 input (optional)\n    --epub_version=    specify epub version to unpack to: 2, 3, A (for automatic) or\n                         F (force to fit to epub2 definitions), default is 2\n    -d                 dump headers and other info to output and extra files\n    -r                 write raw data to the output folder\n```\n\n### [0.2.0] - 2020-03-02\n\n- Minimal working \'extract\' function and \'mobiunpack\' console wrapper\n- Replace most print calls with logging\n\n### [0.1.0] - 2020-03-02\n\n- Empty package registered on pypi\n\n## License\n\nGPL-3.0-only\n\nAll credits for the hard work go to https://github.com/kevinhendricks/KindleUnpack\n',
    'author': 'Titusz Pan',
    'author_email': 'tp@py7.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github/iscc/mobi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
