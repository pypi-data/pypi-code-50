# Copyright (c) 2020 Marco Giusti

from os.path import join as joinpath, dirname, abspath
from setuptools import setup


SETUPDIR = abspath(dirname(__file__))


def version():
    glb = {}
    with open(joinpath(SETUPDIR, 'src', 'pygments_graphql.py')) as fp:
        for line in fp:
            if '__version__' in line:
                exec(line, glb)
                return glb['__version__']
    raise RuntimeError('__version__ not found')


def long_description():
    with open(joinpath(SETUPDIR, 'README.rst')) as fp:
        return fp.read()


setup(
    name='pygments-graphql',
    version=version(),
    description='Pygments lexer for GraphQL files',
    long_description=long_description(),
    author='Marco Giusti',
    author_email='marco.giusti@posteo.de',
    license='MIT',
    url='https://gitlab.com/marcogiusti/pygments-graphql',
    py_modules=['pygments_graphql'],
    package_dir={'': 'src'},
    install_requires=[
        'pygments'
    ],
    extras_require={
        'dev': [
            'flake8',
            'pip-tools',
            'tox'
        ]
    },
    entry_points={
        'pygments.lexers': ['graphql = pygments_graphql:GraphqlLexer'],
    },
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    )
)
