from os.path import join, dirname, abspath

from setuptools import setup, find_packages

from nicely import __version__

curdir = abspath(dirname(__file__))
readme = open(join(curdir, 'README.rst')).read()

setup(
    name             = 'nicely',
    version          = __version__,
    description      = 'Python Fancy Printer',
    long_description = readme,
    keywords         = ['testing', 'logging', 'debugging'],
    url              = 'https://framagit.org/louis-riviere-xyz/nicely/tree/stable',
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
        'nicely': 'nicely',
    },
    packages = [
        'nicely',
    ],
)
