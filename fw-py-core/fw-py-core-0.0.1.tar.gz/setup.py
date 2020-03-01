import setuptools
from core.clean import CleanCommand
from core.release import ReleaseCommand

# with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="fw-py-core",
    version="0.0.1",
    author="rainmakers",
    author_email="rainmakers9090@gmail.com",
    description="Python core library'",
    long_description_content_type="text/markdown",
    # url="https://github.com",
    packages=setuptools.find_packages(exclude=["tests"]),
    cmdclass={"clean": CleanCommand , "release": ReleaseCommand},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
