import ptst_swagger

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='ptst_swagger',
    version=ptst_swagger.__version__,
    packages=find_packages(),
    url='https://github.com/vden68/ptst_swagger',
    license='',
    author='Vasiliy Denisov',

    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'allure-pytest',
        'requests',
        'requests-toolbelt',
    ],
)