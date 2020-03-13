# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['sportident']
install_requires = \
['pyserial', 'six']

setup_kwargs = {
    'name': 'sportident',
    'version': '1.2.6',
    'description': 'Python module to communicate with SportIdent main stations',
    'long_description': '# SportIdent Reader\n\n[![Build Status](https://api.travis-ci.org/sportorg/sireader.svg)](https://travis-ci.org/sportorg/sireader)\n\nsportIdent.py is a python module to communicate with a SportIdent main station to read out SportIdent cards. \nSportIdent is an electronic punching system mainly used for orienteering events.\n\n```python\nfrom time import sleep\nfrom sportident import SIReaderReadout\n\n# connect to base station, the station is automatically detected,\n# if this does not work, give the path to the port as an argument\n# see the pyserial documentation for further information.\nsi = SIReaderReadout()\n\n# wait for a card to be inserted into the reader\nwhile not si.poll_sicard():\n    sleep(1)\n\n# some properties are now set\ncard_number = si.sicard\ncard_type = si.cardtype\n\n# read out card data\ncard_data = si.read_sicard()\n\n# beep\nsi.ack_sicard()\n```',
    'author': 'Danil Akhtarov',
    'author_email': 'help@o-ural.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/sportident',
    'py_modules': modules,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
