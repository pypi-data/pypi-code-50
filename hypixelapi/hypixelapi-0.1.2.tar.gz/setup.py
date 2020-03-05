import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypixelapi",
    version="0.1.2",
    author="MylesMor",
    author_email="hello@mylesmor.dev",
    license="MIT",
    description="A Python 3 wrapper for the HypixelAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MylesMor/hypixelapi",
    packages=setuptools.find_packages(),
    install_requires=["requests", "argparse"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
