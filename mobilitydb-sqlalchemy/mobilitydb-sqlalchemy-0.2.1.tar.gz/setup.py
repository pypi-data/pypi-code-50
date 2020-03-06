# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mobilitydb_sqlalchemy', 'mobilitydb_sqlalchemy.types']

package_data = \
{'': ['*']}

install_requires = \
['geoalchemy2>=0.6.3,<0.7.0',
 'pandas>=0.25.3,<0.26.0',
 'shapely>=1.6.4,<2.0.0',
 'sqlalchemy>=1.3.11,<2.0.0']

extras_require = \
{'docs': ['sphinx>=2.3.1,<3.0.0',
          'sphinx-rtd-theme>=0.4.3,<0.5.0',
          'tomlkit>=0.5.8,<0.6.0'],
 'movingpandas': ['movingpandas>=0.1.dev2,<0.2']}

setup_kwargs = {
    'name': 'mobilitydb-sqlalchemy',
    'version': '0.2.1',
    'description': 'MobilityDB extensions to SQLAlchemy',
    'long_description': '.. image:: https://github.com/adonmo/mobilitydb-sqlalchemy/workflows/Tests/badge.svg\n   :target: https://github.com/adonmo/mobilitydb-sqlalchemy/actions\n   :alt: Test Status\n\n.. image:: https://readthedocs.org/projects/mobilitydb-sqlalchemy/badge/?version=latest\n   :target: https://mobilitydb-sqlalchemy.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation Status\n\n.. image:: https://img.shields.io/pypi/dm/mobilitydb-sqlalchemy.svg\n   :target: https://pypistats.org/packages/mobilitydb-sqlalchemy\n   :alt: PyPI downloads\n\n.. image:: https://img.shields.io/github/license/adonmo/mobilitydb-sqlalchemy.svg\n   :target: https://github.com/adonmo/mobilitydb-sqlalchemy/blob/master/LICENSE.txt\n   :alt: MIT License\n\nMobilityDB SQLAlchemy\n=====================\n\nThis package provides extensions to `SQLAlchemy <http://sqlalchemy.org/>`_ for interacting with `MobilityDB <https://github.com/ULB-CoDE-WIT/MobilityDB>`_. The data retrieved from the database is directly mapped to time-indexed pandas DataFrame objects. TGeomPoint and TGeogPoint objects can be optionally mapped to movingpandas\' Trajectory data structure.\n\nThanks to the amazing work by `MobilityDB <https://github.com/ULB-CoDE-WIT/MobilityDB>`_ and `movingpandas <https://github.com/anitagraser/movingpandas>`_ teams, because of which this project exists.\n\nA demo webapp built using this library is now available online:\n\n**Live Demo**: https://mobilitydb-sqlalchemy-demo.adonmo.com\n\n**Source Code**: https://github.com/adonmo/mobilitydb-sqlalchemy-demo\n\nInstallation\n============\n\nThe package is available on `PyPI <https://pypi.org/project/mobilitydb-sqlalchemy>`_\\ , for Python >= 3.7\n\n.. code-block:: sh\n\n    pip install mobilitydb-sqlalchemy\n\nUsage\n=====\n\n.. code-block:: py\n\n    from mobilitydb_sqlalchemy import TGeomPoint\n\n    from sqlalchemy import Column, Integer\n    from sqlalchemy.ext.declarative import declarative_base\n    Base = declarative_base()\n\n    class Trips(Base):\n        __tablename__ = "test_table_trips_01"\n        car_id = Column(Integer, primary_key=True)\n        trip_id = Column(Integer, primary_key=True)\n        trip = Column(TGeomPoint)\n\n    trips = session.query(Trips).all()\n\n    # Querying using MobilityDB functions, for example - valueAtTimestamp\n    session.query(\n        Trips.car_id,\n        func.asText(\n            func.valueAtTimestamp(Trips.trip, datetime.datetime(2012, 1, 1, 8, 10, 0))\n        ),\n    ).all()\n\nThere is also a `tutorial <https://anitagraser.com/2020/03/02/movement-data-in-gis-29-power-your-web-apps-with-movement-data-using-mobilitydb-sqlalchemy/>`_ published on Anita Graser\'s blog.\n\nFor more details, read our `documentation <https://mobilitydb-sqlalchemy.readthedocs.io/en/latest/>`_ (specifically, the `quickstart <https://mobilitydb-sqlalchemy.readthedocs.io/en/latest/quickstart.html>`_).\n\nContributing\n============\n\nIssues and pull requests are welcome.\n\n* For proposing new features/improvements or reporting bugs, `create an issue <https://github.com/adonmo/mobilitydb-sqlalchemy/issues/new/choose>`_.\n* Check `open issues <https://github.com/adonmo/mobilitydb-sqlalchemy/issues>`_ for viewing existing ideas, verify if it is already proposed/being worked upon.\n* When implementing new features make sure to add relavant tests and documentation before sending pull requests.\n\nSetup environment\n-----------------\n\nFirst, make sure you have `poetry installed <https://python-poetry.org/docs/#installation>`_\nThen, get the dependencies by running (in the project home directory):\n\n.. code-block:: sh\n\n    poetry install\n\nAlso make sure you setup git hooks locally, this will ensure code is formatted using `black <https://github.com/psf/black>`_ before committing any changes to the repository\n\n.. code-block:: sh\n\n    pre-commit install\n\nRunning Tests\n-------------\n\nSpin up a mobilitydb instance\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n.. code-block:: sh\n\n    docker volume create mobilitydb_data\n    docker run --name "mobilitydb" -d -p 25432:5432 -v mobilitydb_data:/var/lib/postgresql codewit/mobilitydb\n\nRun the tests\n^^^^^^^^^^^^^\n\nmovingpandas is an optional dependency - but to run tests you would need it. So if this is your first time running tests, install it by running:\n\n.. code-block:: sh\n\n    # Currently installing the optional dependency of movingpandas\n    # using `poetry install -E movingpandas` doesn\'t work\n\n    # To get movingpandas use pip instead of poetry, run the following (in exact order):\n    poetry shell\n    pip install cython\n    pip install git+https://github.com/SciTools/cartopy.git --no-binary cartopy\n    pip install movingpandas\n\n    # This is because of movingpandas dependency cartopy not being PEP 518 compliant\n    # Refer: https://github.com/SciTools/cartopy/issues/1112\n\nNow, you can actually run the tests using:\n\n.. code-block:: sh\n\n    poetry run pytest\n',
    'author': 'B Krishna Chaitanya',
    'author_email': 'bkchaitan94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adonmo/mobilitydb-sqlalchemy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
