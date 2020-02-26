import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decp_scraper",
    version="1.0.6",
    author="JLoDoesIT",
    author_email="jlospam@hotmail.com",
    description="Extract DECP files from few websites easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JLoDoesIt/atexo-decp-scraper",
    packages=setuptools.find_packages(),
    package_data={'decp_scraper': ['plateformes.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
