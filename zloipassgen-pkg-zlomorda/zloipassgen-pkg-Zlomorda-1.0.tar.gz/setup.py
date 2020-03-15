import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zloipassgen-pkg-Zlomorda", # Replace with your own username
    version="1.0",
    author="Zlomorda",
    author_email="daticho@gmail.com",
    description="Zloi (and Evil) password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zlomorda/zloipassgen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)