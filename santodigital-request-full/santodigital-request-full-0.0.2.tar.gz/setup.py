import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="santodigital-request-full", # Replace with your own username
    version="0.0.2",
    author="Rodrigo Gonçalves",
    author_email="rodrigo@santodigital.com.br",
    description="Http request library for paginated response api",
    long_description=long_description,
    url="https://bitbucket.org/rodrigoag/santodigital-request-full",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)