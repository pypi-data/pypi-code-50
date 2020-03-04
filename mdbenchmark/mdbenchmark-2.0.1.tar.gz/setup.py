# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mdbenchmark',
 'mdbenchmark.cli',
 'mdbenchmark.ext',
 'mdbenchmark.mdengines',
 'mdbenchmark.migrations',
 'mdbenchmark.tests',
 'mdbenchmark.tests.mdengines',
 'mdbenchmark.tests.migrations']

package_data = \
{'': ['*'],
 'mdbenchmark': ['templates/*'],
 'mdbenchmark.tests': ['data/*',
                       'data/analyze-files-gromacs-one-unstarted/1/*',
                       'data/analyze-files-gromacs-one-unstarted/1/.datreant/*',
                       'data/analyze-files-gromacs-one-unstarted/2/*',
                       'data/analyze-files-gromacs-one-unstarted/2/.datreant/*',
                       'data/analyze-files-gromacs-one-unstarted/3/*',
                       'data/analyze-files-gromacs-one-unstarted/3/.datreant/*',
                       'data/analyze-files-gromacs-one-unstarted/4/*',
                       'data/analyze-files-gromacs-one-unstarted/4/.datreant/*',
                       'data/analyze-files-gromacs-one-unstarted/5/*',
                       'data/analyze-files-gromacs-one-unstarted/5/.datreant/*',
                       'data/analyze-files-gromacs/1/*',
                       'data/analyze-files-gromacs/1/.datreant/*',
                       'data/analyze-files-gromacs/2/*',
                       'data/analyze-files-gromacs/2/.datreant/*',
                       'data/analyze-files-gromacs/3/*',
                       'data/analyze-files-gromacs/3/.datreant/*',
                       'data/analyze-files-gromacs/4/*',
                       'data/analyze-files-gromacs/4/.datreant/*',
                       'data/analyze-files-gromacs/5/*',
                       'data/analyze-files-gromacs/5/.datreant/*',
                       'data/analyze-files-namd/1/*',
                       'data/analyze-files-namd/1/.datreant/*',
                       'data/analyze-files-namd/2/*',
                       'data/analyze-files-namd/2/.datreant/*',
                       'data/analyze-files-w-errors/1/*',
                       'data/analyze-files-w-errors/1/.datreant/*',
                       'data/analyze-files-w-errors/2/*',
                       'data/analyze-files-w-errors/2/.datreant/*',
                       'data/analyze-files-w-errors/3/*',
                       'data/analyze-files-w-errors/3/.datreant/*',
                       'data/analyze-files-w-errors/4/*',
                       'data/analyze-files-w-errors/4/.datreant/*',
                       'data/analyze-files-w-errors/5/*',
                       'data/analyze-files-w-errors/5/.datreant/*',
                       'data/analyze-files-w-errors/6/.datreant/*',
                       'data/analyze-files-w-errors/7/*',
                       'data/analyze-files-w-errors/7/.datreant/*',
                       'data/analyze-files-w-errors/8/*',
                       'data/analyze-files-w-errors/8/.datreant/*']}

install_requires = \
['click>=6.7',
 'datreant>=1.0,<2.0',
 'jinja2>=2.10,<3.0',
 'matplotlib>=2',
 'numpy>=1.15',
 'pandas>=0.24',
 'python-levenshtein>=0.12.0,<0.13.0',
 'tabulate>=0.8.5,<0.9.0',
 'xdg>=1,<2']

extras_require = \
{'docs': ['Sphinx>=1,<2',
          'sphinx-autobuild>=0.7.1,<0.8.0',
          'sphinx-click>=2.3,<3.0']}

entry_points = \
{'console_scripts': ['mdbenchmark = mdbenchmark:cli']}

setup_kwargs = {
    'name': 'mdbenchmark',
    'version': '2.0.1',
    'description': 'Quickly generate, start and analyze benchmarks for your molecular dynamics simulations.',
    'long_description': '============================================\n  Benchmark molecular dynamics simulations\n============================================\n\n.. image:: https://img.shields.io/pypi/v/mdbenchmark.svg\n    :target: https://pypi.python.org/pypi/mdbenchmark\n\n.. image:: https://anaconda.org/conda-forge/mdbenchmark/badges/version.svg\n    :target: https://anaconda.org/conda-forge/mdbenchmark\n\n.. image:: https://img.shields.io/pypi/l/mdbenchmark.svg\n    :target: https://pypi.python.org/pypi/mdbenchmark\n\n.. image:: https://travis-ci.org/bio-phys/MDBenchmark.svg?branch=develop\n    :target: https://travis-ci.org/bio-phys/MDBenchmark\n\n.. image:: https://readthedocs.org/projects/mdbenchmark/badge/?version=latest&style=flat\n    :target: https://mdbenchmark.readthedocs.io/en/latest/\n\n.. image:: https://codecov.io/gh/bio-phys/MDBenchmark/branch/develop/graph/badge.svg\n    :target: https://codecov.io/gh/bio-phys/MDBenchmark\n\n.. image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square\n    :target: http://makeapullrequest.com\n\n.. image:: https://zenodo.org/badge/112506401.svg\n    :target: https://zenodo.org/badge/latestdoi/112506401\n\n---------------\n\n**MDBenchmark** — quickly generate, start and analyze benchmarks for your molecular dynamics simulations.\n\nMDBenchmark is a tool to squeeze the maximum out of your limited computing\nresources. It tries to make it as easy as possible to set up systems on varying\nnumbers of nodes and compare their performances to each other.\n\nYou can also create a plot to get a quick overview of the possible performance\n(and also show of to your friends)! The plot below shows the performance of a\nmolecular dynamics system on up to five nodes with and without GPUs.\n\n.. image:: https://raw.githubusercontent.com/bio-phys/MDBenchmark/master/docs/_static/runtimes.png\n\n\nInstallation\n============\n\nYou can install ``mdbenchmark`` via ``pip``, ``conda`` or ``pipenv``:\n\npip\n---\n\n.. code::\n\n   pip install mdbenchmark\n\nconda\n-----\n\n.. code::\n\n   conda install -c conda-forge mdbenchmark\n\npipenv\n------\n\n.. code::\n\n   pipenv install mdbenchmark\n\nAfter installation MDBenchmark is accessible on your command-line via ``mdbenchmark``::\n\n    $ mdbenchmark\n    Usage: mdbenchmark [OPTIONS] COMMAND [ARGS]...\n\n    Generate, run and analyze benchmarks of molecular dynamics simulations.\n\n    Options:\n    --version  Show the version and exit.\n    --help     Show this message and exit.\n\n    Commands:\n    analyze   Analyze benchmarks and print the performance...\n    generate  Generate benchmarks for molecular dynamics...\n    plot      Generate plots showing the benchmark...\n    submit    Submit benchmarks to queuing system.\n\nFeatures\n========\n\n- Generates benchmarks for GROMACS and NAMD simulations (contributions for other MD engines are welcome!).\n- Automatically detects the queuing system on your high-performance cluster and submits jobs accordingly.\n- Grabs performance from the output logs and creates a fancy plot.\n- Benchmarks systems on CPUs and/or GPUs.\n\nShort usage reference\n=====================\n\nThe following shows a short usage reference for MDBenchmark. Please consult the\n`documentation`_ for a complete guide.\n\nBenchmark generation\n--------------------\n\nAssuming you want to benchmark GROMACS version 2018.3 and your TPR file is\ncalled ``protein.tpr``, run the following command::\n\n  mdbenchmark generate --name protein --module gromacs/2018.3\n\nTo run benchmarks on GPUs simply add the ``--gpu`` flag::\n\n  mdbenchmark generate --name protein --module gromacs/2018.3 --gpu\n\nBenchmark submission\n--------------------\n\nAfter you generated your benchmarks, you can submit them at once::\n\n  mdbenchmark submit\n\nBenchmark analysis\n------------------\n\nAs soon as the benchmarks have been submitted you can run the analysis via\n``mdbenchmark analyze``. Systems that have not finished yet will be marked with a question mark (``?``). You can save the performance results to a CSV file and subsequently create a plot from the data::\n\n    # Print performance results to console and save them to a file called results.csv \n    mdbenchmark analyze --save-csv results.csv\n    \n    # Create a plot from the results present in the file results.csv\n    mdbenchmark plot --csv results.csv\n\nContributing\n============\n\nContributions to the project are welcome! Information on how to contribute to\nthe project can be found in `CONTRIBUTING.md`_ and `DEVELOPER.rst`_.\n\n.. _documentation: https://mdbenchmark.readthedocs.io/en/latest/\n.. _CONTRIBUTING.md: https://github.com/bio-phys/MDBenchmark/blob/master/.github/CONTRIBUTING.md\n.. _DEVELOPER.rst: https://github.com/bio-phys/MDBenchmark/blob/master/DEVELOPER.rst\n',
    'author': 'Max Linke',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mdbenchmark.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
