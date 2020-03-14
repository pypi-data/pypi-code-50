import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randomwalk", # Replace with your own username
    version="0.0.1",
    author="Rahul Raj",
    author_email="rahulrajpl@protonmail.com",
    description="Package for automating various personal tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahulrajpl/randomwalk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)