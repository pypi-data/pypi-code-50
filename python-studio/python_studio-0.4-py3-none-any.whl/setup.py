import setuptools


with open("Python_Studio/README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = "python studio",
    version = "0.4",
    
    
    author = "Tony Stark",
    author_email = "xsumagravity@gmail.com",
    
    
    description = "studio for running apps",
    long_description = long_description,
    
    
    long_description_content_type = "text/markdown",
    url = "",
    
    
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)