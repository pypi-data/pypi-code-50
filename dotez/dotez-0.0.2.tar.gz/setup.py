from setuptools import setup, find_packages
from os.path import dirname, abspath

root_location = dirname(abspath(__file__))

with open(root_location + '/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="dotez",
    version="0.0.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dotez = dotez.cli:main",
        ],
    },
    install_requires=requirements,
    include_package_data=True,

    # metadata to display on PyPI
    author="Jiyang Tang",
    author_email="tjy1018543509@gmail.com",
    description="Python module for managing dotfiles easily",
    keywords="dotfiles,git,backup",
    url="http://github.com/tjysdsg/dot-easy/",
    project_urls={
        "Bug Tracker": "http://github.com/tjysdsg/dot-easy/issues",
        "Documentation": "http://github.com/tjysdsg/dot-easy/wiki",
        "Source Code": "http://github.com/tjysdsg/dot-easy",
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities'
        # https://pypi.org/classifiers/
    ]
)
