from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="printlist-YY", # Replace with your own username
    version="0.0.1",
    author="ZouYuan",
    author_email="zouyuan@example.com",
    description="print a list",
    long_description=long_description,
    url="https://github.com/pypa/HeadFirstProject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
