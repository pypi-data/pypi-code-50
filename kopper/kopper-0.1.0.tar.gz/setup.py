import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="kopper",
    version="0.1.0",
    author="smbyeon",
    author_email="smbyun0214@gmail.com",
    description="Korail Seat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smbyeon/kopper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests', 'beautifulsoup4', 'numpy', 'pillow', 'matplotlib'],
)