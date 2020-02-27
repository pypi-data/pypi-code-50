from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pav_logger',
    version='1.0.1',
    description='PavLogger provides the ability to log debug and exception to a text file or a SQLite database with optional Backtrace output.',
    url="https://github.com/PavtheDog/pav_logger",
    author='PavtheDog',
    author_email='',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = [],
    extras_require = {
        "dev":[
            "pytest>=3.7",
        ],
    },
)
