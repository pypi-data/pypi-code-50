"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='atcodes_chappie',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.2',

    description='A collection of tools and utilities commonly for python projects.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/atcodesco/chappie/',

    # Author details
    author='ATCODES Dev Team',
    author_email='admin@atcodes.co',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        # # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',

        # Topics
        # 'Natural Language :: English',
    ],

    # What does your project relate to?
    keywords='utilities clients',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    # py_modules=['chappie'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'asgiref>=3.2.3',
        'bleach>=3.1.0',
        'blessings>=1.7',
        'boto3>=1.7.4',
        'botocore>=1.10.4',
        'bpython>=0.18',
        'Cerberus>=1.3.2',
        'certifi>=2019.11.28',
        'chardet>=3.0.4',
        'curtsies>=0.3.1',
        'docutils>=0.14',
        'greenlet>=0.4.15',
        'idna>=2.8',
        'importlib-metadata>=1.5.0',
        'jmespath>=0.9.3',
        'keyring>=21.1.0',
        'pkginfo>=1.5.0.1',
        'Pygments>=2.5.2',
        'pyparsing>=2.4.6',
        'python-dateutil>=2.6.1',
        'pytz>=2019.3',
        'PyYAML>=5.3',
        'readme-renderer>=24.0',
        'requests>=2.22.0',
        'requests-toolbelt>=0.9.1',
        'rollbar>=0.14.7',
        's3transfer>=0.1.13',
        'six>=1.14.0',
        'sqlparse>=0.3.0',
        'tqdm>=4.42.1',
        'twine>=3.1.1',
        'urllib3>=1.25.8',
        'wcwidth>=0.1.8',
        'webencodings>=0.5.1',
        'zipp>=2.1.0'
    ],  # example> ['boto3==1.5.22',]

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': [],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'chappie': ['config/*.yaml'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
