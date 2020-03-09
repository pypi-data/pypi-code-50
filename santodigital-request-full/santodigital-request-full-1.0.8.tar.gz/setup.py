import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="santodigital-request-full", # Replace with your own username
    version="1.0.8",
    author="Rodrigo Gonçalves",
    author_email="rodrigo@santodigital.com.br",
    description="Http request library for paginated response api",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://bitbucket.org/santodigital/santodigital-request-full",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)