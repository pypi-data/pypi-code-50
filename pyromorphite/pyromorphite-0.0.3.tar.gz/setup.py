import os

import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
]

packages = ['pyromorphite']

requires = [
    'pandas==0.25.3',
    'lxml==4.4.2'
    'networkx==2.4.0',
]

test_requirements = [
    'pytest>=3',
    'pytest-benchmark>=3.2.3'
]

about = {}
with open(os.path.join(HERE, 'pyromorphite', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],

    packages=packages,
    package_data={'': ['LICENSE']},

    include_package_data=True,
    install_requires=requires,

    classifiers=classifiers,
    python_requires=">=3.5",
    project_urls={
        'Documentation': 'https://pyromorphite.readthedocs.io',
        'Source': 'https://github.com/xcavation/pyromorphite',
    },
)
