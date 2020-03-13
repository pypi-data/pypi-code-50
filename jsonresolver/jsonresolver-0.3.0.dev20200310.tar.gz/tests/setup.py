import os

from setuptools import setup

current_dir = os.getcwd()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.2.2',
    'mock>=1.3.0',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=2.8.1',
    'pytest-pep8>=1.0.6',
    'pytest>=3.0.0',
    'requests>=2.7.0',
]

extras_require = {
    'docs': [
        "Sphinx>=1.5.1",
    ],
    'jsonref': [
        'jsonref>=0.1',
    ],
    'jsonschema': [
        'jsonschema>=2.5.1',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.7.0',
]

install_requires = [
    'six>=1.12.0',
    'pluggy>=0.10.0,<1.0',
    'werkzeug>=1.0.0',
]

setup(
    name="demo",
    packages=['demo'],
    package_dir={'demo': current_dir},
    install_requires=install_requires,
    extras_require=extras_require,
    setup_requires=setup_requires,
    # the following makes a plugin available to pytest
    entry_points={
        'espresso': ['demo.simple = demo.simple'],
        'raising': ['demo.raising = demo.raising'],
        'raising_hook': ['demo.raising_hook = demo.raising_hook'],
        'someotherstuff': [],
        'doubletrouble': ['demo.simple = demo.simple',
                          'demo.simple2 = demo.simple'],
        'importfail': ['importfail = test.importfail'],
    }
)
