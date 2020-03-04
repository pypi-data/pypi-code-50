# setup.py
# Copyright (C) 2020 Fracpete (fracpete at gmail dot com)

from setuptools import setup


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="rnb2docker",
    description="Library for turning R Jupyter Notebooks into Docker images.",
    long_description=(
        _read('DESCRIPTION.rst') + b'\n' +
        _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/fracpete/rnb2docker",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
    ],
    license='Apache Software License 2.0',
    package_dir={
        '': 'src'
    },
    packages=[
        "rnb2docker",
    ],
    version="0.0.1",
    author='Peter "fracpete" Reutemann',
    author_email='fracpete@gmail.com',
    entry_points={
        "console_scripts": [
            "rnb2docker=rnb2docker.generator:sys_main",
        ]
    }
)
