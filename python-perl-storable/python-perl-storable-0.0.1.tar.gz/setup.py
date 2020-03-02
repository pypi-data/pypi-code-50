from setuptools import setup, find_packages
from os.path import join, dirname
import re

readme = open(join(dirname(__file__), 'README.md')).read()

def get(r, name):
    match = re.search(r, readme, re.S | re.M)
    if not match:
        raise Exception("В README.md не найден" + name)
    return match

version = get(r'^# VERSION\s*(\S+)', "а версия")
author = get(r'^# AUTHOR\s*([^<>#]+)\s+<([^<>]+)>', " автор")
description = get(r'^# NAME\s*([^\n]+?)\s*$', "о описание")
requirements = get(r'^# REQUIREMENTS\s+([^#]*?)\s*#', "ы зависимости")

requirements = requirements.group(1)
requirements = [] if requirements == 'Нет' else requirements.split('\n* ')

setup(
    name='python-perl-storable',
    version=version.group(1),
    description=description.group(1),
    long_description=readme,
    long_description_content_type="text/markdown",

    #scripts=[],
    platforms=['any'],
    python_requires='>=3.6',
    # The project's main homepage.
    url='https://github.com/darviarush/python-perl-storable',

    # Author details
    author=author.group(1),
    author_email=author.group(2),

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        "Topic :: Text Processing",

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        
        "Operating System :: OS Independent",

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    
   # What does your project relate to?
    # keywords='sample setuptools development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=requirements,

    # setup_requires=[]

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
        # 'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

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
