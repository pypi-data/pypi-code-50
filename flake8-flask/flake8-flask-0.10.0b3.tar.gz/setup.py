# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['flake8_flask']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.7.9,<4.0.0', 'r2c-py-ast==0.1.0b1']

entry_points = \
{'flake8.extension': ['r2c-flake8 = flake8_flask.main:Flake8Flask']}

setup_kwargs = {
    'name': 'flake8-flask',
    'version': '0.10.0b3',
    'description': 'Static analysis checks for Flask, by r2c. Available in our free program analysis tool, Bento. (ht',
    'long_description': '# flake8-flask\n\nflake8-flask is a plugin for flake8 with checks specifically for the [flask](https://pypi.org/project/Flask/) framework, written by [r2c](https://r2c.dev)\n\n## Installation\n\n```\npip install flake8-flask\n```\n\nValidate the install using `--version`.\n\n```\n> flake8 --version\n3.7.9 (flake8-flask: 0.2.1, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1)\n```\n\n## List of warnings\n\n`r2c-flask-send-file-open`: This check detects the use of a file-like object in `flask.send_file` without either `mimetype` or `attachment_filename` keyword arguments. `send_file` will throw a ValueError in this situation.\n\n`r2c-flask-secure-set-cookie`: This check detects calls to `response.set_cookie` that do not have `secure`, `httponly`, and `samesite` set. This follows the [guidance in the Flask documentation](https://flask.palletsprojects.com/en/1.1.x/security/#set-cookie-options).\n\n`r2c-flask-unescaped-file-extension`: Flask will not autoescape Jinja templates that do not have .html, .htm, .xml, or .xhtml as extensions. This check will alert you if you do not have one of these extensions. This check will also do its best to detect if context variables are escaped if a non-escaped extension is used.\n\n`r2c-flask-use-blueprint-for-modularity`: This check recommends using Blueprint when there are too many route handlers in a single file. Blueprint encourages modularity and [can greatly simplify how large applications work and provide a central means for Flask extensions to register operations on applications.](https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints)\n\n`r2c-flask-use-jsonify`: `flask.jsonify()` is a [Flask](https://palletsprojects.com/p/flask/) helper method which handles the correct settings for returning JSON from Flask routes. This check catches uses of `json.dumps()` returned from Flask routes and encourages `flask.jsonify()` instead.\n\n`r2c-flask-missing-jwt-token`: This check alerts when `@jwt_required`, `@jwt_optional`, `@fresh_jwt_required`, and `@jwt_refresh_token_required` decorators are missing in files where `flask_jwt`, `flask_jwt_extended`, or `flask_jwt_simple` packages are imported.\n\nHave an idea for a check? Reach out to us at https://r2c.dev!\n',
    'author': 'grayson',
    'author_email': 'grayson@returntocorp.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
