from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requirements = {
    "package": [
        "marshmallow<3",
        "SQLAlchemy",
    ],
    "test": [
        "pytest",
    ]
}

requirements.update(all=sorted(set().union(*requirements.values())))

setup(
    name='golden_marshmallows',
    version='0.2.1',
    author='Guillaume Chorn',
    author_email='guillaume.chorn@gmail.com',
    packages=['golden_marshmallows'],
    url='https://github.com/gchorn/golden-marshmallows',
    download_url='https://github.com/gchorn/golden-marshmallows/archive/'
                 'v0.2.1.tar.gz',
    description='Marshmallow Schema subclass that auto-defines fields based on'
                ' SQLAlchemy classes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements['package'],
    license='MIT',
    test_suite='tests',
    tests_require=requirements['test'],
)
