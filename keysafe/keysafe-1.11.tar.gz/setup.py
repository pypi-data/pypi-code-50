from setuptools import setup, find_packages
from keysafe import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='keysafe',
    author='ViperVit (V.Vigasin)',
    author_email='vitolg1@gmail.com',
    license='Apache',
    description='Keyring-based utilitiy for enchanced safekeeping of login informaiton.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test*"]),
    url='https://github.com/vipervit/keysafe',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Security"
    ]
)
