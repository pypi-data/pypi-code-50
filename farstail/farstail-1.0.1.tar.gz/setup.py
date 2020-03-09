import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="farstail", # Replace with your own username
    version="1.0.1",
    author="mohammad azari jafari",
    author_email="azari.jafari.m@gmail.com",
    description="Persian Natural Language Inference DataSet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m-azari/FarsTail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		"Natural Language :: Persian",
    ],
    python_requires='>=3.6',
)