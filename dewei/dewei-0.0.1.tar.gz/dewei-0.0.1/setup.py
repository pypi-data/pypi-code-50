import setuptools


setuptools.setup(
    name="dewei",
    version="0.0.1",
    author="Dewei",
    author_email="deweiliu@hotmail.com",
    description="A small example package",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://deweiliu.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3,<4',
)
