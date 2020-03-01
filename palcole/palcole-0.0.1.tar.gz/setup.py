import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name = "palcole",
        version = "0.0.1",
        author = "Marcelo Nuñez",
        author_email = "real.nugatti@gmail.com",
        description = "Modulo preparado para el colegio",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/marcelo-nugatti/PalCole",
        packages = setuptools.find_packages(),
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires = '>=3.6',
)


    















