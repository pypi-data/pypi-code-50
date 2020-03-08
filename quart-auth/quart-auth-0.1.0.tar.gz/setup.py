# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['quart_auth']

package_data = \
{'': ['*']}

install_requires = \
['quart>=0.11']

setup_kwargs = {
    'name': 'quart-auth',
    'version': '0.1.0',
    'description': 'A Quart extension to provide secure cookie authentication',
    'long_description': 'Quart-Auth\n==========\n\n|Build Status| |pypi| |python| |license|\n\nQuart-Auth is an extension for `Quart\n<https://gitlab.com/pgjones/quart>`_ to provide for secure cookie\nauthentication (session management). It allows for a session to be\nlogged in, authenticated and logged out.\n\nUsage\n-----\n\nTo use Quart-Auth with a Quart app you have to create an AuthManager and\ninitialise it with the application,\n\n.. code-block:: python\n\n    app = Quart(__name__)\n    AuthManager(app)\n\nor via the factory pattern,\n\n.. code-block:: python\n\n    auth_manager = AuthManager()\n\n    def create_app():\n        app = Quart(__name__)\n        auth_manager.init_app(app)\n        return app\n\nIn addition you will need to configure Quart-Auth, which defaults to\nthe most secure. At a minimum you will need to set secret key,\n\n.. code-block:: python\n\n    app.secret_key = "secret key"  # Do not use this key\n\nwhich you can generate via,\n\n.. code-block:: python\n\n    >>> import secrets\n    >>> secrets.token_urlsafe(16)\n\nTou may also need to disable secure cookies to use in development, see\nconfiguration below.\n\nWith AuthManager initialised you can use the ``login_required``\nfunction to decorate routes that should only be accessed by\nauthenticated users,\n\n.. code-block:: python\n\n    @app.route("/")\n    @login_required\n    async def restricted_route():\n        ...\n\nYou can also use the ``login_user``, and ``logout_user`` functions to\nstart and end sessions for a specific ``AuthenticatedUser`` instance,\n\n.. code-block:: python\n\n    @app.route("/login")\n    async def login():\n        # Check Credentials here, e.g. username & password.\n        ...\n        # We\'ll assume the user has an identifying ID equal to 2\n        login_user(AuthenticatedUser(2))\n        ...\n\n    @app.route("/logout")\n    async def logout():\n        logout_user()\n        ...\n\nExtending Quart-Auth\n--------------------\n\nQuart-Auth is meant to be extended, much like Quart (and Flask), a\ngood example of this is loading user data from a database,\n\n.. code-block:: python\n\n    from quart import Quart\n    from quart_auth import AuthenticatedUser, AuthManager, current_user, login_required\n\n    class User(AuthenticatedUser):\n        def __init__(self, auth_id):\n            super().__init__(auth_id)\n            self._resolved = False\n            self._email = None\n\n        async def _resolve(self):\n            if not self._resolved:\n                self._email = await db.fetch_email(self.auth_id)\n                self._resolved = True\n\n        @property\n        async def email(self):\n            await self._resolve()\n            return self._email\n\n    auth_manager = AuthManager()\n    auth_manager.user_class = User\n\n    app = Quart(__name__)\n\n    @app.route("/")\n    @login_required\n    async def index():\n        return await current_user.email\n\n    auth_manager.init_app(app)\n\n.. note::\n\n    If you are used to Flask-Login you are likely expecting the\n    current_user to be fully loaded without the extra resolve\n    step. This is not possible in Quart-Auth as the ``current_user``\n    is loaded synchronously whereas the User is assumed to be loaded\n    asynchronously i.e. ``await current_user.email`` is preferred over\n    ``(await current_user).email``.\n\nAuth ID\n~~~~~~~\n\nQuart-Auth authenticates using a ``str``, ``auth_id``, which can be\nset to the User ID. It is better not use the user\'s ID in case the\nuser\'s session is compromised e.g. via a stolen phone, as the\n``auth_id`` itself most be revoked to disable the session.\n\nConfiguration\n-------------\n\nThe following configuration options are used by Quart-Auth,\n\n============================ ============================= ===================\nConfiguration key            type                          default\n---------------------------- ----------------------------- -------------------\nQUART_AUTH_COOKIE_DOMAIN     Optional[str]                 None\nQUART_AUTH_COOKIE_NAME       str                           QUART_AUTH\nQUART_AUTH_COOKIE_PATH       str                           /\nQUART_AUTH_COOKIE_HTTP_ONLY  bool                          True\nQUART_AUTH_COOKIE_SAMESITE   Union[None, "Strict", "Lax"]  Strict\nQUART_AUTH_COOKIE_SECURE     bool                          True\nQUART_AUTH_DURATION          int                           365 * 24 * 60 * 60\nQUART_AUTH_SALT              str                           quart auth salt\n============================ ============================= ===================\n\nThe ``COOKIE`` related options refer directly to standard cookie\noptions. In development it is likely that you\'ll need to set\n``QUART_AUTH_COOKIE_SECURE`` to ``False``.\n\nContributing\n------------\n\nQuart-Auth is developed on `GitLab\n<https://gitlab.com/pgjones/quart-auth>`_. You are very welcome to\nopen `issues <https://gitlab.com/pgjones/quart-auth/issues>`_ or\npropose `merge requests\n<https://gitlab.com/pgjones/quart-auth/merge_requests>`_.\n\nTesting\n~~~~~~~\n\nThe best way to test Quart-Auth is with Tox,\n\n.. code-block:: console\n\n    $ pip install tox\n    $ tox\n\nthis will check the code style and run the tests.\n\nHelp\n----\n\nThis README is the best place to start, after that try opening an\n`issue <https://gitlab.com/pgjones/quart-auth/issues>`_.\n\n\n.. |Build Status| image:: https://gitlab.com/pgjones/quart-auth/badges/master/pipeline.svg\n   :target: https://gitlab.com/pgjones/quart-auth/commits/master\n\n.. |pypi| image:: https://img.shields.io/pypi/v/quart-auth.svg\n   :target: https://pypi.python.org/pypi/Quart-Auth/\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/quart-auth.svg\n   :target: https://pypi.python.org/pypi/Quart-Auth/\n\n.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg\n   :target: https://gitlab.com/pgjones/quart-auth/blob/master/LICENSE\n',
    'author': 'pgjones',
    'author_email': 'philip.graham.jones@googlemail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/pgjones/quart-auth/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
