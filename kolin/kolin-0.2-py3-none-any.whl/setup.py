import setuptools

with open("kolin/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kolin",
    version="0.2",
    
    
    author="Downey",
    author_email="xsumagravity@gmail.com",
    
    
    description="Allows you to use kolin language",
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
