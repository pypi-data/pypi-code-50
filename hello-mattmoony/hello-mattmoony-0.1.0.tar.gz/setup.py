import json
from setuptools import setup

with open('hello/conf.json', 'r') as f:
    version = json.load(f)['__version__']

setup(
    name='hello-mattmoony',
    packages=['hello',],
    entry_points={
        'console_scripts': ['hello-mattmoony = hello.hello:main',],
    },
    version=version,
    description='Hello World - Python app',
    author='Matthias M.',
    author_email='m4ttm00ny@gmail.com'
)