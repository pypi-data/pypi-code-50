import pathlib
from setuptools import setup, find_packages
from mlnods import __version__, name

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name=name,
    version=__version__,
    keywords="graph partition, graph analysis, cross-validation dataset",
    description="""a python package to split machine learning data sets using graph partitioning""",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/bromberglab/mlnods",
    author="Yana Bromberg, Maximilian Miller",
    author_email="mmiller@bromberglab.com",
    license="NPOSL-3.0",
    python_requires='>=3.6',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
    ],
    entry_points = {
        'console_scripts': ['mlnods=mlnods.__main__:main'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
        "Operating System :: OS Independent"
    ],  
    project_urls={
        "Bug Tracker": "https://bitbucket.org/bromberglab/mlnods/issues",
        "Documentation": "https://bitbucket.org/bromberglab/mlnods/wiki/docs",
        "Source Code": "https://bitbucket.org/bromberglab/mlnods",
    }
)
