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
    'version': '0.1.2',
    'description': 'calcul des couts de credit immobilier',
    'long_description': "# immo tools lib\n\n## installation\n\navec pip :\n````shell script\npip install immo-tools-lib\n````\n\navec poetry :\n````shell script\npoetry add immo-tools-lib\n````\n\n## usage\n\n````python\nfrom immo_tools import calculator\n\nduration = 300\namount = 250000\nyear_rate = 1.5\ninsurance_rate = .26\n\nloan = calculator.build_loan(\n    duration, \n    amount, \n    year_rate, \n    insurance_rate, \n    build_summary=True, \n    duration_unit='month')\n\n# Tableau d'amoritssement :\nloan.summary\n\n# montant total des intérêts payés :\nloan.get_interests()\n\n# mensualités sans assurance :\nloan.get_monthly()\n\n# Coût de l'emprunt au bout de 10 ans :\nloan.get_cost(10)\n````\n\n## développement\n\n### tests\n\nlancer les tests :\n\n````shell script\npytest\n````\n\navec le coverage :\n\n````shell script\npytest --cov\n````\n\nlancer les tests avec nox : (attention, c'est super long !):\n\n````shell scripts\nnox -r\n````\n\nPermet de lancer les tests sur plusieurs versions de python et de manière isollée.\nNox crée son propre environnement virtuel et y install les dépendances.\nL'option ``-r`` permet déviter de recréer tout l'environnement virtuel à chaque fois.\n\n### build & publish\n\nbuild :\n\n````shell script\npoetry build\n````\n\n\npublish sur pypi :\n\n````shell script\npoetry publish --build\n````\n\n",
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
