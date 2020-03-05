from os.path import join, dirname, abspath

from setuptools import setup, find_packages

from sqlview import __version__


curdir = abspath(dirname(__file__))
readme = open(join(curdir, 'README.rst')).read()

setup(
    name             = 'sqlview',
    version          = __version__,
    description      = 'sqlite reader',
    long_description = readme,
    keywords         = ['utility', ],
    url              = 'https://framagit.org/louis-riviere-xyz/sqlview',
    author           = 'Louis RIVIERE',
    author_email     = 'louis@riviere.xyz',
    license          = 'MIT',
    classifiers      = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    package_dir = {
        'sqlview': 'sqlview',
    },
    packages = [
        'sqlview',
    ],
    entry_points = dict(
        console_scripts = (
            'sql_stats=sqlview.command:sql_stats',
            'sql_dump=sqlview.command:sql_dump',
        ),
    ),
)
