import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvote-api",
    version="0.0.1",
    author="baccenfutter",
    author_email="baccenfutter@c-base.org",
    description="Simple voting API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c-base/pyvote",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
