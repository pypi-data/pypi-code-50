import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yalow",
    version="0.0.2",
    author="Zechariah Thurman",
    author_email="zechariah.thurman@gmail.com",
    description="Yet Another LOgging Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zthurman/yalow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)