import setuptools
from pathlib import Path

setuptools.setup(
    name="questgame", # Replace with your own username
    version="0.0.2",
    author="Chris Proctor",
    author_email="chris@chrisproctor.net",
    description="A simple game framework",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/cproctor/quest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
