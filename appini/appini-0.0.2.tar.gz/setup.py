import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "appini",
    version = "0.0.2",
    author = "Umut YILDIRIM",
    author_email = "umut374@gmail.com",
    description = ("A tool to create mobile apps from websites "
                                   "using flutter and dart."),
    license = "GNU",
    keywords = "mobileapp websites appini",
    url = "https://appini.ml/cli",
    packages=['appini'],
    zip_safe=False,
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://gitlab.com/HopeSweaty/appini/issues",
        "Documentation": "https://docs.appini.ml/CLI/get_started/",
        "Source Code": "https://gitlab.com/HopeSweaty/appini/",
    },
    # python_requires='>=3.5',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
    scripts=['bin/appini'],
)