import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="101703196_topsis", # Replace with your own username
    version="1.0.0",
    author="Guneesha Sehgal",
    author_email="guneeshasehgal@gmail.com",
    description="topsis implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guneesha12/101703196_topsis/tree/v_1.0.0",
    download_url="https://github.com/guneesha12/101703196_topsis/archive/v_1.0.0.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
