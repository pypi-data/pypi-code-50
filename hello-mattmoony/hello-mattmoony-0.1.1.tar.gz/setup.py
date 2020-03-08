import json
from setuptools import setup

setup(
    name='hello-mattmoony',
    packages=['hello',],
    entry_points={
        'console_scripts': ['hello-mattmoony = hello.hello:main',],
    },
    version='0.1.1',
    description='Hello World - Python app',
    author='Matthias M.',
    author_email='m4ttm00ny@gmail.com'
)