# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['keras_fsl',
 'keras_fsl.callbacks',
 'keras_fsl.dataframe',
 'keras_fsl.dataframe.flows',
 'keras_fsl.dataframe.operators',
 'keras_fsl.datasets',
 'keras_fsl.imgaug.sequentials',
 'keras_fsl.losses',
 'keras_fsl.models',
 'keras_fsl.models.branch_models',
 'keras_fsl.models.head_models',
 'keras_fsl.models.layers',
 'keras_fsl.sequences',
 'keras_fsl.sequences.prediction',
 'keras_fsl.sequences.prediction.pairs',
 'keras_fsl.sequences.prediction.single',
 'keras_fsl.sequences.training',
 'keras_fsl.sequences.training.pairs',
 'keras_fsl.sequences.training.single']

package_data = \
{'': ['*']}

install_requires = \
['imgaug>=0.4.0,<0.5.0',
 'numpy>=1.18.1,<2.0.0',
 'pandas>=1.0.1,<2.0.0',
 'pyyaml>=5.3,<6.0',
 'tensorflow>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'keras-fsl',
    'version': '0.1.0',
    'description': 'Model builder for some State-of-the-Art architecture in few-shot learning',
    'long_description': None,
    'author': 'Clément Walter',
    'author_email': 'clement0walter@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.5,<4.0.0',
}


setup(**setup_kwargs)
