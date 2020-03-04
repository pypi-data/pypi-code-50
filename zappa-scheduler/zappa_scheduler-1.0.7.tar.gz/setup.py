import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='zappa_scheduler',
    version='1.0.7',
    packages=find_packages(".", exclude='tests'),
    url='https://github.com/wisaac407/zappa-scheduler',
    license='MIT License',
    author='andytwoods, Isaac Weaver',
    author_email='andytwoods@gmail.com, wisaac407@gmail.com',
    description="Store future tasks in the db and call them after set delays.",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=['django-picklefield']
)
