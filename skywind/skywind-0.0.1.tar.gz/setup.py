import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skywind",
    version="0.0.1",
    author="cookiery",
    author_email="2061803022@qq.com",
    description="A test Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cookiery",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
