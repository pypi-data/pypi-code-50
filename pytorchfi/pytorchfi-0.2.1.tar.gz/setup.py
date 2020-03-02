import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorchfi",
    version="0.2.1",
    author="UIUC RSim",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/pytorchfi/pytorchfi",
    project_urls={
        "Documentation": "https://pytorchfi.github.io",
        "Source Code": "https://github.com/pytorchfi/pytorchfi"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
