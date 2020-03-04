# -*- coding: utf-8 -*-

# from distutils.core import setup
from setuptools import setup, find_packages

# read the contents of your README file
from os import path
import augmentedtree


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Setuptools clean option only removes the build folder.

REMOVE_THESE_PATH_PRIOR_SETUP = ["build", "dist", "*.egg-info"]
REMOVE_THESE_PATH_POST_SETUP = ["build", "*.egg-info"]


def _remove_paths(root_path, path_patterns):
    """
    Remove path using rmtree of shutils within *root_path* by the given unix-pattern.

    Args:
        root_path (str):
            Path in which folders shall be removed.

        path_patterns (List[str]):
            Pattern of folders to be removed.
    """
    from shutil import rmtree
    from pathlib import Path
    abs_path = Path(root_path).resolve()
    paths_to_remove = []
    for path_pattern in path_patterns:
        found_paths_to_remove = list(abs_path.glob(path_pattern))
        paths_to_remove.extend(found_paths_to_remove)

    for path_to_remove in paths_to_remove:
        print("removing path {}".format(path_to_remove))
        rmtree(path_to_remove)


_remove_paths(this_directory, REMOVE_THESE_PATH_PRIOR_SETUP)


setup(
    name="augmentedtree",
    version=augmentedtree.__version__,
    author="David Scheliga",
    author_email="david.scheliga@ivw.uni-kl.de",
    url="https://gitlab.com/david.scheliga/augmentedtree",
    project_urls={
        "Documentation": "https://augmentedtree.readthedocs.io/en/latest/",
        "Source Code Repository": "https://gitlab.com/david.scheliga/augmentedtree"
    },
    description="Easy navigation within nested data of mappings (dict, ...) and "
    "sequences (list, ...). Easy access of values via single keys within"
    " these nested data structures. Enables different (human accessable)"
    " representation of nested data structures.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU General Public License v3 (GPLv3)",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
    ],
    keywords="dictionary, mapping, list, sequence, nested, handling, navigation, selection",
    python_requires=">=3.6",
    packages=find_packages(exclude=["*.scratches", "*.debug_scripts", "*.scratches.*", "*.debug_scripts.*"]),
    requires=["pandas", 'numpy'],
)


_remove_paths(this_directory, REMOVE_THESE_PATH_POST_SETUP)
