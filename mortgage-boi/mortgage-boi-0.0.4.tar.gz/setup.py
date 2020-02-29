import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mortgage-boi",
    version="0.0.4",
    author="Charlie Reese",
    author_email="j.charles.reese@gmail.com",
    description="A package for calculating mortgage data and cash flows",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/charliereese/mortgage_boi",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Financial and Insurance Industry",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",	
    ],
    python_requires='>=3.6',
)
