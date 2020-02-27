import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datalake_vqd_utils", # Replace with your own username
    version="0.0.21",
    author="Casper van Houten",
    author_email="casper.vanhouten@viqtordavis.com",
    description="Package containing tools for cloud-based data lakes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    'boto3>=1.9.222',
    'sqlalchemy>=1.3.13',
    'pymysql>=0.9.3',
    'pandas>=0.23.4'
    ],
    python_requires='>=3.6',
)
