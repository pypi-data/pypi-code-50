import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name                          = "basemath",
    version                       = "1.0.2",
    license                       = "MIT",
    author                        = "eerne/m13kj (Ernest)",
    author_email                  = "infinitumco666@gmail.com",
    description                   = "A small library to work with numbers of any base",
    long_description              = long_description,
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/m13kj/basemath",
    package_dir                   = {'': '.'},
    packages                      = setuptools.find_packages(),
    classifiers                   = [
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering"
        ],
    python_requires = ">=3.6",
    )
