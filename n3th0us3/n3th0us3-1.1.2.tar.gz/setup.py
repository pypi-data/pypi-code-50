from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='n3th0us3',
    version='1.1.2',
    packages=find_packages(exclude=['unittests*', ]),
    package_dir={'n3th0us3': 'n3th0us3'},
    author='Anzhela',
    author_email='dev.anzhela@gmail.com',
    description="Unofficial python package for domains.nethouse.ru service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
