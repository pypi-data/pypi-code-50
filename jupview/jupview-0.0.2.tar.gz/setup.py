import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupview", # Replace with your own username
    version="0.0.2",
    author="Artiom Peysahovsky",
    author_email="peysahovsky@gmail.com",
    description="Simple terminal jupyter notebook viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artiomio/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Environment :: Console"
    ],
    python_requires='>=3.6',
    scripts=["jupview"],
    py_modules=["jupview"]
    
)