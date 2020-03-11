# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['immo_tools']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.1,<2.0.0', 'pandas>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'immo-tools-lib',
    'version': '0.1.0',
    'description': 'calcul des couts de credit immobilier',
    'long_description': "# immo-tools\n\nlancer les tests :\n\n````shell script\npytest\n````\n\navec le coverage :\n\n````shell script\npytest --cov\n````\n\nlancer les tests avec nox : (attention, c'est super long !):\n\n````shell scripts\nnox -r\n````\n\nPermet de lancer les tests sur plusieurs versions de python et de manière isollée.\nNox crée son propre environnement virtuel et y install les dépendances.\nL'option ``-r`` permet déviter de recréer tout l'environnement virtuel à chaque fois.\n\n## build\n\nune seule commande :\n\n````shell script\npoetry build\n````\n\n",
    'author': 'thomas.marquis.dev',
    'author_email': 'thomas.marquis314@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thomas-marquis/immo-tools-lib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
