# setup(
#     name = 'CURTIS',
#     version = '0.1',
#     description = 'Automatic generation of commutative diagrams',
#     url = 'https://github.com/pribanacek/Part-II-Project',
#     author = 'Jakub Priban',
#     # license = 'something',
#     packages = find_packages('antlr', 'networkx', 'numpy')
# )

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="CICADAS",
    version="1.0.0a1",
    author="Jakub Priban",
    author_email="jp775@cam.ac.uk",
    description="Self-constructing commutative diagrams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pribanacek/cicadas",
    packages=find_packages(where = 'src'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/pribanacek/cicadas/issues',
        'Source': 'https://github.com/pribanacek/cicadas',
    },
)
