import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="basepackage",
    version="0.1.1",
    author="Lucifer Monao",
    author_email="Lucifermonao@gmx.de",
    description="This package includes some, for me, helpful small things.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/users/LuciferMonao/projects/2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)