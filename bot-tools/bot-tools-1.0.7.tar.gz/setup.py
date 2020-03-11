import setuptools
from bot_tools import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bot-tools",
    version=__version__,
    author="Thor",
    author_email="theonlythor@protonmail.com",
    description="Common tools for python bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onlythor/bot_tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    install_requires=['colorama'],
    python_requires='>=3.6'
)
