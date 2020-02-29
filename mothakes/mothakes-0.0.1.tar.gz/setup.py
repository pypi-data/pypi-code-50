import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mothakes", # Replace with your own username
    version="0.0.1",
    author="Simon Fong",
    author_email="simonfong6@gmail.com",
    description="Tools used by Simon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simonfong6/mothakes-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
