import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sinner",
    version="0.0.1",
    author="Friar Hob",
    author_email="github@friarhob.33mail.com",
    description="SINNER - Simplest Implementation of Neural Networks for Effortless Runs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/friarhob/sinner-neural",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
