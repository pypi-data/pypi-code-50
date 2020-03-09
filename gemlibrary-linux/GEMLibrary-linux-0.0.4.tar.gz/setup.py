import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GEMLibrary-linux",
    version="0.0.4",
    include_package_data=True,
    author="Kevin Morgan",
    author_email="KMorgan@teleioscommodities.com",
    description="GEM Derivatives Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX :: Linux",
    ],
    python_required=">=3.6",
)
