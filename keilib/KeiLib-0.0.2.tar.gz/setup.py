import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KeiLib",
    version="0.0.2",
    author="Kei0x",
    author_email="kei0x@protonmail.com",
    description="My personal library for using 42API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/kei0x/keilib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
