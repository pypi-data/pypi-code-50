import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ski",
    version="0.1.7",
    author="Papan Yongmalwong",
    author_email="papillonbee@gmail.com",
    description="ski is a package for educational purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/papillonbee",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'cmocean==2.0'
    ]
)