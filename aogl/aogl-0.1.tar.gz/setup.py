import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='aogl',  
    version='0.1',
    author="Andrew Odendaal",
    author_email="andrew@ao.gl",
    description="A python package to retrieve the latest 10 blog posts from https://ao.gl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ao/aogl_pip",
    packages=["aogl"],
    entry_points = {
        "console_scripts": ['aogl = aogl.aogl:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
