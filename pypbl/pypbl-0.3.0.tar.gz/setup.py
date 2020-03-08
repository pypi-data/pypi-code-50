# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pypbl']

package_data = \
{'': ['*']}

install_requires = \
['dunamai>=1.0.0,<2.0.0',
 'emcee>=3.0.2,<4.0.0',
 'numpy>=1.18.0,<2.0.0',
 'pandas>=0.25.3,<0.26.0',
 'scipy>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'pypbl',
    'version': '0.3.0',
    'description': 'A python library for preference based learning using pairwise comparisons.',
    'long_description': '# pypbl\n\n[![Actions Status](https://github.com/jimparr19/pypbl/workflows/pythonpackage/badge.svg)](https://github.com/jimparr19/pypbl/actions)\n[![Documentation Status](https://readthedocs.org/projects/pypbl/badge/?version=latest)](https://pypbl.readthedocs.io/en/latest/?badge=latest)\n[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jimparr19/pypbl/master?filepath=binder%2Fpypbl.ipynb)\n\nA python library for preference based learning using pairwise comparisons.\n\nWe want to recommend a personalised list of items to an individual. \n\nThere are three approaches we could take:\n\n1. Ask the individual to manually rank all items.\n2. Ask the individual to provide weights based on their preferences of different features (size, cost, weight etc), and calculate the weighted value of each item.\n3. Find similar people and base recommendations on what these people also like.\n3. Ask the individual compare a small number of alternatives, and derive feature weights from those comparisons.\n\nOption 1 quickly becomes an enormous burden on the user as the number of items increases. \n\nOption 2 is difficult for the user to do and replicate. What exactly does it mean if the weight assigned to one feature is double the weight assigned to another?\n\nOption 3 requires lots of data, a way to determine similarity between individuals and may not be fully personalised.\n\nOption 4 is enabled by preference based learning using pairwise comparisons.\n\n### Installing\n\n```\npip install pypbl\n```\n\n## Development\n\nDependencies and packaging are managed using [Poetry](https://github.com/python-poetry/poetry). \n\nInstall poetry and clone the repository\n\n\nTo create a virtual environment and install dependencies\n```\npoetry install\n```\n\nTo run tests\n```\npoetry run pytest --cov=src --cov-branch --cov-fail-under=90 tests/\n```\n\nTo run linting\n```\npoetry run flake8 src/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics\n```\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details\n\n## Acknowledgments\n\n* Early versions of this package is heavily based on the [PrefeR](https://cran.r-project.org/web/packages/prefeR/index.html) library by John Lepird. \n* [PreferenceElicitation.jl](https://github.com/sisl/PreferenceElicitation.jl) by Mykel Kochenderfer.\n* [Interactive Bayesian Optimisation](https://github.com/misterwindupbird/IBO) by Eric Brochu.\n\n\n## TODO\n* Improve suggestion engine as using entropy is expensive and required a hammer to compute accurately \n* Include [dynasty](https://github.com/joshspeagle/dynesty) sampling algorithm and [PyMC3](https://docs.pymc.io/) or perhaps [pyMC4](https://github.com/pymc-devs/pymc4)\n* Include preference elicitation using Gaussian Processes see [gp_pref_elicit](https://github.com/lmzintgraf/gp_pref_elicit)\n',
    'author': 'Jim Parr',
    'author_email': 'jimparr19@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypbl.readthedocs.io/en/latest/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
