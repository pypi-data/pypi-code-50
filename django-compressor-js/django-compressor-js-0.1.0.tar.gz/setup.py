# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_compressor_js']

package_data = \
{'': ['*']}

install_requires = \
['django-compressor>=2.4,<3.0', 'dukpy>=0.2.2,<0.3.0']

setup_kwargs = {
    'name': 'django-compressor-js',
    'version': '0.1.0',
    'description': 'Transpile JavaScript without running an extra node.js process.',
    'long_description': '# django-compressor-js\n\nInstead of running an extra node.js process watching for changes in your Javascript, this precompiler for `django-compressor` will convert any ES6 code into ES5 automagically.\n\n# Install\n1. `pip install django-compressor-js`\n1. Add precompiler (`text/es6` can be anything, but it has to match the script type in the template)\n```\nCOMPRESS_PRECOMPILERS = (\n    ("text/es6", "django_compressor_js.precompilers.BabelCompiler"),\n)\n```\n1. Add to HTML template\n```\n{% compress js %}\n\t<script src="{% static \'js/test-es6-code.js\' %}" type="text/es6"></script>\n{% endcompress %}\n```\n\n# Caveats\nMost ES6 syntax seems to work pretty well, but requiring modules doesn\'t import correctly. Also, this approach adds some latency when compressing on the fly (i.e. `COMPRESS_OFFLINE = False`).\n\n# Run tests\n`poetry run pytest`\n\n# Credits\n`dukpy` and `django-compressor` for doing all the hard things.\n',
    'author': 'Adam Hill',
    'author_email': 'adamghill@yahoo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adamghill/django-compressor-js',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
