import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdsheets",
    version="1.0.1",
    author="Rodrigo Gonçalves",
    author_email="rodrigo@santodigital.com.br",
    description="Lib para recuperar informações de planilhas do Google Spreadsheets",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://bitbucket.org/santodigital/sdsheets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)