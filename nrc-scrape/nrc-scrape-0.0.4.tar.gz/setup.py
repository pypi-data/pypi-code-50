import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nrc-scrape", # Replace with your own username
    version="0.0.4",
    author="Bradley Fox",
    author_email="bradfox2@gmail.com",
    description="Python package to scrape NRC Event Reports.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bradfox2/nrc-scrape",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['beautifulsoup4==4.8.2',
                        'numpy==1.18.1',
                        'pandas==1.0.1',
                        'requests==2.23.0',
                        'python-dateutil==2.8.1'],
    python_requires='>=3.7',
)