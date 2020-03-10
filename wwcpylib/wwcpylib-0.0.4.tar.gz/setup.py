import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wwcpylib",  # Replace with your own username
    version="0.0.4",
    author="iamwwc",
    author_email="qaq1362211689@gmail.com",
    description="More useful tools!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamwwc/wwcpylib",
    packages=['wwcpylib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    include_package_data=True
)
