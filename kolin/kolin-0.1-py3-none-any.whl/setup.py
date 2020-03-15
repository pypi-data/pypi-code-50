import setuptools

with open("kolin/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kolin",
    version="0.1",
    
    
    author="Downey",
    author_email="xsumagravity@gmail.com",
    
    
    description="Allows you to use kolin langua",
    long_description=long_description,
    
    
    long_description_content_type="text/markdown",
    url="",
    
    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.0',
)
