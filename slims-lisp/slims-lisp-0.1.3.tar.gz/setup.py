from setuptools import find_packages, setup

release_version = '0.1.3'

setup(
    name = 'slims-lisp',
    version = release_version,
    description = 'A high-level CLI for SlIMS REST API',
    long_description = open('README.rst').read(),
    long_description_content_type = 'text/x-rst',
    license = 'Apache License 2.0',
    author = 'Laboratory of Integrative System Physiology (LISP) at EPFL',
    author_email = 'alexis.rapin@epfl.ch',
    url = 'https://github.com/auwerxlab/slims-lisp-python-api',
    download_url = 'https://github.com/auwerxlab/slims-lisp-python-api/archive/v' + release_version + '.tar.gz',
    packages = find_packages(),
    python_requires = '>=3.5.2',
    install_requires = [
        'click>=7.0',
        'requests>=2.22.0',
        'datetime>=4.3',
    ],
    entry_points = {
        'console_scripts': [
            'slims-lisp = slims_lisp.__main__:cli'
        ]
    },
)
