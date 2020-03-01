# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['goldenmask']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'cython>=0.29.14,<0.30.0']

entry_points = \
{'console_scripts': ['goldenmask = goldenmask.cli:goldenmask']}

setup_kwargs = {
    'name': 'goldenmask',
    'version': '0.2.0',
    'description': 'Protect your python source code with one command.',
    'long_description': '# Goldenmask: Protect your python source code\n\n[简体中文](README_zh_CN.md)\n\nGoldenmask is a tool to protect your python source code easily. It has two methods at the moment: using **Compileall** or using **Cython**. It has a corresponding option named `--layer/-l`, you can choose your favorite method by yourself. Meanwhile, it can protect different file types: python files end with `.py`, wheel packages end with `.whl ` and source package end with `.tar.gz`. \n\nGoldenmask is a name derived from a  Chinese kungfu named "JinZhongZhao". Because it is not a qualified phrase in a sense,  this name is so unique that can be used as a temporary compilation directory named `__goldenmask__` and a compilation information file named `.goldenmask` which contains the detailed python version string and the platform string.\n\nLet\'s try to goldenmask now!\n\n## Quick Start\n\n```bash\n$ pip install goldenmask\n# the default method is Compileall\n$ goldenmask yourpythonfile.py\n$ tree -a .\n.\n├── __goldenmask__\n│\xa0\xa0 ├── .goldenmask\n│\xa0\xa0 └── yourpythonfile.pyc\n└── yourpythonfile.py\n\n1 directory, 3 files\n# repalce your python file\n$ goldenmask -i yourpythonfile.py\n$ tree -a .\n.\n├── .goldenmask\n└── yourpythonfile.pyc\n\n0 directories, 2 files\n# protect python files under directory\n$ goldenmask yourpythonmoduledir\n# protect the wheel package\n$ goldenmask goldenmask-0.1.2-py3-none-any.whl\n# protect the source packege\n$ goldenmask goldenmask-0.1.2.tar.gz\n```\n\n## Installation\n\nGoldenmask is distributed on [PyPI]( https://pypi.org ) and supports Python 3.6+. You can simply install goldenmask as below:\n\n```bash\n$ pip install -U goldenmask\n```\n\nHowever, it\'s a better choice to use a virtual environment:\n\n```bash\n$ python -m venv env\n# On Windows:\n$ .\\venv\\Scripts\\activate\n# On Linux:\n$ source env/bin/activate\n$ pip install goldenmask --upgrade\n```\n\nBecause goldenmask depends on Cython, you should make sure that there is an appropriate C compiler on your machine. You can see the [detailed guide](https://cython.readthedocs.io/en/latest/src/quickstart/install.html) on Cython\'s documentation. By the way, if you works on a **Linux** system, you can easily fetch everything you need with one command `sudo apt-get install build-essential` on Ubuntu and `yum groupinstall "Development Tools"` on Centos. However, If you are using **Mac OS X** or **Windows**, you may spend quite some time installing this compilers.\n\n# Usage\n\nYou can get everything using [option]() `--help`:\n\n```\n$ goldenmask --help\nUsage: goldenmask [OPTIONS] [FILES_OR_DIRS]...\n\n  Goldenmask is a tool to protect your python source code easily.\n\n  FILES_OR_DIRS can be python files, wheel packages,source packages or dirs\n  contain python files.\n\nOptions:\n  -l, --layer <int>  Level of protection: 1 - compileall; 2 - cython.\n  -i, --inplace      Whether compile python files in place.\n  --no_smart         This will copy and compile everything you specified.\n  --help             Show this message and exit.\n```\n\n## Credits\n\nThe [blog](https://prodesire.cn/2019/01/06/%E5%A6%82%E4%BD%95%E5%8A%A0%E5%AF%86%E4%BD%A0%E7%9A%84-Python-%E4%BB%A3%E7%A0%81-%E2%80%94%E2%80%94-%E8%AE%B0-PyCon-China-2018-%E7%9A%84%E4%B8%80%E6%AC%A1%E5%88%86%E4%BA%AB/) from [Prodesire](https://github.com/prodesire).',
    'author': 'youngquan',
    'author_email': 'youngquan@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/youngquan/goldenmask',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
