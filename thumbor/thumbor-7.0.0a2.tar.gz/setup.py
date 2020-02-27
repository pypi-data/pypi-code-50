# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thumbor',
 'thumbor.detectors',
 'thumbor.detectors.face_detector',
 'thumbor.detectors.feature_detector',
 'thumbor.detectors.glasses_detector',
 'thumbor.detectors.profile_detector',
 'thumbor.detectors.queued_detector',
 'thumbor.detectors.queued_sqs_detector',
 'thumbor.engines',
 'thumbor.engines.extensions',
 'thumbor.error_handlers',
 'thumbor.ext',
 'thumbor.ext.filters',
 'thumbor.filters',
 'thumbor.handler_lists',
 'thumbor.handlers',
 'thumbor.lib',
 'thumbor.loaders',
 'thumbor.metrics',
 'thumbor.optimizers',
 'thumbor.result_storages',
 'thumbor.storages',
 'thumbor.url_signers']

package_data = \
{'': ['*'], 'thumbor': ['fixtures/filters/*'], 'thumbor.ext.filters': ['lib/*']}

install_requires = \
['Pillow>=7.0.0,<8.0.0',
 'derpconf>=0.8.3,<0.9.0',
 'libthumbor>=1.3.2,<2.0.0',
 'opencv-python-headless>=4.2.0,<5.0.0',
 'pytz>=2019.3,<2020.0',
 'statsd>=3.3.0,<4.0.0',
 'tornado>=6.0.3,<7.0.0',
 'webcolors>=1.10,<2.0']

entry_points = \
{'console_scripts': ['thumbor = thumbor.server:main',
                     'thumbor-config = thumbor.config:generate_config',
                     'thumbor-url = thumbor.url_composer:main']}

setup_kwargs = {
    'name': 'thumbor',
    'version': '7.0.0a2',
    'description': 'thumbor is an open-source photo thumbnail service by globo.com',
    'long_description': None,
    'author': 'globo.com',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
