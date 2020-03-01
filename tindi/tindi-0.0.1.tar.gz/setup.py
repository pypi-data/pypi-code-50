import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tindi", # Replace with your own username
    version="0.0.1",
    author="Marcelo Nunez",
    author_email="real.nugatti@gmail.com",
    description="Paquete calculadora",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcelo-nugatti/tindi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
