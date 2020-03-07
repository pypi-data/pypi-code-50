#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="cmdtime",
    version="0.0.3",
    packages=setuptools.find_packages(),

    entry_points = {
        'console_scripts': [
            'cmdtime=cmdtime.cmdtime:main'
        ],
    },

    # metadata to display on PyPI
    author="Ravi Chandran",
    description="Similar to Linux `time` utility useful for Windows Command Prompt using pure Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ravi-chandran/cmdtime",

    python_requires=">=3.5",    
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
