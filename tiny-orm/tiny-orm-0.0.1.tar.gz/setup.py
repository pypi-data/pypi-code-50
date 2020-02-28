"""
Contains information necessaries to build, release and install a distribution.
"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tiny-orm',
    version='0.0.1',
    author='Meng Xiangzhuo',
    author_emial='15195891330@163.com',
    description='A tiny ORM for SQLite',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xzmeng/tiny-orm',
    license='MIT License',
    py_modules=['tiny_orm'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
    ],  # see more at https://pypi.python.org/pypi?%3Aaction=list_classifiers
    zip_safe=False,
    python_requires='>=3.6',
)
