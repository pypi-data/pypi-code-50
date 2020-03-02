import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keyboard-listener",
    version="0.0.7",
    author="Adib Attie",
    author_email="adib.attie33@gmail.com",
    description="A keyboard listener that allows for custom combinations and keywords to trigger custom functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dibsonthis/keyboard_listener",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)