import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="sc2-tournament-analysis",
    version="0.0.17",
    author="ZephyrBlu/Luke Holroyd",
    author_email="hello@zephyrus.gg",
    description="A script for analyzing tournament replay packs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZephyrBlu/sc2-tournament-analysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
