import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wallet_lib',
    version='1.2.7',
    author="Bitcoin.com",
    author_email="gamesbot@bitcoin.com",
    description="Package to work with hot wallet for different cryptocurrency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bitcoin-com/wallet_lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pyzmq==18.1.1','simplejson==3.17.0','python-bitcoinrpc==1.0'],
    python_requires='>=3.6'
)
