from setuptools import setup, find_packages

setup(
    name="latexlate",
    version="1.1.5",
    author = "Nanopro",
    author_email = "nanopro1g@gmail.com",
    description = "A small template language for LaTeX, now with support for wolfram mathematica",
    long_description='A small template language for LaTeX, now with support for wolfram mathematica',
    long_description_content_type="text/markdown",
    url="https://gitlab.com/nanopro/latexlate",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
